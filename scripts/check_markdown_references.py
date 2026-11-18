#!/usr/bin/env python3
"""Verify every relative markdown path mentioned in the bundle resolves.

Progressive disclosure only works if the pointers are real. A skill that says
"see ../../references/page-formats.md" and is wrong does not error - the model
either hallucinates the content or silently proceeds without it, and the user
gets a thinner answer for a reason nobody can see. This is the check that keeps
the reference layer honest as files get renamed.

    python -m scripts.check_markdown_references
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Backtick-quoted paths that look like markdown files, plus markdown links.
_BACKTICK = re.compile(r"`([^`\n]*?\.md)`")
_LINK = re.compile(r"\]\(([^)\s]+?\.md)\)")
_SKIP_PREFIXES = ("http://", "https://", "mailto:")


def _is_path(candidate: str) -> bool:
    """Filter out backticked shell commands that merely end in a .md filename.

    `python -m scripts.fit --file draft.md` is an instruction, not a pointer at
    a file in this repo, and flagging it trains the reader to ignore this check.
    """
    if " " in candidate or candidate.startswith("-"):
        return False
    # `skills/<name>/SKILL.md` is a pattern shown to a reader, not a path that
    # resolves. Angle brackets are how this repo writes a placeholder segment.
    if "<" in candidate or ">" in candidate or "*" in candidate:
        return False
    return not candidate.startswith(_SKIP_PREFIXES)


def candidates(text: str) -> set[str]:
    found = set(_BACKTICK.findall(text)) | set(_LINK.findall(text))
    return {c.strip() for c in found if c.strip() and _is_path(c.strip())}


def main() -> int:
    files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
    failures: list[str] = []
    checked = 0

    for path in files:
        text = path.read_text(encoding="utf-8")
        for ref in sorted(candidates(text)):
            checked += 1
            # A bare filename inside prose ("write it to company-profile.md")
            # is a name, not a path. Only resolve things that look like paths.
            if "/" not in ref:
                if not list(ROOT.rglob(ref)):
                    failures.append(f"{path.relative_to(ROOT)} -> {ref} (no such file anywhere)")
                continue
            resolved = (path.parent / ref).resolve()
            if resolved.exists():
                continue
            # A path written WITHOUT a leading dot ("references/x.md") inside a
            # nested file is a repo-root-relative pointer, which is fine. A
            # path written WITH one ("../../references/x.md") is making an
            # explicit claim about depth, so it must resolve from this file or
            # it is wrong — falling back to root here would silently hide the
            # single most common error in a nested reference layer.
            if not ref.startswith("."):
                if (ROOT / ref).resolve().exists():
                    continue
            hint = ""
            if ref.startswith("."):
                target = Path(ref).name
                matches = [
                    m for m in ROOT.rglob(target) if ".git" not in m.parts
                ]
                if matches:
                    rel = os.path.relpath(matches[0], path.parent)
                    hint = f" — did you mean {rel}?"
            failures.append(f"{path.relative_to(ROOT)} -> {ref} (unresolved){hint}")

    for failure in failures:
        print(f"FAIL  {failure}")
    print(f"\nchecked {checked} reference(s) across {len(files)} files, {len(failures)} broken")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
