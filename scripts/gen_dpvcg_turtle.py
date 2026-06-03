#!/usr/bin/env python3
"""Extract individual E*.ttl Turtle snippets from the vendored DPV examples HTML.

The upstream DPV release does not ship stand-alone ``E####.ttl`` files in its
distribution archive.  The canonical Turtle content for each example is embedded
as ``<pre>`` blocks inside the examples HTML page (``dex.html``) under a section
or anchor with ``id="E####"``.

This script parses that HTML, extracts each Turtle snippet, and writes
``examples/E####.ttl`` (one file per example).  The output is consumed by
``scripts/load_examples.py``, which splits valid/problem chunks, prepends the
standard DPV prefix preamble, and routes files to ``tests/data/dpvcg/``.

Idempotent: re-running with unchanged inputs produces byte-identical output.

Usage::

    uv run python scripts/gen_example_ttls.py \\
        [-i upstream-releases/dpv/examples/dex.html] \\
        [-o examples]
"""

from __future__ import annotations

import argparse
import sys
from html.parser import HTMLParser
from pathlib import Path


# ---------------------------------------------------------------------------
# HTML parser
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def write_if_changed(path: Path, content: str) -> bool:
    if path.exists() and path.read_text() == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    return True


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent

    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "-i", "--input-html", type=Path,
        default=repo_root / "upstream-releases" / "dpv" / "examples" / "dex.html",
        help="Path to the DPV examples HTML file (dex.html).",
    )
    parser.add_argument(
        "-o", "--output-dir", type=Path,
        default=repo_root / "examples",
        help="Directory to write E####.ttl files.",
    )
    args = parser.parse_args()

    if not args.input_html.exists():
        parser.error(
            f"Input HTML not found: {args.input_html}\n"
            "Expected the vendored upstream DPV examples page."
        )

    print(f"Parsing {args.input_html} ...", file=sys.stderr)
    extractor = _TurtleExtractor()
    extractor.feed(args.input_html.read_text(encoding="utf-8"))

    if not extractor.examples:
        print(
            "ERROR: no Turtle examples found in the HTML. "
            "The file format may have changed.",
            file=sys.stderr,
        )
        sys.exit(1)

    args.output_dir.mkdir(parents=True, exist_ok=True)

    written = 0
    kept = 0
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
        f"gen_example_ttls: extracted {len(extractor.examples)} examples "
        f"({written} written, {kept} unchanged).",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
