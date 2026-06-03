#!/usr/bin/env python3
"""
Transform every DPV 2.3 extension (the non-core modules vendored alongside
``upstream-releases/dpv/dpv/``) into per-extension LinkML schemas under
``src/dpv/schema/extensions/``.

This is the complement to ``dpv_core_to_linkml.py`` (which only handles the
``dpv/`` core release). It produces one LinkML schema per extension, each
with its own ``id``, ``name`` and ``default_prefix``, importing only
``linkml:types`` + ``dpv:schema/dpv_core`` (plus any sibling extensions
whose classes it specialises).

Layout produced (mirrors the upstream ``2.3/<ext>/`` tree):

    src/dpv/schema/extensions/
      ai.yaml                  # aggregate of ai/ai-owl.ttl
      ai/
        capabilities.yaml      # ai/modules/capabilities-owl.ttl
        core.yaml
        data.yaml
        development.yaml
        lifecycle.yaml
        measures.yaml
        risks.yaml
        systems.yaml
        techniques.yaml
      pd.yaml                  # …/pd
      pd/{core,extended}.yaml
      loc.yaml
      tech.yaml
      risk.yaml
      risk/{incident,incident_status,risk_controls,risk_levels,
            risk_management,risk_matrix,risk_taxonomy}.yaml
      justifications.yaml
      justifications/{delay,exercise,nonfulfilment,notrequired}.yaml
      legal.yaml
      legal/<cc>.yaml          # one per upstream jurisdiction (eu, de, …)
      legal/eu/{gdpr,dga,ehds,nis2,aiact,rights}.yaml
      legal/eu/gdpr/{compliance,data_breach,…}.yaml
      sector.yaml
      sector/<industry>.yaml
      standards.yaml
      standards/ieee/7012.yaml

Key design choices
==================

* Identity (LinkML) - every extension declares its own
  ``default_prefix: <slug>`` and ``id: https://w3id.org/lmodel/dpv/<path>``;
  classes carry ``class_uri: <slug>:<Name>`` rather than ``dpv:<Name>`` so
  the LinkML identity URI matches the schema's namespace.
* Identity (RDF) - the upstream W3C DPV CURIEs are recorded as
  ``exact_mappings: [dpv_<ext>:<Name>, dpv_<ext>_owl:<Name>]`` so generated
  RDF/OWL never shadows the W3C IRI.
* Cross-extension parents - classes whose ``rdfs:subClassOf`` points at a
  *different* DPV-family namespace (e.g. ``ai-owl:Foo`` ⊑ ``dpv-owl:Bar``,
  or ``eu-gdpr-owl:Foo`` ⊑ ``pd-owl:Baz``) resolve their parent local-name
  unchanged. LinkML name resolution is flat across the merged schema, so as
  long as ``Bar``/``Baz`` is declared in any imported sibling schema the
  ``is_a`` link is valid. Auto-imports are computed from observed foreign
  namespaces.
* Per-module schemas inside an extension reuse the per-module pattern
  already established in ``dpv_core_to_linkml.py``: each module schema imports
  the extension aggregate and emits the *same* classes with an
  ``in_subset: <module>_subset`` tag for downstream slicing.

Reproducibility
===============

Deterministic (stable sort of subjects, no timestamps). Re-running with
unchanged ``upstream-releases/dpv/`` produces byte-identical YAML.

Usage
-----

    uv run --with rdflib --with pyyaml \
      python scripts/dpv_extensions_to_linkml.py \
        [-i upstream-releases/dpv] \
        [-o src/dpv/schema/extensions] \
        [--report]

The DPV version is auto-detected (same logic as ``dpv_core_to_linkml.py``).
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

import rdflib
from rdflib import Graph, Literal, URIRef
from rdflib.namespace import OWL, RDF, RDFS, SKOS, XSD

# ---------------------------------------------------------------------------
# Share helpers with the core generator (keeps formatting / sanitisation
# identical between core and extensions; do not duplicate).
# ---------------------------------------------------------------------------
_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

import dpv_core_to_linkml as core  # noqa: E402

DPV_CORE_OWL_NS = core.DPV_OWL_NS              # https://w3id.org/dpv/owl#
DPV_CORE_CAN_NS = core.DPV_CAN_NS              # https://w3id.org/dpv#
DPV_FAMILY_BASE = "https://w3id.org/dpv/"
LMODEL_BASE = core.LMODEL_BASE                 # https://w3id.org/lmodel/dpv
LMODEL_EXT_BASE = f"{LMODEL_BASE}/"            # https://w3id.org/lmodel/dpv/
DCT = core.DCT

# Match every DPV-family OWL namespace, e.g.
#   https://w3id.org/dpv/owl#                 -> (slug="dpv", flavour="owl")
#   https://w3id.org/dpv/ai/owl#              -> (slug="ai", flavour="owl")
#   https://w3id.org/dpv/legal/eu/gdpr/owl#   -> (slug="legal/eu/gdpr", flavour="owl")
#   https://w3id.org/dpv/ai#                  -> (slug="ai", flavour="can")
_FAMILY_RE = re.compile(
    r"^https://w3id\.org/dpv/(?:(?P<slug>[^#]+?)/)?(?P<tail>owl#|#)"
)

# Local names we never emit as elements (LinkML metamodel / structural).
_RESERVED = core._RESERVED_LOCAL_NAMES


# ---------------------------------------------------------------------------
# Extension model
# ---------------------------------------------------------------------------

@dataclass
class ExtensionSpec:
    """A single DPV extension (aggregate file + optional submodules)."""

    slug: str                        # path under /dpv/, e.g. "ai", "legal/eu/gdpr"
    rel_path: Path                   # dir relative to input_dir, e.g. Path("ai")
    owl_ns: str                      # https://w3id.org/dpv/<slug>/owl#
    can_ns: str                      # https://w3id.org/dpv/<slug>#
    aggregate_owl: Path              # ai/ai-owl.ttl
    aggregate_can: Path | None       # ai/ai.ttl (canonical SKOS)
    submodules: list["SubmoduleSpec"] = field(default_factory=list)
    # Sibling extensions referenced from this extension's TTL (computed
    # post-hoc by scanning subClassOf / domain / range URIs).
    foreign_refs: set[str] = field(default_factory=set)

    @property
    def name(self) -> str:
        """LinkML schema ``name`` - snake_case underscored path."""
        return "dpv_" + self.slug.replace("/", "_").replace("-", "_")

    @property
    def prefix(self) -> str:
        """Default prefix for this extension (NCName)."""
        return self.slug.replace("/", "_").replace("-", "_")

    @property
    def lmodel_id(self) -> str:
        """Stable LinkML schema id under the lmodel/dpv/ w3id redirect."""
        return f"{LMODEL_BASE}/{self.slug}"

    @property
    def lmodel_ns(self) -> str:
        """Namespace IRI that ``prefix`` binds to in the generated schema."""
        return f"{LMODEL_EXT_BASE}{self.slug}/"

    @property
    def out_aggregate(self) -> Path:
        """Output path for the aggregate schema, relative to output_dir."""
        return Path(self.slug + ".yaml")

    @property
    def out_dir(self) -> Path:
        """Output directory for submodule schemas, relative to output_dir."""
        return Path(self.slug)


@dataclass
class SubmoduleSpec:
    """A per-extension module file (e.g. ai/modules/risks-owl.ttl)."""

    name: str                        # snake_case module name (e.g. "risks")
    owl_path: Path                   # ai/modules/risks-owl.ttl
    can_path: Path | None            # ai/modules/risks.ttl


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def _slug_from_owl_iri(iri: str) -> str | None:
    """Extract the DPV path slug from an OWL ontology IRI.

    >>> _slug_from_owl_iri("https://w3id.org/dpv/ai/owl#")
    'ai'
    >>> _slug_from_owl_iri("https://w3id.org/dpv/legal/eu/gdpr/owl#")
    'legal/eu/gdpr'
    >>> _slug_from_owl_iri("https://w3id.org/dpv/owl#")  # core, never an extension
    """
    m = _FAMILY_RE.match(iri)
    if not m or not m.group("slug") or m.group("tail") != "owl#":
        return None
    return m.group("slug")


def _ontology_namespace(g: Graph) -> str | None:
    """Return the ``owl:Ontology`` IRI's namespace (with trailing ``#``).

    Upstream DPV files always declare ``<ns>: a owl:Ontology`` where the IRI
    is the namespace itself (e.g. ``https://w3id.org/dpv/ai/owl#`` minus the
    ``#``). The serialiser writes it with the ``#`` stripped; we re-add it.
    """
    for s in g.subjects(RDF.type, OWL.Ontology):
        if isinstance(s, URIRef):
            iri = str(s)
            if not iri.endswith("#"):
                iri += "#"
            return iri
    return None


def discover_extensions(input_dir: Path) -> list[ExtensionSpec]:
    """Walk ``input_dir`` and return one ExtensionSpec per aggregate file.

    The aggregate file for an extension is any ``<basename>-owl.ttl`` that
    is NOT under a ``modules/`` directory AND whose declared
    ``owl:Ontology`` IRI lives below ``https://w3id.org/dpv/`` with at
    least one path segment (i.e. not the bare core ``dpv/owl#``). Each
    sibling under ``<dir>/modules/`` becomes a SubmoduleSpec sharing the
    same OWL namespace.
    """
    extensions: list[ExtensionSpec] = []

    # Find every potential aggregate file. We deliberately walk the whole
    # tree so deeply nested extensions (legal/eu/gdpr, standards/ieee/7012,
    # sector/health) are picked up uniformly.
    candidate_owls = sorted(input_dir.rglob("*-owl.ttl"))
    aggregates: list[Path] = [
        p for p in candidate_owls
        # exclude modules/ files (those become SubmoduleSpec instances)
        if p.parent.name != "modules"
        # exclude the dpv/ core (handled by dpv_core_to_linkml.py)
        and "dpv" not in {p.parent.name}
    ]

    for owl_path in aggregates:
        # Derive the slug from the path under input_dir. Upstream DPV uses
        # the path layout as the canonical namespace mirror: a file at
        # `<input>/legal/eu/gdpr/eu-gdpr-owl.ttl` corresponds to the
        # ontology IRI `https://w3id.org/dpv/legal/eu/gdpr/owl#`.
        rel_dir = owl_path.parent.relative_to(input_dir)
        slug = rel_dir.as_posix()
        if slug in {"", "."}:
            continue
        ns = f"https://w3id.org/dpv/{slug}/owl#"
        can_ns = f"https://w3id.org/dpv/{slug}#"

        # Sanity-check: the file should actually contain triples in `ns`.
        # Upstream is mostly path-consistent, but a few extensions (notably
        # `legal/eu/rights/`) declare an ontology IRI that does NOT mirror
        # the filesystem path (`https://w3id.org/dpv/rights/eu/owl#`). When
        # that happens, fall back to the actual `owl:Ontology` IRI so
        # extraction still finds the file's classes/properties.
        g = _parse_ttl(owl_path)
        if not any(str(s).startswith(ns) for s in g.subjects() if isinstance(s, URIRef)):
            actual_ns = _ontology_namespace(g)
            if actual_ns and any(
                str(s).startswith(actual_ns)
                for s in g.subjects() if isinstance(s, URIRef)
            ):
                ns = actual_ns
                can_ns = actual_ns.replace("/owl#", "#")
                print(
                    f"   [namespace-fallback] {owl_path.relative_to(input_dir)}: "
                    f"path-ns mismatched, using ontology IRI {ns}",
                    file=sys.stderr,
                )
            elif not (owl_path.parent / "modules").is_dir():
                # Truly empty shell with no submodules - skip silently.
                continue
        canonical_path = owl_path.with_name(owl_path.name.replace("-owl.ttl", ".ttl"))
        if not canonical_path.exists():
            canonical_path = None  # type: ignore[assignment]

        ext = ExtensionSpec(
            slug=slug,
            rel_path=owl_path.parent.relative_to(input_dir),
            owl_ns=ns,
            can_ns=can_ns,
            aggregate_owl=owl_path,
            aggregate_can=canonical_path,
        )

        modules_dir = owl_path.parent / "modules"
        if modules_dir.is_dir():
            for mod_owl in sorted(modules_dir.glob("*-owl.ttl")):
                mod_name = mod_owl.stem[:-len("-owl")]
                mod_can = mod_owl.with_name(f"{mod_name}.ttl")
                ext.submodules.append(SubmoduleSpec(
                    name=mod_name,
                    owl_path=mod_owl,
                    can_path=mod_can if mod_can.exists() else None,
                ))
        extensions.append(ext)

    # Stable ordering: shallowest path first, then alphabetical.
    extensions.sort(key=lambda e: (e.slug.count("/"), e.slug))
    return extensions


# ---------------------------------------------------------------------------
# Namespace-aware extraction (mirrors dpv_to_linkml.extract_*, generalised)
# ---------------------------------------------------------------------------

def _local_of(uri: URIRef, ns: str) -> str | None:
    s = str(uri)
    if not s.startswith(ns):
        return None
    local = s[len(ns):]
    if not local or "/" in local or local.startswith("serialisation-"):
        return None
    if local in _RESERVED:
        return None
    return local


def _family_local(uri: URIRef) -> tuple[str, str] | None:
    """Return (slug, local) if ``uri`` is in ANY DPV-family OWL namespace.

    ``slug`` is the empty string for the core ``dpv-owl:`` namespace, and
    a path slug otherwise. ``local`` is the post-``#`` fragment, with the
    same reserved-name / hyphen filtering as ``_local_of``.
    """
    s = str(uri)
    if not s.startswith(DPV_FAMILY_BASE):
        return None
    # Core dpv-owl:
    if s.startswith(DPV_CORE_OWL_NS):
        local = s[len(DPV_CORE_OWL_NS):]
    else:
        m = _FAMILY_RE.match(s)
        if not m or m.group("tail") != "owl#":
            return None
        local = s[m.end():]
    if not local or "/" in local or local.startswith("serialisation-"):
        return None
    if local in _RESERVED:
        return None
    slug = ""
    if s.startswith(DPV_CORE_OWL_NS):
        slug = ""
    else:
        m = _FAMILY_RE.match(s)
        assert m is not None
        slug = m.group("slug") or ""
    return slug, local


def _uri_to_curie_for(ext: ExtensionSpec, uri: URIRef) -> str | None:
    """Like ``core.uri_to_curie`` but also recognises the extension's own
    ``dpv_<slug>`` / ``dpv_<slug>_owl`` namespaces."""
    s = str(uri)
    if s.startswith(ext.owl_ns):
        return f"dpv_{ext.prefix}_owl:{s[len(ext.owl_ns):]}"
    if s.startswith(ext.can_ns):
        return f"dpv_{ext.prefix}:{s[len(ext.can_ns):]}"
    return core.uri_to_curie(uri)


def _extract_classes_ns(
    g_owl: Graph,
    g_can: Graph | None,
    ext: ExtensionSpec,
    foreign_log: set[str],
) -> dict[str, dict]:
    """Extract every owl:Class in ``ext.owl_ns`` as a LinkML class.

    ``foreign_log`` is mutated to record every external DPV-family slug
    seen on subClassOf / mixin / type triples (used to compute imports).
    """
    classes: dict[str, dict] = {}

    subjects: set[URIRef] = set()
    for t in (OWL.Class, RDFS.Class):
        for s in g_owl.subjects(RDF.type, t):
            if isinstance(s, URIRef) and _local_of(s, ext.owl_ns):
                subjects.add(s)

    structural = {OWL.Class, RDFS.Class, OWL.NamedIndividual,
                  OWL.ObjectProperty, OWL.DatatypeProperty,
                  OWL.AnnotationProperty, OWL.Ontology}

    for cls in sorted(subjects, key=str):
        cls_local = _local_of(cls, ext.owl_ns)
        assert cls_local is not None
        cls_name = core.sanitise_class_name(cls_local)
        entry: dict[str, Any] = {}

        # ---- description -----------------------------------------------
        defn = core.first_literal(g_owl, cls, SKOS.definition) \
               or core.first_literal(g_owl, cls, SKOS.scopeNote)
        if defn:
            entry["description"] = defn

        # ---- named parents (own ns + foreign DPV-family ns) ------------
        named_parents: list[tuple[str, str]] = []
        for o in g_owl.objects(cls, RDFS.subClassOf):
            if not isinstance(o, URIRef):
                continue
            fl = _family_local(o)
            if fl is None:
                continue
            slug, local = fl
            named_parents.append((slug, local))
            if slug != ext.slug:
                foreign_log.add(slug)

        if named_parents:
            parent_name = core.sanitise_class_name(named_parents[0][1])
            # Guard: a class can never be its own parent.
            if parent_name and parent_name != cls_name:
                entry["is_a"] = parent_name

        # ---- rdf:type secondary classes -> mixins ----------------------
        type_mixins: list[str] = []
        for t in g_owl.objects(cls, RDF.type):
            if not isinstance(t, URIRef) or t in structural:
                continue
            fl = _family_local(t)
            if fl is None:
                continue
            slug, local = fl
            type_mixins.append(core.sanitise_class_name(local))
            if slug != ext.slug:
                foreign_log.add(slug)

        seen = {entry.get("is_a")}
        dedup_mixins: list[str] = []
        for m in type_mixins:
            if m and m != cls_name and m not in seen:
                dedup_mixins.append(m)
                seen.add(m)
        if len(named_parents) > 1:
            for _, local in named_parents[1:]:
                m = core.sanitise_class_name(local)
                if m and m not in seen and m != cls_name:
                    dedup_mixins.append(m)
                    seen.add(m)
        if dedup_mixins:
            entry["mixins"] = dedup_mixins

        # ---- identity --------------------------------------------------
        entry["class_uri"] = f"{ext.prefix}:{cls_local}"

        # ---- aliases ---------------------------------------------------
        aliases: list[str] = []
        if cls_name != cls_local:
            aliases.append(cls_local)
        pref = core.first_literal(g_owl, cls, SKOS.prefLabel)
        if pref and pref not in aliases:
            aliases.append(pref)
        for label in core.get_literals(g_owl, cls, SKOS.altLabel):
            if label not in aliases:
                aliases.append(label)
        for label in core.get_literals(g_owl, cls, RDFS.label):
            if label not in aliases:
                aliases.append(label)
        if aliases:
            entry["aliases"] = aliases

        # ---- comments --------------------------------------------------
        comments: list[str] = []
        for sn in core.get_literals(g_owl, cls, SKOS.scopeNote):
            if sn != entry.get("description") and sn not in comments:
                comments.append(sn)
        for note in core.get_literals(g_owl, cls, SKOS.editorialNote):
            if note not in comments:
                comments.append(note)
        if comments:
            entry["comments"] = comments

        # ---- exact / close / broad / narrow / related mappings ---------
        equivs: list[str] = []
        for o in g_owl.objects(cls, OWL.equivalentClass):
            if isinstance(o, URIRef):
                curie = _uri_to_curie_for(ext, o)
                equivs.append(curie if curie else str(o))
        for o in g_owl.objects(cls, SKOS.exactMatch):
            if isinstance(o, URIRef):
                curie = _uri_to_curie_for(ext, o)
                if curie and curie not in equivs:
                    equivs.append(curie)
        # Canonical upstream identity, both flavours, under ext-specific prefixes.
        equivs.append(f"dpv_{ext.prefix}:{cls_local}")
        equivs.append(f"dpv_{ext.prefix}_owl:{cls_local}")
        seen_eq: set[str] = set()
        equivs = [e for e in equivs if not (e in seen_eq or seen_eq.add(e))]
        entry["exact_mappings"] = equivs

        for skos_pred, key in (
            (SKOS.closeMatch, "close_mappings"),
            (SKOS.broadMatch, "broad_mappings"),
            (SKOS.narrowMatch, "narrow_mappings"),
            (SKOS.relatedMatch, "related_mappings"),
            (SKOS.related, "related_mappings"),
        ):
            for o in g_owl.objects(cls, skos_pred):
                if isinstance(o, URIRef) and not _local_of(o, ext.owl_ns):
                    curie = _uri_to_curie_for(ext, o)
                    if curie:
                        entry.setdefault(key, [])
                        if curie not in entry[key]:
                            entry[key].append(curie)

        # ---- deprecation -----------------------------------------------
        if core.first_literal(g_owl, cls, OWL.deprecated) == "true":
            entry["deprecated"] = "true"

        # ---- canonical SKOS enrichment ---------------------------------
        if g_can is not None:
            canonical_subj = URIRef(ext.can_ns + cls_local)
            if (canonical_subj, None, None) in g_can:
                core._enrich_from_canonical(canonical_subj, g_can, entry)
        # Canonical enrichment may have re-introduced a self-referential
        # parent (e.g. SKOS broader pointing to the same SKOS concept);
        # strip it so generated LinkML stays acyclic.
        if entry.get("is_a") == cls_name:
            entry.pop("is_a", None)

        # ---- provenance annotations (skill enrichment) -----------------
        entry.setdefault("annotations", {}).update({
            "upstream_iri": str(cls),
            "dpv_extension_slug": ext.slug,
        })

        classes[cls_name] = entry

    return classes


def _extract_slots_ns(
    g_owl: Graph,
    g_can: Graph | None,
    ext: ExtensionSpec,
    foreign_log: set[str],
) -> dict[str, dict]:
    slots: dict[str, dict] = {}

    prop_types = (OWL.ObjectProperty, OWL.DatatypeProperty, OWL.AnnotationProperty)
    subjects: set[URIRef] = set()
    for t in prop_types:
        for s in g_owl.subjects(RDF.type, t):
            if isinstance(s, URIRef) and _local_of(s, ext.owl_ns):
                subjects.add(s)

    for prop in sorted(subjects, key=str):
        prop_local = _local_of(prop, ext.owl_ns)
        assert prop_local is not None
        sname = core.camel_to_snake(prop_local)
        entry: dict[str, Any] = {
            "definition_uri": f"{ext.prefix}:{prop_local}",
        }

        defn = core.first_literal(g_owl, prop, SKOS.definition) \
               or core.first_literal(g_owl, prop, RDFS.comment)
        if defn:
            entry["description"] = defn

        sub_of: list[tuple[str, str]] = []
        for o in g_owl.objects(prop, RDFS.subPropertyOf):
            if isinstance(o, URIRef):
                fl = _family_local(o)
                if fl:
                    sub_of.append(fl)
                    if fl[0] != ext.slug:
                        foreign_log.add(fl[0])
        if sub_of:
            parent_name = core.camel_to_snake(sub_of[0][1])
            # Guard: a slot can never be its own parent.
            if parent_name and parent_name != sname:
                entry["is_a"] = parent_name

        domains: list[str] = []
        for o in g_owl.objects(prop, RDFS.domain):
            if isinstance(o, URIRef):
                fl = _family_local(o)
                if fl:
                    domains.append(core.sanitise_class_name(fl[1]))
                    if fl[0] != ext.slug:
                        foreign_log.add(fl[0])
        if domains:
            entry["domain"] = domains[0]

        all_types = set(g_owl.objects(prop, RDF.type))
        is_datatype = OWL.DatatypeProperty in all_types

        range_uris = [o for o in g_owl.objects(prop, RDFS.range)
                      if isinstance(o, URIRef)]
        if is_datatype:
            if range_uris:
                entry["range"] = core.XSD_TO_LINKML.get(str(range_uris[0]), "string")
        else:
            dpv_ranges: list[str] = []
            for o in range_uris:
                fl = _family_local(o)
                if fl:
                    dpv_ranges.append(core.sanitise_class_name(fl[1]))
                    if fl[0] != ext.slug:
                        foreign_log.add(fl[0])
            if len(dpv_ranges) == 1:
                entry["range"] = dpv_ranges[0]
            elif len(dpv_ranges) > 1:
                entry["any_of"] = [{"range": r} for r in dpv_ranges]
            if OWL.ObjectProperty in all_types:
                entry["multivalued"] = True

        inverses: list[str] = []
        for o in g_owl.objects(prop, OWL.inverseOf):
            if isinstance(o, URIRef):
                fl = _family_local(o)
                if fl:
                    inverses.append(core.camel_to_snake(fl[1]))
        if inverses:
            entry["inverse"] = inverses[0]

        aliases: list[str] = []
        pref = core.first_literal(g_owl, prop, SKOS.prefLabel)
        if pref and pref not in aliases:
            aliases.append(pref)
        for label in core.get_literals(g_owl, prop, SKOS.altLabel):
            if label not in aliases:
                aliases.append(label)
        for label in core.get_literals(g_owl, prop, RDFS.label):
            if label not in aliases:
                aliases.append(label)
        if aliases:
            entry["aliases"] = aliases

        equivs: list[str] = []
        for o in g_owl.objects(prop, OWL.equivalentProperty):
            if isinstance(o, URIRef):
                curie = _uri_to_curie_for(ext, o)
                equivs.append(curie if curie else str(o))
        equivs.append(f"dpv_{ext.prefix}:{prop_local}")
        equivs.append(f"dpv_{ext.prefix}_owl:{prop_local}")
        seen_eq: set[str] = set()
        equivs = [e for e in equivs if not (e in seen_eq or seen_eq.add(e))]
        entry["exact_mappings"] = equivs

        if OWL.TransitiveProperty in all_types:
            entry["transitive"] = True
        if OWL.SymmetricProperty in all_types:
            entry["symmetric"] = True
        if OWL.ReflexiveProperty in all_types:
            entry["reflexive"] = True
        if core.first_literal(g_owl, prop, OWL.deprecated) == "true":
            entry["deprecated"] = "true"

        if g_can is not None:
            canonical_subj = URIRef(ext.can_ns + prop_local)
            if (canonical_subj, None, None) in g_can:
                core._enrich_from_canonical(canonical_subj, g_can, entry)
        # Strip any self-referential parent that canonical enrichment
        # might have re-introduced.
        if entry.get("is_a") == sname:
            entry.pop("is_a", None)

        # ---- provenance annotations (skill enrichment) -----------------
        entry.setdefault("annotations", {}).update({
            "upstream_iri": str(prop),
            "dpv_extension_slug": ext.slug,
        })

        slots[sname] = entry

    return slots


# ---------------------------------------------------------------------------
# Schema assembly
# ---------------------------------------------------------------------------

def _ext_prefixes(ext: ExtensionSpec, foreign: set[str]) -> dict[str, str]:
    """Prefix map for an extension schema.

    Combines the base ``_base_prefixes()`` from the core generator (so
    every standard mapping target is pre-declared and lint-clean) with
    this extension's own LinkML namespace plus its upstream OWL +
    canonical SKOS namespaces. Foreign extensions referenced from this
    schema's TTL also get their LinkML / OWL / canonical prefixes pre-
    declared so cross-extension ``is_a`` / ``range`` references resolve.
    """
    prefixes = dict(core._base_prefixes())
    # Own ext
    prefixes[ext.prefix] = ext.lmodel_ns
    prefixes[f"dpv_{ext.prefix}"] = ext.can_ns
    prefixes[f"dpv_{ext.prefix}_owl"] = ext.owl_ns
    # Each foreign extension we touched
    for slug in sorted(foreign):
        pref = slug.replace("/", "_").replace("-", "_")
        prefixes.setdefault(pref, f"{LMODEL_EXT_BASE}{slug}/")
        prefixes.setdefault(f"dpv_{pref}", f"https://w3id.org/dpv/{slug}#")
        prefixes.setdefault(f"dpv_{pref}_owl", f"https://w3id.org/dpv/{slug}/owl#")
    return prefixes


def _ext_imports(ext: ExtensionSpec, foreign: set[str]) -> list[str]:
    imports = ["linkml:types", "dpv:schema/dpv_core"]
    for slug in sorted(foreign):
        imports.append(f"dpv:schema/extensions/{slug}")
    return imports


def _humanise(slug: str) -> str:
    return slug.replace("/", " - ").replace("_", " ").title()


def build_aggregate_schema(
    ext: ExtensionSpec,
    classes: dict,
    slots: dict,
    submodule_names: list[str],
    version: str,
    foreign: set[str],
    source: str | None,
) -> dict:
    subset_name = core._module_subset_name(ext.prefix)
    subsets: dict[str, dict] = {
        subset_name: {
            "description": (
                f"All entities from the DPV `{ext.slug}` extension."
            ),
        }
    }
    for sub in sorted(submodule_names):
        subsets[core._module_subset_name(f"{ext.prefix}_{sub}")] = {
            "description": (
                f"Entities from the DPV `{ext.slug}/modules/{sub}` submodule."
            ),
        }

    schema: dict[str, Any] = {
        "id": ext.lmodel_id,
        "name": ext.name,
        "title": f"DPV - {_humanise(ext.slug)}",
        "description": (
            f"LinkML schema generated from the DPV {version} extension "
            f"`{ext.slug}` (`{ext.aggregate_owl.name}`), enriched with "
            "canonical SKOS metadata. Imports the aggregate core schema "
            "`dpv:schema/dpv_core` for the abstract parent classes "
            "this extension specialises."
        ),
        "license": "CC-BY-4.0",
        "see_also": [
            f"https://w3id.org/dpv/{ext.slug}",
            f"https://w3c.github.io/dpv/2.3/{ext.slug}/",
        ],
        "version": version,
    }
    if source:
        schema["source"] = source

    schema.update({
        "prefixes": _ext_prefixes(ext, foreign),
        "default_prefix": ext.prefix,
        "default_range": "string",
        "id_prefixes": [
            ext.prefix,
            f"dpv_{ext.prefix}",
            f"dpv_{ext.prefix}_owl",
        ],
        "imports": _ext_imports(ext, foreign),
        "subsets": subsets,
    })
    schema["annotations"] = {
        "dpv_version": version,
        "dpv_extension_slug": ext.slug,
        "source_ttl": _repo_rel(ext.aggregate_owl),
        **({"source_canonical_ttl": _repo_rel(ext.aggregate_can)}
           if ext.aggregate_can else {}),
        "upstream_owl_namespace": ext.owl_ns,
        "upstream_canonical_namespace": ext.can_ns,
    }
    if slots:
        schema["slots"] = core._order_elements(slots, subset_name)
    if classes:
        schema["classes"] = core._order_elements(classes, subset_name)
    return core._order_keys(schema, core._SCHEMA_KEY_ORDER)


def build_submodule_schema(
    ext: ExtensionSpec,
    sub: SubmoduleSpec,
    classes: dict,
    slots: dict,
    version: str,
    foreign: set[str],
    source: str | None,
) -> dict:
    subset_name = core._module_subset_name(f"{ext.prefix}_{sub.name}")
    schema: dict[str, Any] = {
        "id": f"{ext.lmodel_id}/{sub.name}",
        "name": f"{ext.name}_{sub.name}",
        "title": f"DPV - {_humanise(ext.slug)} / {sub.name.replace('_', ' ').title()}",
        "description": (
            f"LinkML schema generated from the DPV {version} extension "
            f"module `{ext.slug}/modules/{sub.owl_path.name}`."
        ),
        "license": "CC-BY-4.0",
        "see_also": [
            f"https://w3id.org/dpv/{ext.slug}",
            f"https://w3c.github.io/dpv/2.3/{ext.slug}/",
        ],
        "version": version,
    }
    if source:
        schema["source"] = source

    # Submodule imports the aggregate so we can reference its slots/classes
    # by local name (LinkML resolves names across the merged tree).
    sub_imports = ["linkml:types", "dpv:schema/dpv_core",
                   f"dpv:schema/extensions/{ext.slug}"]
    for slug in sorted(foreign):
        if slug != ext.slug:
            entry = f"dpv:schema/extensions/{slug}"
            if entry not in sub_imports:
                sub_imports.append(entry)

    schema.update({
        "prefixes": _ext_prefixes(ext, foreign),
        "default_prefix": ext.prefix,
        "default_range": "string",
        "id_prefixes": [
            ext.prefix,
            f"dpv_{ext.prefix}",
            f"dpv_{ext.prefix}_owl",
        ],
        "imports": sub_imports,
        "subsets": {
            subset_name: {
                "description": (
                    f"Entities from the DPV `{ext.slug}/modules/{sub.name}` "
                    "submodule."
                ),
            },
        },
    })
    schema["annotations"] = {
        "dpv_version": version,
        "dpv_extension_slug": ext.slug,
        "dpv_submodule": sub.name,
        "source_ttl": _repo_rel(sub.owl_path),
        **({"source_canonical_ttl": _repo_rel(sub.can_path)}
           if sub.can_path else {}),
        "upstream_owl_namespace": ext.owl_ns,
        "upstream_canonical_namespace": ext.can_ns,
    }
    if slots:
        schema["slots"] = core._order_elements(slots, subset_name)
    if classes:
        schema["classes"] = core._order_elements(classes, subset_name)
    return core._order_keys(schema, core._SCHEMA_KEY_ORDER)


# ---------------------------------------------------------------------------
# I/O helpers
# ---------------------------------------------------------------------------

def _parse_ttl(path: Path) -> Graph:
    g = Graph()
    g.parse(str(path), format="turtle")
    return g


_REPO_ROOT = Path(__file__).resolve().parent.parent


def _repo_rel(path: Path) -> str:
    """Return ``path`` as a repo-root-relative POSIX string when possible."""
    try:
        return path.resolve().relative_to(_REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def _write(schema: dict, path: Path) -> tuple[int, int]:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(core.dump_yaml(schema), encoding="utf-8")
    n_cls = len(schema.get("classes", {}))
    n_slt = len(schema.get("slots", {}))
    print(f"   -> {path.relative_to(path.parents[len(path.parents) - 1])}  "
          f"(classes={n_cls}, slots={n_slt})", file=sys.stderr)
    return n_cls, n_slt


def _patch_core_subsets(
    core_schema_path: Path,
    ext_subsets: dict[str, dict],
) -> None:
    """Merge ``ext_subsets`` into the ``subsets:`` block of ``dpv_core.yaml``.

    The core schema is written by ``dpv_core_to_linkml.py`` and already contains
    the DPV core-module subsets.  This function adds every extension subset
    so that a single ``import dpv:schema/dpv_core`` is sufficient for
    ``gen-doc`` and other consumers to resolve the complete subset index.

    Existing entries are preserved; new ones are inserted in sorted order
    after the last existing entry.  The file is only rewritten when at least
    one new subset is added.
    """
    if not core_schema_path.exists():
        print(
            f"WARN: cannot patch subsets - {core_schema_path} does not exist "
            "(run dpv_core_to_linkml.py first).",
            file=sys.stderr,
        )
        return

    import yaml as _yaml  # noqa: PLC0415 (local import; yaml is already on sys.path via core)

    raw = core_schema_path.read_text(encoding="utf-8")
    schema = _yaml.safe_load(raw)
    if not isinstance(schema, dict):
        print(f"WARN: {core_schema_path} did not parse as a dict; skipping subset patch.",
              file=sys.stderr)
        return

    existing: dict[str, dict] = schema.get("subsets") or {}
    added = {k: v for k, v in sorted(ext_subsets.items()) if k not in existing}
    if not added:
        print("\nCore subsets already up-to-date - no changes needed.", file=sys.stderr)
        return

    merged = dict(existing)
    merged.update(added)
    schema["subsets"] = merged
    core_schema_path.write_text(core.dump_yaml(schema), encoding="utf-8")
    print(
        f"\nPatched {core_schema_path.name}: added {len(added)} extension subsets "
        f"({', '.join(sorted(added)[:5])}{', ...' if len(added) > 5 else ''}).",
        file=sys.stderr,
    )


# ---------------------------------------------------------------------------
# Generation
# ---------------------------------------------------------------------------

def generate(
    input_dir: Path,
    output_dir: Path,
    version: str,
    report: bool,
) -> tuple[int, int, int]:
    """Generate every extension schema. Returns (n_ext, n_cls, n_slt)."""
    extensions = discover_extensions(input_dir)
    if not extensions:
        sys.exit(f"No DPV extensions found under {input_dir}")

    total_ext = total_cls = total_slt = 0
    # Accumulate all extension subsets so they can be patched into
    # dpv_core.yaml after generation (name -> {description}).
    all_ext_subsets: dict[str, dict] = {}

    for ext in extensions:
        print(f"\n=== Extension: {ext.slug} ({ext.aggregate_owl.name}) ===",
              file=sys.stderr)

        # --- aggregate -----------------------------------------------------
        g_owl = _parse_ttl(ext.aggregate_owl)
        g_can = _parse_ttl(ext.aggregate_can) if ext.aggregate_can else None
        if g_can is not None:
            print(f"   enriched from canonical {ext.aggregate_can.name}",
                  file=sys.stderr)

        foreign: set[str] = set()
        classes = _extract_classes_ns(g_owl, g_can, ext, foreign)
        slots = _extract_slots_ns(g_owl, g_can, ext, foreign)
        slots, moved = core._split_collision_slots_to_attributes(classes, slots)
        if moved and report:
            print(f"   collision-prone slots moved to attributes: {moved}",
                  file=sys.stderr)
        # Strip the slug for the *own* extension; only foreign refs matter.
        foreign.discard(ext.slug)
        foreign.discard("")  # core "dpv" slug is implicit via dpv_core import

        if not classes and not slots:
            print("   (skipped - aggregate empty)", file=sys.stderr)
            continue

        agg_schema = build_aggregate_schema(
            ext,
            classes,
            slots,
            submodule_names=[s.name for s in ext.submodules],
            version=version,
            foreign=foreign,
            source=core.get_ontology_iri(g_owl),
        )
        # Collect the subsets declared in this aggregate schema so they can
        # be patched into dpv_core.yaml later.
        all_ext_subsets.update(agg_schema.get("subsets") or {})

        agg_path = output_dir / ext.out_aggregate
        _write(agg_schema, agg_path)
        total_ext += 1
        total_cls += len(classes)
        total_slt += len(slots)

        if report:
            n_owl = sum(1 for s in g_owl.subjects(RDF.type, OWL.Class)
                        if isinstance(s, URIRef) and _local_of(s, ext.owl_ns))
            print(f"   coverage: owl:Class={n_owl} -> classes={len(classes)} | "
                  f"slots={len(slots)} | foreign-imports={sorted(foreign)}",
                  file=sys.stderr)

        # --- submodules ---------------------------------------------------
        for sub in ext.submodules:
            g_owl_s = _parse_ttl(sub.owl_path)
            g_can_s = _parse_ttl(sub.can_path) if sub.can_path else None
            sub_foreign: set[str] = set()
            sub_classes = _extract_classes_ns(g_owl_s, g_can_s, ext, sub_foreign)
            sub_slots = _extract_slots_ns(g_owl_s, g_can_s, ext, sub_foreign)
            sub_slots, _ = core._split_collision_slots_to_attributes(
                sub_classes, sub_slots,
            )
            sub_foreign.discard(ext.slug)
            sub_foreign.discard("")
            if not sub_classes and not sub_slots:
                continue
            sub_schema = build_submodule_schema(
                ext, sub, sub_classes, sub_slots, version,
                foreign=sub_foreign,
                source=core.get_ontology_iri(g_owl_s),
            )
            # Collect submodule subsets too.
            all_ext_subsets.update(sub_schema.get("subsets") or {})
            sub_path = output_dir / ext.out_dir / f"{sub.name}.yaml"
            _write(sub_schema, sub_path)

    # Patch dpv_core.yaml with all collected extension subsets so that a
    # single import of dpv:schema/dpv_core exposes the full subset index.
    core_schema_path = output_dir.parent / "dpv_core.yaml"
    _patch_core_subsets(core_schema_path, all_ext_subsets)

    return total_ext, total_cls, total_slt


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    default_input = repo_root / "upstream-releases" / "dpv"
    default_output = repo_root / "src" / "dpv" / "schema" / "extensions"

    parser = argparse.ArgumentParser(
        description=("Generate LinkML schemas for every DPV 2.3 extension "
                     "vendored under upstream-releases/dpv/."),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--version", default=None,
        help="Override the DPV version (default: auto-detect from core).",
    )
    parser.add_argument(
        "-i", "--input-dir", type=Path, default=default_input,
        help=("Directory containing the vendored DPV upstream tree "
              "(default: upstream-releases/dpv/)."),
    )
    parser.add_argument(
        "-o", "--output-dir", type=Path, default=default_output,
        help=f"Output directory for extension schemas "
             f"(default: {default_output.relative_to(repo_root)}).",
    )
    parser.add_argument(
        "--report", action="store_true",
        help="Print per-extension coverage summary to stderr.",
    )
    args = parser.parse_args()

    if not args.input_dir.exists():
        parser.error(f"Input directory does not exist: {args.input_dir}")

    version = args.version
    if not version:
        # Re-use the core detection logic against the core dpv/ subdir.
        core_dir = args.input_dir / "dpv"
        if core_dir.exists():
            version = core.detect_version(core_dir)
    if not version:
        parser.error(
            "Could not detect DPV version; pass --version explicitly."
        )
    print(f"DPV version: {version}", file=sys.stderr)
    print(f"Input:  {args.input_dir}", file=sys.stderr)
    print(f"Output: {args.output_dir}", file=sys.stderr)

    n_ext, n_cls, n_slt = generate(
        args.input_dir, args.output_dir, version, args.report,
    )
    print(
        f"\nDone. Extensions: {n_ext}, "
        f"classes (sum): {n_cls}, slots (sum): {n_slt}.",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
