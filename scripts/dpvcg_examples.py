#!/usr/bin/env python3
"""DPV-CG examples pipeline: extract -> load -> to-yaml.

A single CLI exposing the three stages that turn the upstream DPV examples
HTML page into LinkML-validatable YAML fixtures:

``extract``
    Pull each ``<pre>`` Turtle block out of ``dex.html`` (anchored on
    ``id="E####"``) and write ``examples/E####.ttl``.

``load``
    Wrap each ``E####.ttl`` in the standard prefix preamble, split
    upstream ``# problem`` chunks, sanity-parse with rdflib, and route
    files to ``tests/data/dpvcg/{valid,problem,invalid}/``.

``to-yaml``
    Walk the generated LinkML schemas to build IRI -> element-name
    indexes, then convert each wrapped TTL fixture under
    ``tests/data/dpvcg/valid/`` to one YAML document per typed root
    subject (``<ClassName>-<stem>-<n>.yaml``) so ``tests/test_data.py``
    can validate them against the dpv datamodel.

Every stage is idempotent: re-running with unchanged inputs produces
byte-identical output.

Usage::

    uv run python scripts/dpvcg_examples.py extract  [-i HTML] [-o DIR]
    uv run python scripts/dpvcg_examples.py load     [-i DIR]  [-o DIR]
    uv run python scripts/dpvcg_examples.py to-yaml  [-s DIR]  [-i DIR] [-o DIR]
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

import rdflib
import yaml
from rdflib import BNode, Graph, Literal, URIRef
from rdflib.namespace import RDF

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import write_if_changed, yaml_dump_indented  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent

# Same local/upstream/OWL DPV namespaces the generator uses.
DPV_LOCAL_NS = "https://w3id.org/lmodel/dpv/"
DPV_CAN_NS = "https://w3id.org/dpv#"
DPV_OWL_NS = "https://w3id.org/dpv/owl#"
LMODEL_DPV_NS = "https://w3id.org/lmodel/dpv/"


# ===========================================================================
# Stage 1: extract  (was scripts/gen_dpvcg_turtle.py)
# ===========================================================================

class _TurtleExtractor(HTMLParser):
    """Extract Turtle ``<pre>`` blocks keyed by the nearest ``E####`` anchor."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._current_ex: str | None = None
        self._in_pre: int = 0
        self._buf: list[str] = []
        # Maps example-id (e.g. "E0001") -> Turtle text
        self.examples: dict[str, str] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        d = dict(attrs)
        eid = d.get("id") or ""
        # An element whose id is "E####" marks the start of an example section.
        # We track the most recently seen one so that a subsequent <pre> is
        # attributed to the right example.
        if len(eid) >= 5 and eid[0] == "E" and eid[1:].isdigit():
            self._current_ex = eid
        if tag == "pre":
            self._in_pre += 1
            self._buf = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "pre" and self._in_pre:
            self._in_pre -= 1
            content = "".join(self._buf).strip()
            if (
                content
                and self._current_ex
                and self._current_ex not in self.examples
                and (
                    "dpv:" in content
                    or "dpv_upstream:" in content
                    or "ex:" in content
                    or "@prefix" in content
                )
            ):
                self.examples[self._current_ex] = content

    def handle_data(self, data: str) -> None:
        if self._in_pre:
            self._buf.append(data)


def cmd_extract(args: argparse.Namespace) -> int:
    if not args.input_html.exists():
        print(
            f"Input HTML not found: {args.input_html}\n"
            "Expected the vendored upstream DPV examples page.",
            file=sys.stderr,
        )
        return 2

    print(f"Parsing {args.input_html} ...", file=sys.stderr)
    extractor = _TurtleExtractor()
    extractor.feed(args.input_html.read_text(encoding="utf-8"))

    if not extractor.examples:
        print(
            "ERROR: no Turtle examples found in the HTML. "
            "The file format may have changed.",
            file=sys.stderr,
        )
        return 1

    args.output_dir.mkdir(parents=True, exist_ok=True)

    written = kept = 0
    written_paths: set[Path] = set()
    for eid in sorted(extractor.examples):
        content = extractor.examples[eid] + "\n"
        out = args.output_dir / f"{eid}.ttl"
        written_paths.add(out)
        if write_if_changed(out, content):
            written += 1
        else:
            kept += 1

    # Prune stale E*.ttl files from previous runs.
    for existing in args.output_dir.glob("E*.ttl"):
        if existing not in written_paths:
            existing.unlink()

    print(
        f"extract: {len(extractor.examples)} examples "
        f"({written} written, {kept} unchanged).",
        file=sys.stderr,
    )
    return 0


