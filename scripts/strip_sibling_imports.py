"""Prepare a DPV extension YAML for isolated gen-doc rendering.

Strategy
--------
Each ``src/dpv/schema/extensions/<slug>.yaml`` imports the core schema
``dpv:schema/dpv`` plus zero or more sibling extensions. For per-
extension doc generation we want one self-contained document per
extension, but two upstream-DPV irregularities block a naive merge:

1. **Cross-extension name collisions** -- e.g. ``DataAggregationBias``
   declared in both ``ai`` and ``risk``; ``DpvData`` declared in both
   ``ai`` and core ``dpv_personal_data`` -- with *different* ``class_uri``
   values. ``SchemaLoader`` refuses to merge such pairs ("Conflicting
   URIs").

2. **Cross-schema parent / mixin references** -- extension classes
   regularly use ``is_a`` and ``mixins`` pointing at classes declared
   in core (e.g. ``AISystem.mixins=[DpvSystem]``). Stripping the core
   import to dodge (1) then leaves those references dangling.

This script produces a self-contained per-extension YAML by:

* dropping **all** non-built-in imports (sibling extensions *and* the
  core schema), so SchemaLoader has nothing left to merge against;
* dropping any local ``is_a`` / ``mixins`` / slot-``is_a`` references
  whose target is not declared locally in the same extension.

The resulting YAML is self-contained and merge-safe. ``gen-doc`` then
renders an isolated reference for each extension: cross-schema parent
relationships are lost in the docs (acceptable for v1; the upstream
DPV cross-references can be re-introduced later via gen-doc template
customisation if needed).

Usage:
    python scripts/strip_sibling_imports.py <src.yaml> <dst.yaml>
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

KEEP_IMPORTS = {"linkml:types"}


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("usage: strip_sibling_imports.py <src.yaml> <dst.yaml>", file=sys.stderr)
        return 2
    src, dst = Path(argv[1]), Path(argv[2])
    data = _load_yaml(src)

    original_imports = list(data.get("imports") or [])
    data["imports"] = [i for i in original_imports if i in KEEP_IMPORTS]

    classes = data.get("classes") or {}
    slots = data.get("slots") or {}
    local_class_names = set(classes)
    local_slot_names = set(slots)

    stripped_isa = stripped_mixins = stripped_slot_isa = 0

    for cls_def in classes.values():
        if not isinstance(cls_def, dict):
            continue
        parent = cls_def.get("is_a")
        if parent and parent not in local_class_names:
            del cls_def["is_a"]
            stripped_isa += 1
        mixins = cls_def.get("mixins")
        if isinstance(mixins, list):
            kept = [m for m in mixins if m in local_class_names]
            stripped_mixins += len(mixins) - len(kept)
            if kept:
                cls_def["mixins"] = kept
            else:
                cls_def.pop("mixins", None)

    for slot_def in slots.values():
        if not isinstance(slot_def, dict):
            continue
        parent = slot_def.get("is_a")
        if parent and parent not in local_slot_names:
            del slot_def["is_a"]
            stripped_slot_isa += 1

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")

    print(
        f"  imports kept: {data['imports']} "
        f"(dropped {len(original_imports) - len(data['imports'])}); "
        f"dangling class is_a stripped: {stripped_isa}, "
        f"dangling mixins stripped: {stripped_mixins}, "
        f"dangling slot is_a stripped: {stripped_slot_isa}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

