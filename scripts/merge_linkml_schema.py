"""Pre-merge a LinkML schema, resolving URI-style imports via the import map.

Why this script exists
----------------------
The SchemaLoader-based generators in LinkML (``gen-pydantic`` and the
``python``/``sqltable``/``excel`` slots of ``gen-project``) construct a
secondary ``SchemaView`` from the already-merged schema *without* propagating
the ``importmap`` they were given. That secondary view re-reads the merged
schema's preserved ``imports:`` list and HTTP-fetches every URI entry,
ignoring the local import map entirely. For canonical URI imports such as
``dpv:schema/dpv_core`` this manifests as a hard 404 at build time before
the upstream package is published.

The workaround is to flatten the schema once, up-front, and then strip the
non-built-in entries from ``imports:`` so the secondary view has nothing left
to re-resolve. ``linkml:types`` is preserved because it resolves from the
linkml_runtime package catalog and is required by the framework.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml
from linkml.utils.schemaloader import SchemaLoader
from linkml_runtime.dumpers import yaml_dumper

# After SchemaLoader merges everything (including the built-in linkml types),
# the merged schema attributes every element to the top-level schema's URI.
# If we leave *any* import in the list, a downstream SchemaLoader re-resolves
# that import and tries to re-merge its elements, producing
# "Conflicting URIs ... for item: string"-style errors. So strip them all.
BUILTIN_IMPORTS: set[str] = set()


def merge(schema_path: Path, importmap_path: Path, output_path: Path) -> None:
    loader = SchemaLoader(
        str(schema_path),
        importmap=str(importmap_path),
        mergeimports=True,
    )
    loader.resolve()
    schema = loader.schema
    schema.imports = [imp for imp in (schema.imports or []) if imp in BUILTIN_IMPORTS]
    schema.source_file = str(schema_path.resolve())
    output_path.parent.mkdir(parents=True, exist_ok=True)
    serialized = yaml_dumper.dumps(schema)
    output_path.write_text(serialized)
    # Sanity check: make sure the round-tripped file actually has no leftover
    # URI imports (defensive against future linkml_runtime serializer changes).
    parsed = yaml.safe_load(output_path.read_text())
    leftover = [i for i in parsed.get("imports", []) if i not in BUILTIN_IMPORTS]
    if leftover:
        raise SystemExit(f"Unexpected leftover imports in {output_path}: {leftover}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("schema", type=Path, help="Path to the entry-point LinkML schema YAML")
    parser.add_argument("--importmap", type=Path, required=True, help="Path to the importmap JSON")
    parser.add_argument("--output", type=Path, required=True, help="Path of merged YAML to write")
    args = parser.parse_args(argv)
    merge(args.schema, args.importmap, args.output)
    print(f"Wrote merged schema: {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