# ===========================================================================
# Stage 2: load  (was scripts/load_dpvcg_turtle.py)
# ===========================================================================

PREAMBLE = """\
@prefix : <https://example.org/dpv/default#> .
@prefix bibo: <http://purl.org/ontology/bibo/> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix dex: <https://w3id.org/dpv/examples#> .
@prefix dpv: <https://w3id.org/lmodel/dpv> .
@prefix dpv_upstream: <https://w3id.org/dpv#> .
@prefix eu-gdpr: <https://w3id.org/dpv/legal/eu/gdpr#> .
@prefix ex: <https://example.org/dpv/ex#> .
@prefix exA: <https://example.org/dpv/exA#> .
@prefix exB: <https://example.org/dpv/exB#> .
@prefix extension: <https://w3id.org/dpv/extension#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix justifications: <https://w3id.org/dpv/justifications#> .
@prefix legal-eu: <https://w3id.org/dpv/legal/eu#> .
@prefix legal-ie: <https://w3id.org/dpv/legal/ie#> .
@prefix loc: <https://w3id.org/dpv/loc#> .
@prefix nace: <https://w3id.org/dpv/nace#> .
@prefix odrl: <http://www.w3.org/ns/odrl/2/> .
@prefix org: <http://www.w3.org/ns/org#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix pd: <https://w3id.org/dpv/pd#> .
@prefix profile: <http://www.w3.org/ns/dx/prof/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix risk: <https://w3id.org/dpv/risk#> .
@prefix schema: <https://schema.org/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix tech: <https://w3id.org/dpv/tech#> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
"""

PROBLEM_RE = re.compile(r"^\s*#\s*problem\b", re.IGNORECASE)
SOLUTION_RE = re.compile(r"^\s*#\s*(solution|valid|fix)\b", re.IGNORECASE)


def split_chunks(text: str) -> tuple[str, list[str]]:
    """Return (valid_text, [problem_chunks]).

    Chunks beginning with a ``# problem`` comment line and ending at the
    next ``# solution`` / ``# valid`` / ``# problem`` marker (or EOF) are
    pulled into the problem list. Everything else stays in valid.
    """
    lines = text.splitlines(keepends=True)
    valid: list[str] = []
    problems: list[list[str]] = []
    current: list[str] | None = None

    for line in lines:
        if PROBLEM_RE.match(line):
            if current is not None:
                problems.append(current)
            current = [line]
        elif current is not None and SOLUTION_RE.match(line):
            problems.append(current)
            current = None
            valid.append(line)
        elif current is not None:
            current.append(line)
        else:
            valid.append(line)

    if current is not None:
        problems.append(current)

    return "".join(valid), ["".join(c) for c in problems]


def _wrap(body: str) -> str:
    """Prepend the prefix preamble and ensure a single trailing newline."""
    body = body.rstrip() + "\n"
    return PREAMBLE + "\n" + body


def _parses(content: str) -> bool:
    try:
        rdflib.Graph().parse(data=content, format="turtle")
    except Exception:  # noqa: BLE001
        return False
    return True


def cmd_load(args: argparse.Namespace) -> int:
    if not args.input_dir.exists():
        print(f"Input directory does not exist: {args.input_dir}", file=sys.stderr)
        return 2

    valid_dir = args.output_dir / "valid"
    invalid_dir = args.output_dir / "invalid"
    problem_dir = args.output_dir / "problem"
    for d in (valid_dir, invalid_dir, problem_dir):
        d.mkdir(parents=True, exist_ok=True)

    # Placeholder so the invalid/ folder is tracked even when empty.
    placeholder = invalid_dir / ".gitkeep"
    if not placeholder.exists():
        placeholder.write_text("")

    n_valid = n_problem = n_skipped = 0
    written: set[Path] = set()

    for src in sorted(args.input_dir.glob("E*.ttl")):
        text = src.read_text()
        valid_body, problem_chunks = split_chunks(text)

        if valid_body.strip():
            content = _wrap(valid_body)
            # Route to valid/ when the wrapped snippet round-trips through
            # rdflib; otherwise the snippet is intentionally fragmentary or
            # malformed and belongs in problem/ for downstream review.
            target_dir = valid_dir if _parses(content) else problem_dir
            out = target_dir / f"{src.stem}.ttl"
            if write_if_changed(out, content):
                if target_dir is valid_dir:
                    n_valid += 1
                else:
                    n_problem += 1
            written.add(out)
        else:
            n_skipped += 1

        for i, chunk in enumerate(problem_chunks, 1):
            content = _wrap(chunk)
            out = problem_dir / f"{src.stem}-problem-{i}.ttl"
            if write_if_changed(out, content):
                n_problem += 1
            written.add(out)

    # Prune stale fixtures from earlier runs to keep the tree deterministic.
    for d in (valid_dir, problem_dir):
        for existing in d.glob("E*.ttl"):
            if existing not in written:
                existing.unlink()

    print(
        f"load: valid={n_valid} problem={n_problem} skipped={n_skipped}",
        file=sys.stderr,
    )
    return 0


