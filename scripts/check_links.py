#!/usr/bin/env python3
"""Check that every relative Markdown link and backticked file path in the skill resolves.

Placeholders used in templates and docs (foo.md, your-*.md, {model}.md) are ignored.
Exit status 1 lists every broken reference; run in CI on every pull request.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLACEHOLDER = re.compile(r"(^|/)(foo|your-[\w-]+|\{[\w-]+\})\.md$")
LINK = re.compile(r"\]\(([^)#\s]+?\.(?:md|ya?ml|webp|png|jpe?g|json))(?:#[^)]*)?\)")
TICK = re.compile(r"`((?:assets|layouts|styles|prompts|presets|recovery|reference|spec|adapters|agents|skill|references|examples|scripts)/[\w./-]+\.(?:md|ya?ml|json|py))`")


def main() -> int:
    broken: list[str] = []
    for md in sorted(ROOT.rglob("*.md")):
        if any(part.startswith(".") for part in md.relative_to(ROOT).parts):
            continue
        text = md.read_text(encoding="utf-8")
        refs = {m.group(1) for m in LINK.finditer(text)} | {m.group(1) for m in TICK.finditer(text)}
        for ref in sorted(refs):
            if ref.startswith(("http://", "https://", "mailto:")) or PLACEHOLDER.search(ref):
                continue
            if not ((md.parent / ref).exists() or (ROOT / ref).exists()):
                broken.append(f"{md.relative_to(ROOT)} → {ref}")
    # Every module file must be reachable from its index, or the engine will never load it.
    indexes = {
        "adapters": ROOT / "adapters" / "registry.md",
        "presets": ROOT / "presets" / "registry.md",
        "styles": ROOT / "reference" / "file-index.md",
        "layouts": ROOT / "reference" / "file-index.md",
        "prompts": ROOT / "reference" / "file-index.md",
    }
    unlisted: list[str] = []
    for folder, index in indexes.items():
        if not index.exists():
            continue
        listed = index.read_text(encoding="utf-8")
        for f in sorted((ROOT / folder).glob("*.md")):
            if f.name in {"registry.md", "_template.md"} or f == index:
                continue
            if f.name not in listed:
                unlisted.append(f"{folder}/{f.name} is not listed in {index.relative_to(ROOT)}")
    if broken or unlisted:
        if broken:
            print("Broken references:\n  " + "\n  ".join(broken))
        if unlisted:
            print("Unlisted modules:\n  " + "\n  ".join(unlisted))
        return 1
    print("All Markdown references resolve and every module is indexed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
