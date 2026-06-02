"""Data test.

Validates example YAML fixtures against the dpvs LinkML schema using
``linkml.validator.Validator`` (JSON-Schema based, open-world) rather
than instantiating generated dataclasses. The dpvs schema deliberately
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
from linkml_runtime.utils.schemaview import SchemaView

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_ROOT = Path(__file__).parent / "data"
# Use the pre-merged, self-contained schema produced by `just _merged-schema`
# (see `scripts/merge_schema.py`). The source `src/dpvs/schema/dpvs.yaml`
# imports `dpvs:schema/dpvs_core` via a URI-style CURIE; resolving that
# import requires the build-time import map, and `SchemaView` falls back
# to fetching the URI over HTTP without it (404 on the w3id IRI — see
# ISSUE.md §8/§9). The merged YAML has `imports:` already flattened, so
# no import resolution is needed at test time.
SCHEMA_PATH = REPO_ROOT / "tmp" / "dpvs.yaml"

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
def validator() -> Validator:
    """Build a single ``Validator`` over the merged dpvs schema.

    Uses the pre-merged, self-contained YAML at ``tmp/dpvs.yaml`` so
    there are no URI imports left for ``SchemaView`` to (mis-)resolve.
    """
    if not SCHEMA_PATH.exists():
        pytest.skip(
            f"Merged schema not found at {SCHEMA_PATH}. "
            "Run `just _merged-schema` first (or `just gen-project`)."
        )
    sv = SchemaView(str(SCHEMA_PATH))
    return Validator(sv.schema)


def _target_class_for(filepath: str) -> str:
    """Filename convention: ``<TargetClass>-...yaml``."""
    return Path(filepath).stem.split("-")[0]


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath, validator):
    """Each valid fixture must validate against its target class."""
    target_class = _target_class_for(filepath)
    report = validator.validate_source(
        YamlLoader(filepath), target_class=target_class
    )
    assert not report.results, (
        f"{Path(filepath).name} (target={target_class}) failed validation:\n"
        + "\n".join(f"  - {r.severity}: {r.message}" for r in report.results)
    )


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files(filepath, validator):
    """Each invalid fixture must fail validation against its target class."""
    target_class = _target_class_for(filepath)
    report = validator.validate_source(
        YamlLoader(filepath), target_class=target_class
    )
    assert report.results, (
        f"{Path(filepath).name} (target={target_class}) was expected to fail "
        "validation but no validation errors were reported."
    )