# ===========================================================================
# Stage 3: to-yaml  (was scripts/dpvcg_turtle_to_yaml.py)
# ===========================================================================

def _expand_curie(curie: str, prefixes: dict[str, str]) -> str | None:
    """Expand a CURIE using the schema's prefix table; return None on miss."""
    if ":" not in curie or curie.startswith(("http://", "https://")):
        return curie if curie.startswith(("http://", "https://")) else None
    prefix, _, local = curie.partition(":")
    base = prefixes.get(prefix)
    return base + local if base else None


def _collect_uris(
    element: dict, prefixes: dict[str, str], identity_key: str
) -> list[str]:
    """Return every full IRI that identifies this element (identity + maps)."""
    uris: list[str] = []
    if identity_key in element:
        expanded = _expand_curie(element[identity_key], prefixes)
        if expanded:
            uris.append(expanded)
    for mapping_key in ("exact_mappings", "close_mappings", "narrow_mappings"):
        for curie in element.get(mapping_key, []) or []:
            expanded = _expand_curie(curie, prefixes)
            if expanded:
                uris.append(expanded)
    return uris


def build_indexes(schema_dir: Path) -> tuple[dict[str, str], dict[str, str]]:
    """Walk every ``*.yaml`` in ``schema_dir`` and return:

    * ``classes``: full IRI -> LinkML class name (PascalCase)
    * ``slots``:   full IRI -> LinkML slot name (snake_case)

    A URI may map to multiple LinkML names across schemas. We keep the
    first occurrence in sort-stable schema order so the chosen name is
    deterministic across runs.
    """
    classes: dict[str, str] = {}
    slots: dict[str, str] = {}

    yaml_files = sorted(schema_dir.rglob("*.yaml"))
    for sf in yaml_files:
        try:
            doc = yaml.safe_load(sf.read_text()) or {}
        except yaml.YAMLError as exc:
            print(f"WARN: cannot parse {sf}: {exc}", file=sys.stderr)
            continue
        prefixes = doc.get("prefixes") or {}

        # Default identity (per the skill): class_uri / slot_uri default to
        # {default_prefix}:{ElementName} when not declared explicitly.
        default_prefix = doc.get("default_prefix")
        default_base = prefixes.get(default_prefix) if default_prefix else None

        for cname, cdef in (doc.get("classes") or {}).items():
            cdef = cdef or {}
            uris = _collect_uris(cdef, prefixes, "class_uri")
            if not uris and default_base:
                uris.append(default_base + cname)
            for uri in uris:
                classes.setdefault(uri, cname)
            # per-class attributes: act as slots scoped to that class
            for aname, adef in (cdef.get("attributes") or {}).items():
                adef = adef or {}
                a_uris = _collect_uris(adef, prefixes, "slot_uri")
                if not a_uris and default_base:
                    a_uris.append(default_base + aname)
                for uri in a_uris:
                    slots.setdefault(uri, aname)

        for sname, sdef in (doc.get("slots") or {}).items():
            sdef = sdef or {}
            uris = _collect_uris(sdef, prefixes, "slot_uri")
            if not uris and default_base:
                uris.append(default_base + sname)
            for uri in uris:
                slots.setdefault(uri, sname)

    return classes, slots


