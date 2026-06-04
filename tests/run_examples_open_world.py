#!/usr/bin/env python
"""Open-world drop-in replacement for ``linkml-run-examples``.

Why this script exists
======================

The upstream ``linkml-run-examples`` CLI (and the underlying
``linkml-validate`` CLI, and the default ``_get_default_validator``
factory in ``linkml.validator``) all hardcode
``JsonschemaValidationPlugin(closed=True)``. With ``closed=True`` the
generated JSON Schema for every class carries
``additionalProperties: false``, so any DPV slot that is declared
domain-less (i.e. on no specific class) is rejected on every instance
even though the schema deliberately permits it.

That hardcoded ``closed=True`` is incompatible with the dpv design
(see ``docs/about.md`` -> "Open-world modelling"): DPV properties are
intentionally attached to ``DpvThing`` rather than to a specific class
so that any instance can carry any DPV property that makes sense for
it. The pytest suite already runs the open-world validator (matching
the design). This script gives the ``just _test-examples`` recipe the
same semantics, so the example pipeline and the unit tests cannot
disagree.

It also still:

* Iterates ``--input-directory`` (must validate) and
  ``--counter-example-input-directory`` (must fail validation).
* Resolves the target class from the filename
  (``<TargetClass>-<rest>.yaml``).
* Writes round-trip YAML/JSON copies of each successful positive
  example to ``--output-directory``.
* Emits a Markdown summary on stdout (the justfile redirects this
  into ``examples/output/README.md``), mirroring the shape of the
  report produced by the stock CLI.

This is a project-local workaround. See ``ISSUE.md`` for the upstream
gap that motivates it.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml
from linkml.validator import Validator
from linkml.validator.loaders import YamlLoader
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml.validator.report import Severity
from linkml_runtime.utils.schemaview import SchemaView


@dataclass
class CaseResult:
    name: str
    target_class: str
    ok: bool
    messages: list[str]


def _target_class_for(path: Path) -> str:
    return path.stem.split("-")[0]


def _normalize_target(value: str) -> str:
    return "".join(ch.lower() for ch in value if ch.isalnum())


def _iter_candidate_names(value: str) -> list[str]:
    candidates = {value}
    if ":" in value:
        candidates.add(value.split(":", 1)[1])
    if "#" in value:
        candidates.add(value.rsplit("#", 1)[1])
    if "/" in value:
        candidates.add(value.rstrip("/").rsplit("/", 1)[1])
    return [c for c in candidates if c]


def _build_target_index(schema) -> dict[str, str]:
    index: dict[str, str] = {}
    for class_name, class_def in schema.classes.items():
        raw_names: list[str] = [class_name]
        if getattr(class_def, "name", None):
            raw_names.append(class_def.name)
        if getattr(class_def, "class_uri", None):
            raw_names.append(class_def.class_uri)
        raw_names.extend(getattr(class_def, "aliases", []) or [])
        for raw in raw_names:
            for candidate in _iter_candidate_names(str(raw)):
                index.setdefault(_normalize_target(candidate), class_name)
    return index


def _resolve_target_class(
    requested: str,
    schema,
    target_index: dict[str, str],
    fallback_class: str = "DpvThing",
) -> tuple[str, str | None]:
    if requested in schema.classes:
        return requested, None
    resolved = target_index.get(_normalize_target(requested))
    if resolved:
        return resolved, f'target class "{requested}" resolved to "{resolved}"'
    if fallback_class in schema.classes:
        return (
            fallback_class,
            (
                f'target class "{requested}" not found in schema; '
                f'validated against fallback "{fallback_class}"'
            ),
        )
    return requested, f'target class "{requested}" not found in schema'


def _validate_one(
    validator: Validator,
    schema,
    target_index: dict[str, str],
    path: Path,
) -> CaseResult:
    requested_target = _target_class_for(path)
    target, resolution_note = _resolve_target_class(requested_target, schema, target_index)
    try:
        report = validator.validate_source(YamlLoader(str(path)), target_class=target)
    except Exception as exc:  # pragma: no cover - defensive
        return CaseResult(
            path.name,
            target,
            ok=False,
            messages=[f"loader error: {exc}"],
        )
    errors = [
        f"{r.severity}: {r.message}"
        for r in report.results
        if r.severity in (Severity.ERROR, Severity.FATAL)
    ]
    messages = list(errors)
    if messages and resolution_note:
        messages.insert(0, f"note: {resolution_note}")
    return CaseResult(path.name, target, ok=not errors, messages=messages)


def _write_roundtrips(src: Path, out_dir: Path) -> None:
    """Copy the example as YAML and JSON into ``out_dir``.

    Matches the artifact layout the stock ``linkml-run-examples``
    produces so downstream tooling (and the docs site) keep working.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    with src.open() as fh:
        data = yaml.safe_load(fh)
    (out_dir / f"{src.stem}.yaml").write_text(yaml.safe_dump(data, sort_keys=True))
    (out_dir / f"{src.stem}.json").write_text(json.dumps(data, indent=2, sort_keys=True))


