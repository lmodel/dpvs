"""Data test.

Validates example YAML fixtures against the dpv LinkML schema using
``linkml.validator.Validator`` (JSON-Schema based, open-world) rather
than instantiating generated dataclasses. The dpv schema deliberately
declares DPV properties as domainless (open-world) on ``DpvThing``, so
the generated Pydantic / dataclass ``__init__`` would reject any DPV
property that is not explicitly modelled on a concrete subclass. The
LinkML validator honours the schema's open-world intent and matches
what ``just _test-examples`` (``linkml-run-examples``) does at the CLI.
"""

import glob
import os
from pathlib import Path

import pytest
from linkml.validator import Validator
from linkml.validator.loaders import YamlLoader
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.utils.schemaview import SchemaView

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_ROOT = Path(__file__).parent / "data"
# Use the pre-merged, self-contained schema produced by `just _merged-schema`
# (see `scripts/merge_linkml_schema.py`). The source `src/dpv/schema/dpv.yaml`
# imports `dpv:schema/dpv_core` via a URI-style CURIE; resolving that
# import requires the build-time import map, and `SchemaView` falls back
# to fetching the URI over HTTP without it (404 on the w3id IRI - see
# ISSUE.md §8/§9). The merged YAML has `imports:` already flattened, so
# no import resolution is needed at test time.
SCHEMA_PATH = REPO_ROOT / "tmp" / "dpv.yaml"

# Recursively pick up every YAML example under tests/data/**/valid/ and
# tests/data/**/invalid/ so that subordinate corpora (e.g. dpvcg/) are
# exercised alongside the top-level valid/ and invalid/ directories.
VALID_EXAMPLE_FILES = sorted(
    glob.glob(os.path.join(DATA_ROOT, "**", "valid", "*.yaml"), recursive=True)
)
INVALID_EXAMPLE_FILES = sorted(
    glob.glob(os.path.join(DATA_ROOT, "**", "invalid", "*.yaml"), recursive=True)
)


@pytest.fixture(scope="session")
def schema_view() -> SchemaView:
    if not SCHEMA_PATH.exists():
        pytest.skip(
            f"Merged schema not found at {SCHEMA_PATH}. "
            "Run `just _merged-schema` first (or `just gen-project`)."
        )
    return SchemaView(str(SCHEMA_PATH))


@pytest.fixture(scope="session")
def validator(schema_view: SchemaView) -> Validator:
    """Build a single ``Validator`` over the merged dpv schema.

    Uses the pre-merged, self-contained YAML at ``tmp/dpv.yaml`` so
    there are no URI imports left for ``SchemaView`` to (mis-)resolve.
    """
    return Validator(schema_view.schema, validation_plugins=[JsonschemaValidationPlugin()])


def _target_class_for(filepath: str) -> str:
    """Filename convention: ``<TargetClass>-...yaml``."""
    return Path(filepath).stem.split("-")[0]


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


def _build_target_index(sv: SchemaView) -> dict[str, str]:
    index: dict[str, str] = {}
    for class_name, class_def in sv.schema.classes.items():
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


@pytest.fixture(scope="session")
def target_index(schema_view: SchemaView) -> dict[str, str]:
    return _build_target_index(schema_view)


def _resolve_target_class(
    requested: str,
    schema_view: SchemaView,
    target_index: dict[str, str],
    fallback_class: str = "DpvThing",
) -> str:
    classes = schema_view.schema.classes
    if requested in classes:
        return requested
    resolved = target_index.get(_normalize_target(requested))
    if resolved:
        return resolved
    if fallback_class in classes:
        return fallback_class
    return requested


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath, validator, schema_view, target_index):
    """Each valid fixture must validate against its target class."""
    target_class = _resolve_target_class(
        _target_class_for(filepath),
        schema_view,
        target_index,
    )
    report = validator.validate_source(
        YamlLoader(filepath), target_class=target_class
    )
    assert not report.results, (
        f"{Path(filepath).name} (target={target_class}) failed validation:\n"
        + "\n".join(f"  - {r.severity}: {r.message}" for r in report.results)
    )


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files(filepath, validator, schema_view, target_index):
    """Each invalid fixture must fail validation against its target class."""
    target_class = _resolve_target_class(
        _target_class_for(filepath),
        schema_view,
        target_index,
    )
    report = validator.validate_source(
        YamlLoader(filepath), target_class=target_class
    )
    assert report.results, (
        f"{Path(filepath).name} (target={target_class}) was expected to fail "
        "validation but no validation errors were reported."
    )