# Compact, stable CURIE prefixes for *emitted* identifiers.
_EMIT_PREFIXES: list[tuple[str, str]] = [
    (DPV_LOCAL_NS, "dpv"),
    (DPV_CAN_NS, "dpv_upstream"),
    (DPV_OWL_NS, "dpv_owl"),
    ("https://w3id.org/dpv/legal/eu/gdpr#", "eu-gdpr"),
    ("https://w3id.org/dpv/legal/eu#", "legal-eu"),
    ("https://w3id.org/dpv/legal/ie#", "legal-ie"),
    ("https://w3id.org/dpv/loc#", "loc"),
    ("https://w3id.org/dpv/nace#", "nace"),
    ("https://w3id.org/dpv/pd#", "pd"),
    ("https://w3id.org/dpv/risk#", "risk"),
    ("https://w3id.org/dpv/tech#", "tech"),
    ("https://w3id.org/dpv/justifications#", "justifications"),
    ("https://w3id.org/dpv/extension#", "extension"),
    ("https://example.org/dpv/ex#", "ex"),
    ("https://example.org/dpv/exA#", "exA"),
    ("https://example.org/dpv/exB#", "exB"),
    ("https://example.org/dpv/default#", ""),
    ("http://www.w3.org/2004/02/skos/core#", "skos"),
    ("http://purl.org/dc/terms/", "dct"),
    ("http://schema.org/", "schema"),
    ("https://schema.org/", "schema"),
    ("http://www.w3.org/ns/odrl/2/", "odrl"),
    ("http://www.w3.org/2006/time#", "time"),
    ("http://www.w3.org/ns/org#", "org"),
    ("http://xmlns.com/foaf/0.1/", "foaf"),
    (LMODEL_DPV_NS, "dpv"),
]


def _to_curie(uri: str) -> str:
    for ns, pfx in _EMIT_PREFIXES:
        if uri.startswith(ns):
            local = uri[len(ns):]
            return f"{pfx}:{local}" if pfx else local
    return uri


def _term_to_json(term: Any) -> Any:
    if isinstance(term, Literal):
        return str(term)
    if isinstance(term, URIRef):
        return _to_curie(str(term))
    if isinstance(term, BNode):
        return f"_:{term}"
    return str(term)


def _subject_id(subj: Any) -> str:
    if isinstance(subj, BNode):
        return f"_:{subj}"
    return _to_curie(str(subj))


def _root_class_for(
    subj: Any, graph: Graph, class_index: dict[str, str]
) -> str | None:
    """Pick the most specific LinkML class for ``subj`` from ``rdf:type``
    triples, falling back to alphabetical for determinism."""
    candidates: list[str] = []
    for o in graph.objects(subj, RDF.type):
        if isinstance(o, URIRef):
            name = class_index.get(str(o))
            if name:
                candidates.append(name)
    if not candidates:
        return None
    # Prefer the longest name (heuristic for specificity), tie-break alpha.
    candidates.sort(key=lambda n: (-len(n), n))
    return candidates[0]


def convert_ttl(
    src: Path,
    class_index: dict[str, str],
    slot_index: dict[str, str],
) -> list[tuple[str, dict, dict | None]]:
    """Return [(filename_stem_part, yaml_dict, unmapped_or_none), ...]
    for one TTL fixture."""
    graph = Graph()
    graph.parse(src, format="turtle")

    emitted: list[tuple[str, dict, dict | None]] = []
    typed_subjects = sorted(
        {s for s in graph.subjects(RDF.type, None)
         if isinstance(s, URIRef) and _root_class_for(s, graph, class_index)},
        key=str,
    )
    for idx, subj in enumerate(typed_subjects, 1):
        cls_name = _root_class_for(subj, graph, class_index)
        if cls_name is None:
            continue
        obj: dict[str, Any] = {"id": _subject_id(subj)}

        # Collect predicates -> list of object renderings.
        bucket: dict[str, list[Any]] = defaultdict(list)
        unbucket: dict[str, list[Any]] = defaultdict(list)
        for p, o in graph.predicate_objects(subj):
            if p == RDF.type:
                continue
            slot_name = slot_index.get(str(p))
            value = _term_to_json(o)
            if slot_name:
                bucket[slot_name].append(value)
            else:
                unbucket[_to_curie(str(p))].append(value)

        for k, vs in bucket.items():
            obj[k] = vs[0] if len(vs) == 1 else sorted(vs, key=str)
        unmapped_out: dict[str, Any] | None = None
        if unbucket:
            unmapped_out = {
                k: (vs[0] if len(vs) == 1 else sorted(vs, key=str))
                for k, vs in unbucket.items()
            }

        emitted.append((f"{cls_name}-{src.stem}-{idx}", obj, unmapped_out))

    return emitted


