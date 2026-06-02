#!/usr/bin/env python3
"""Generate the ``dpv_27560`` LinkML module from ``schema/dpv-27560.ttl``.

Reads the upstream DPV-27560 (ISO/IEC 27560:2023 Consent Records) TTL stub and
writes a deterministic LinkML module to
``linkml/src/dpvs/schema/modules/dpvs_27560.yaml``.

Each ``rdfs:Class`` in the ``dpv-27560:`` namespace becomes a LinkML class:

* ``name`` — kebab-case local name sanitised to NCName (``-`` → ``_``)
* ``class_uri`` — upstream CURIE preserved via ``dpv_27560_upstream:``
* ``title`` / ``description`` — taken from ``dct:title``
* ``aliases`` — original kebab-case local name when sanitisation occurred

Idempotent: classes are emitted in sorted order; re-running with unchanged
input produces a byte-identical YAML file.

Usage::

    uv run python scripts/gen_dpv_27560.py \\
        [-i ../schema/dpv-27560.ttl] [-o src/dpvs/schema/modules/dpvs_27560.yaml]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml
from rdflib import Graph, Namespace
from rdflib.namespace import DCTERMS, RDFS

DPV_27560_NS = "https://w3id.org/dpv/schema/dpv-27560#"
LMODEL_NS = "https://w3id.org/lmodel/dpvs-27560/"

DPV_27560 = Namespace(DPV_27560_NS)


def to_pascal(local: str) -> str:
    """Convert a kebab/snake-case local name to PascalCase NCName.

    ``record`` -> ``Record``; ``record-eu-gdpr`` -> ``RecordEuGdpr``.
    """
    parts = re.split(r"[^A-Za-z0-9]+", local)
    return "".join(p[:1].upper() + p[1:] for p in parts if p)


def build_schema(graph: Graph) -> dict:
    classes: dict[str, dict] = {}
    subjects = sorted(
        s for s in graph.subjects(predicate=None, object=RDFS.Class)
        if str(s).startswith(DPV_27560_NS)
    )
    for subj in subjects:
        local = str(subj)[len(DPV_27560_NS):]
        name = to_pascal(local)
        title_lit = graph.value(subj, DCTERMS.title)
        title = str(title_lit) if title_lit is not None else local

        cls: dict = {
            # Identity: we own this IRI (dpvs-27560 w3id redirect).
            "class_uri": f"dpvs_27560:{local}",
            "title": title,
            "description": title,
            "aliases": [local],
            # Upstream W3C IRI recorded as a mapping target, never identity.
            "exact_mappings": [f"dpv_27560:{local}"],
        }
        classes[name] = cls

    return {
        "id": "https://w3id.org/lmodel/dpvs-27560",
        "name": "dpvs-27560",
        "title": "DPV — ISO/IEC 27560:2023 Consent Records",
        "description": (
            "LinkML schema generated from the DPV profile for ISO/IEC "
            "27560:2023 (Consent Records and Receipts). Sourced from the "
            "upstream `schema/dpv-27560.ttl`."
        ),
        "license": "CC-BY-4.0",
        "see_also": [
            "https://w3id.org/dpv/schema/dpv-27560",
            "https://www.iso.org/standard/80392.html",
        ],
        "source": DPV_27560_NS,
        "version": "2.3",
        "prefixes": {
            # Identity (we own).
            "dpvs_27560": LMODEL_NS,
            # Upstream identities — mapping targets only.
            "dpv_27560": DPV_27560_NS,
            "dpv": "https://w3id.org/dpv#",
            "linkml": "https://w3id.org/linkml/",
            "skos": "http://www.w3.org/2004/02/skos/core#",
            "dcterms": "http://purl.org/dc/terms/",
        },
        "default_prefix": "dpvs_27560",
        "default_range": "string",
        "imports": ["linkml:types"],
        "classes": classes,
    }


def dump_yaml(schema: dict) -> str:
    return yaml.safe_dump(
        schema,
        sort_keys=False,
        default_flow_style=False,
        allow_unicode=True,
        width=100,
    )


def write_if_changed(path: Path, content: str) -> bool:
    if path.exists() and path.read_text() == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    return True


def main() -> None:
    linkml_root = Path(__file__).resolve().parent.parent
    dpv_repo_root = linkml_root.parent

    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "-i", "--input", type=Path,
        default=dpv_repo_root / "schema" / "dpv-27560.ttl",
        help="Upstream DPV-27560 Turtle file.",
    )
    parser.add_argument(
        "-o", "--output", type=Path,
        default=linkml_root / "src" / "dpvs" / "schema" / "modules"
                / "dpvs_27560.yaml",
        help="Output LinkML module YAML.",
    )
    args = parser.parse_args()

    if not args.input.exists():
        parser.error(f"Input does not exist: {args.input}")

    graph = Graph()
    graph.parse(args.input, format="turtle")
    schema = build_schema(graph)
    content = dump_yaml(schema)

    changed = write_if_changed(args.output, content)
    print(
        f"gen_dpv_27560: {'wrote' if changed else 'unchanged'} {args.output} "
        f"({len(schema['classes'])} classes)",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
