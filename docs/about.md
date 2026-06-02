# About dpvs

**dpvs** is a [LinkML](https://linkml.io) port of the
[W3C Data Privacy Vocabulary (DPV) v2.3](https://w3c.github.io/dpv/).
It re-expresses the upstream OWL release as a single, navigable LinkML
schema together with curated cross-walks to other privacy, AI, security
and compliance vocabularies (ISO, NIST, OCSF, OSCAL, ODRL, Gist, CDM, …).

## Why a LinkML port?

The canonical DPV release ships as OWL / RDF and HTML. That form is
authoritative, but it is awkward to consume from typical data-engineering
toolchains. By re-expressing DPV in LinkML we get, from a single source
of truth:

- Pydantic / dataclass / SQL / GraphQL / JSON-Schema bindings via
  `gen-project`.
- Markdown documentation, DBML diagrams, SPARQL, SHACL, OWL and
  Pandera artifacts via the standard LinkML generators.
- A simple substrate for authoring SSSOM mappings to adjacent
  ontologies, so that DPV concepts can be referenced consistently
  across heterogeneous compliance stacks.
- Round-trippable example fixtures that double as conformance tests.

## Design

### Schema layout

- [src/dpvs/schema/dpvs.yaml](https://github.com/lmodel/dpvs/blob/main/src/dpvs/schema/dpvs.yaml) — top-level
  schema (prefix `dpvs:` → `https://w3id.org/lmodel/dpvs/`). Re-exports
  the aggregate core schema.
- [src/dpvs/schema/dpvs_core.yaml](https://github.com/lmodel/dpvs/blob/main/src/dpvs/schema/dpvs_core.yaml) —
  ~973 classes and ~145 slots covering every term in upstream DPV 2.3
  (TOM, consent, context, contract, entities, jurisdiction, legal
  basis, notice, personal data, processing, purposes, rights, risk,
  rules, status, technical measures, …).
- [src/dpvs/schema/modules/](https://github.com/lmodel/dpvs/tree/main/src/dpvs/schema/modules) — per-module
  subset schemas. Both standalone-consumable and importable from
  `dpvs.yaml`. All imports across the tree use the canonical URI form
  (e.g. `dpvs:schema/dpvs_core`) rather than relative file paths, so
  the same schema files resolve locally during build and over
  [w3id.org/lmodel](https://w3id.org/lmodel/) once published. See
  [Build pipeline](#build-pipeline) for the import-map mechanics.
- [src/dpvs/mappings/](https://github.com/lmodel/dpvs/tree/main/src/dpvs/mappings) — SSSOM cross-walks.

### Open-world modelling

DPV is intrinsically open-world: most properties are declared on the
top-level `DpvThing` rather than pinned to a specific class, so any
instance may carry any DPV property that makes sense for it.

This is preserved in dpvs:

- `DpvThing` is the abstract base and declares only `id`.
- DPV properties are domainless slots that can apply to any descendant.
- Validation is therefore done via `linkml.validator.Validator` against
  the merged schema (JSON-Schema semantics), **not** by instantiating
  the generated closed-world dataclasses. The closed-world Pydantic
  classes are still emitted for use cases where a stricter contract is
  desired.

### Mappings

Cross-walks live under [src/dpvs/mappings/](https://github.com/lmodel/dpvs/tree/main/src/dpvs/mappings) as
[SSSOM](https://mapping-commons.github.io/sssom/) TSVs and are merged
into the schema as `exact_mappings`, `close_mappings`,
`related_mappings`, etc. by the
[apply_sssom_overlay.py](https://github.com/lmodel/dpvs/blob/main/scripts/apply_sssom_overlay.py) script.
Current cross-walks:

| File | Target |
| --- | --- |
| `dpv-cdm.sssom.tsv` | FINOS Common Domain Model |
| `dpv-gist.sssom.tsv` | Semantic Arts Gist |
| `dpv-iso.sssom.tsv` | ISO/IEC general privacy terms |
| `dpv-iso22989.sssom.tsv` | ISO/IEC 22989 (AI concepts) |
| `dpv-iso27001.sssom.tsv` | ISO/IEC 27001 (ISMS) |
| `dpv-iso29100-lmodel.sssom.tsv` | ISO/IEC 29100 (privacy framework) |
| `dpv-iso42001.sssom.tsv` | ISO/IEC 42001 (AI management) |
| `dpv-nist-ai-rmf.sssom.tsv` | NIST AI Risk Management Framework |
| `dpv-nist-csf-v2.sssom.tsv` | NIST Cybersecurity Framework v2 |
| `dpv-ocsf.sssom.tsv` | OCSF |
| `dpv-odrl.sssom.tsv` | W3C ODRL |
| `dpv-oscal.sssom.tsv` | NIST OSCAL |

Mappings are verified by
[scripts/verify_mappings.py](https://github.com/lmodel/dpvs/blob/main/scripts/verify_mappings.py), which
project-agnostically auto-discovers schemas by `default_prefix` and
checks that every `subject_id` resolves to an element in some schema.

### Examples and tests

- [tests/data/](https://github.com/lmodel/dpvs/tree/main/tests/data) contains hand-authored and vendored
  YAML fixtures split into `valid/` and `invalid/` subtrees. The
  `dpvcg/` subtree carries the upstream DPV CG examples converted to
  LinkML YAML by [scripts/ttl_to_yaml.py](https://github.com/lmodel/dpvs/blob/main/scripts/ttl_to_yaml.py).
- [tests/test_data.py](https://github.com/lmodel/dpvs/blob/main/tests/test_data.py) validates each fixture
  against the schema using `linkml.validator.Validator` with
  `SchemaView(..., merge_imports=True)` so that the relative
  `./dpvs_core` import resolves against the schema directory rather
  than the test working directory.
- Fixture generation is fully automated: `just test` (via `_test-python`)
  runs `_gen-fixtures`, which chains three steps:
  1. `_extract-example-ttls` —
     [scripts/gen_example_ttls.py](https://github.com/lmodel/dpvs/blob/main/scripts/gen_example_ttls.py)
     parses `upstream-releases/dpv/examples/dex.html` and writes one
     `examples/E####.ttl` per embedded `<pre>` block. The upstream
     release does not ship stand-alone `E*.ttl` files; the Turtle
     content lives only in the HTML documentation page.
  2. `_load-ttl-fixtures` —
     [scripts/load_examples.py](https://github.com/lmodel/dpvs/blob/main/scripts/load_examples.py)
     wraps each `examples/E*.ttl` in a self-contained Turtle document
     (prepending the standard DPV prefix preamble) and routes it to
     `tests/data/dpvcg/valid/` or `problem/` based on rdflib parse
     success.
  3. `_gen-fixtures` —
     [scripts/ttl_to_yaml.py](https://github.com/lmodel/dpvs/blob/main/scripts/ttl_to_yaml.py)
     converts each typed root subject into a
     `<ClassName>-<stem>-<n>.yaml` fixture that `test_data.py` picks
     up automatically via its glob. Idempotent: re-running with
     unchanged inputs produces byte-identical output.
- `just _test-examples` runs the same fixtures through
  `linkml-run-examples` for CLI parity.

### Build pipeline

- `just` orchestrates everything; common targets include
  `gen-project`, `_test-python`, `_test-examples`, `lint`, `doc`.
  `_test-python` depends on `_gen-fixtures` → `_load-ttl-fixtures` →
  `_extract-example-ttls` so the full fixture pipeline (HTML extraction
  → TTL wrapping → YAML conversion) always runs before pytest.
- URI imports are resolved at build time via an import map. The
  source-of-truth [`importmap.json`](https://github.com/lmodel/dpvs/blob/main/importmap.json) uses relative
  paths for portability and IDE consumption; the `_importmap` recipe
  materialises an absolute-path copy at `tmp/importmap.json` (required
  because `SchemaLoader` joins import-map values with the importing
  schema's directory). Set `LINKML_IMPORT_MAP=` (empty) to fall back
  to HTTP resolution against `w3id.org`.
- [scripts/merge_schema.py](https://github.com/lmodel/dpvs/blob/main/scripts/merge_schema.py) flattens the
  schema into a self-contained YAML before feeding it to `gen-project`.
  This works around a LinkML upstream bug (raised upstream) where
  SchemaLoader-based sub-generators (`python`, `sqltable`, `excel`)
  construct a secondary `SchemaView` without propagating `--importmap`
  and therefore HTTP-fetch URI imports they cannot resolve.
- `gen_dpv_27560.py` and the `gen_*_patched.py` scripts work around
  several LinkML generator edge-cases that surface on a schema this
  large (DBML, Pandera, RDF, SPARQL, Markdown data-dictionary).
- [scripts/dpv_to_linkml.py](https://github.com/lmodel/dpvs/blob/main/scripts/dpv_to_linkml.py) regenerates
  `dpvs_core.yaml` from the vendored upstream OWL release under
  [upstream-releases/dpv/](https://github.com/lmodel/dpvs/tree/main/upstream-releases/dpv).

## Status

This is an early-stage but functional port. Key milestones:

- ✅ Full DPV 2.3 surface area (973 classes / 145 slots) generated
  from upstream OWL.
- ✅ Open-world validation honored by `tests/test_data.py` and the
  `linkml-run-examples` CLI path.
- ✅ 12 SSSOM cross-walks authored / regenerated; verifier checks every
  row against the schema.
- ✅ Upstream DPV CG examples round-tripped from TTL into LinkML YAML
  and exercised in CI; unmapped predicates preserved as
  `# __unmapped__:` provenance comments so nothing is silently dropped.
  The upstream release ships only a monolithic HTML page (`dex.html`);
  [scripts/gen_example_ttls.py](https://github.com/lmodel/dpvs/blob/main/scripts/gen_example_ttls.py)
  extracts 88 individual `E####.ttl` snippets from it. The full
  pipeline (HTML → TTL → wrapped TTL → 176 YAML fixtures) is wired
  into `just test` via `_gen-fixtures` — no manual step required.
- ✅ URI-style imports (`dpvs:schema/...`) wired across `dpvs.yaml`
  and all 33 module schemas, with build-time resolution via
  `importmap.json` and post-publication resolution via
  [w3id.org/lmodel](https://w3id.org/lmodel/). `gen-project`,
  `gen-doc` and all 12 sub-generators complete cleanly.
- ✅ Per-module subsets are first-class in the generated documentation:
  `dpvs_core.yaml` declares `core_subset` plus one `<module>_subset`
  per module (35 total), and every class/slot is tagged with its
  module membership via `in_subset`. `gen-doc` renders a dedicated
  page for each subset. Per-module schemas under `modules/` remain
  usable standalone but are intentionally not imported by `dpvs.yaml`
  to avoid duplicate `from_schema` resolution in `gen-project`.
- ✅ Class-name collision avoidance trimmed to the minimum needed:
  DPV-domain terms (`Consent`, `Contract`, `Notice`, `Policy`,
  `Purpose`, `Right`, `Risk`, `Rule`, `Status`, `Assessment`) keep
  their natural names; only generic primitives that collide with
  Python typing or common base classes (`Agent`, `Organisation`,
  `Person`, `Process`, `Service`, …) are emitted as `Dpv*`.
- 🚧 Generator patches (`gen_*_patched.py`) consolidate workarounds for
  upstream LinkML issues (raised upstream); upstreaming is in progress.
- 🚧 Documentation site at
  [https://lmodel.github.io/dpvs](https://lmodel.github.io/dpvs) is
  generator-driven and tracks `main`.

## See also

- [W3C DPV](https://w3c.github.io/dpv/) — upstream source.
- [LinkML](https://linkml.io) — the modelling language used here.
- [SSSOM](https://mapping-commons.github.io/sssom/) — the mapping format
  used for the cross-walks.
- [CONTRIBUTING.md](https://github.com/lmodel/dpvs/blob/main/CONTRIBUTING.md) — how to file changes.