def cmd_to_yaml(args: argparse.Namespace) -> int:
    if not args.schema_dir.exists():
        print(
            f"Schema directory not found: {args.schema_dir}\n"
            "Run dpv_core_to_linkml.py first to generate the schema.",
            file=sys.stderr,
        )
        return 2
    if not args.input_dir.exists():
        print(
            f"Input directory not found: {args.input_dir}\n"
            "Run `dpvcg_examples.py load` first.",
            file=sys.stderr,
        )
        return 2

    print(f"indexing schema under {args.schema_dir} ...", file=sys.stderr)
    class_index, slot_index = build_indexes(args.schema_dir)
    print(
        f"  indexed {len(class_index)} class IRIs, "
        f"{len(slot_index)} slot IRIs",
        file=sys.stderr,
    )
    if not class_index:
        print(
            "ERROR: no classes indexed; the schema directory appears empty.",
            file=sys.stderr,
        )
        return 1

    args.output_dir.mkdir(parents=True, exist_ok=True)

    written = 0
    skipped = 0
    untyped: list[str] = []
    written_paths: set[Path] = set()

    for src in sorted(args.input_dir.glob("E*.ttl")):
        try:
            docs = convert_ttl(src, class_index, slot_index)
        except Exception as exc:  # noqa: BLE001
            print(f"  ! {src.name}: parse failed: {exc}", file=sys.stderr)
            skipped += 1
            continue
        if not docs:
            untyped.append(src.name)
            continue
        for stem, doc, unmapped in docs:
            out = args.output_dir / f"{stem}.yaml"
            body = yaml_dump_indented(doc, sort_keys=True)
            # Unmapped predicates are preserved as a leading YAML comment
            # block (rather than an ``__unmapped__`` key) so the file is
            # loadable by the generated Pydantic / dataclass models while
            # still leaving the triples visible for downstream curation.
            if unmapped:
                lines = ["# __unmapped__:"]
                unmapped_yaml = yaml_dump_indented(unmapped, sort_keys=True)
                for ln in unmapped_yaml.splitlines():
                    lines.append(f"#   {ln}" if ln else "#")
                content = "\n".join(lines) + "\n" + body
            else:
                content = body
            if write_if_changed(out, content):
                written += 1
            written_paths.add(out)

    # Prune stale converted YAMLs from previous runs (only those we own:
    # ``<ClassName>-E####-<n>.yaml`` pattern).
    stale_re = re.compile(r"^[A-Z][A-Za-z0-9_]+-E\d+-\d+\.yaml$")
    for existing in args.output_dir.glob("*.yaml"):
        if stale_re.match(existing.name) and existing not in written_paths:
            existing.unlink()

    print(
        f"to-yaml: wrote/updated {written} YAML documents; "
        f"skipped {skipped} TTL files; {len(untyped)} fixtures yielded "
        f"no typed root subject",
        file=sys.stderr,
    )
    if untyped:
        print("  fixtures with no typed root:", file=sys.stderr)
        for n in untyped[:20]:
            print(f"    - {n}", file=sys.stderr)
        if len(untyped) > 20:
            print(f"    ... ({len(untyped) - 20} more)", file=sys.stderr)
    return 0


# ===========================================================================
# CLI
# ===========================================================================

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__.splitlines()[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_ext = sub.add_parser("extract", help="dex.html -> examples/E####.ttl")
    p_ext.add_argument(
        "-i", "--input-html", type=Path,
        default=REPO_ROOT / "upstream-releases" / "dpv" / "examples" / "dex.html",
        help="Path to the DPV examples HTML file (dex.html).",
    )
    p_ext.add_argument(
        "-o", "--output-dir", type=Path,
        default=REPO_ROOT / "examples",
        help="Directory to write E####.ttl files.",
    )
    p_ext.set_defaults(func=cmd_extract)

    p_load = sub.add_parser(
        "load", help="examples/E####.ttl -> tests/data/dpvcg/{valid,problem}/",
    )
    p_load.add_argument(
        "-i", "--input-dir", type=Path,
        default=REPO_ROOT / "examples",
        help="Directory containing E*.ttl fragments.",
    )
    p_load.add_argument(
        "-o", "--output-dir", type=Path,
        default=REPO_ROOT / "tests" / "data" / "dpvcg",
        help="Output root with valid/, invalid/, problem/ subdirs.",
    )
    p_load.set_defaults(func=cmd_load)

    p_yaml = sub.add_parser(
        "to-yaml", help="valid/*.ttl -> <ClassName>-<stem>-<n>.yaml",
    )
    p_yaml.add_argument(
        "-s", "--schema-dir", type=Path,
        default=REPO_ROOT / "src" / "dpv" / "schema",
        help="Directory containing generated LinkML schemas.",
    )
    p_yaml.add_argument(
        "-i", "--input-dir", type=Path,
        default=REPO_ROOT / "tests" / "data" / "dpvcg" / "valid",
        help="Directory of wrapped TTL fixtures from `load`.",
    )
    p_yaml.add_argument(
        "-o", "--output-dir", type=Path,
        default=REPO_ROOT / "tests" / "data" / "dpvcg" / "valid",
        help="Directory to write per-subject YAML documents.",
    )
    p_yaml.set_defaults(func=cmd_to_yaml)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