def _render_report(
    positives: list[CaseResult],
    negatives: list[CaseResult],
) -> str:
    lines: list[str] = []
    lines.append("# Example validation report")
    lines.append("")
    lines.append(
        "_Generated by `scripts/run_examples_open_world.py` "
        "(open-world drop-in for `linkml-run-examples`; see `ISSUE.md`)._"
    )
    lines.append("")

    def _section(title: str, cases: list[CaseResult], must_pass: bool) -> None:
        passed = sum(1 for c in cases if c.ok is must_pass)
        lines.append(f"## {title} ({passed}/{len(cases)})")
        lines.append("")
        if not cases:
            lines.append("_No cases._")
            lines.append("")
            return
        for c in cases:
            expected_ok = (c.ok is must_pass)
            mark = "OK" if expected_ok else "FAIL"
            lines.append(f"- **{mark}** `{c.name}` (target: `{c.target_class}`)")
            if not expected_ok:
                for m in c.messages or ["(no error reported but one was expected)"]:
                    lines.append(f"    - {m}")
        lines.append("")

    _section("Positive examples (must validate)", positives, must_pass=True)
    _section("Counter examples (must fail validation)", negatives, must_pass=False)
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--schema", required=True, type=Path)
    parser.add_argument("--input-directory", required=True, type=Path)
    parser.add_argument(
        "--counter-example-input-directory", required=True, type=Path
    )
    parser.add_argument("--output-directory", required=True, type=Path)
    parser.add_argument(
        "--closed",
        action="store_true",
        help=(
            "Use closed-world JSON Schema validation (matches stock "
            "`linkml-run-examples`). Off by default because the dpv "
            "schema is intentionally open-world."
        ),
    )
    args = parser.parse_args()

    # Schema is expected to be the pre-merged, self-contained YAML
    # produced by `scripts/merge_linkml_schema.py` (e.g. `tmp/dpv.yaml`).
    # We deliberately do NOT pass `merge_imports=True` here because the
    # top-level `src/dpv/schema/dpv.yaml` imports the semantic-group schemas
    # (e.g. `dpv:schema/dpv_common`) as URI-style CURIEs; `SchemaView` would
    # expand the `dpv:` prefix
    # to its w3id IRI and fetch the import over HTTP (404). See
    # ISSUE.md §8/§9 for the upstream gap. The build pipeline
    # (`just _merged-schema`) flattens imports out-of-band.
    schema = SchemaView(str(args.schema)).schema
    target_index = _build_target_index(schema)
    validator = Validator(
        schema, validation_plugins=[JsonschemaValidationPlugin(closed=args.closed)]
    )

    positives = [
        _validate_one(validator, schema, target_index, p)
        for p in sorted(args.input_directory.glob("*.yaml"))
    ]
    negatives = [
        _validate_one(validator, schema, target_index, p)
        for p in sorted(args.counter_example_input_directory.glob("*.yaml"))
    ]

    # Round-trip artifacts for the positives that validated.
    for case, src in zip(
        positives, sorted(args.input_directory.glob("*.yaml"))
    ):
        if case.ok:
            _write_roundtrips(src, args.output_directory)

    print(_render_report(positives, negatives))

    pos_failures = [c for c in positives if not c.ok]
    neg_failures = [c for c in negatives if c.ok]
    if pos_failures or neg_failures:
        sys.stderr.write(
            f"\n{len(pos_failures)} positive example(s) failed validation, "
            f"{len(neg_failures)} counter-example(s) unexpectedly passed.\n"
        )
        for c in pos_failures:
            sys.stderr.write(f"  POSITIVE FAIL: {c.name} (target={c.target_class})\n")
            for m in c.messages:
                sys.stderr.write(f"    - {m}\n")
        for c in neg_failures:
            sys.stderr.write(
                f"  COUNTER-EXAMPLE UNEXPECTEDLY PASSED: {c.name} "
                f"(target={c.target_class})\n"
            )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
