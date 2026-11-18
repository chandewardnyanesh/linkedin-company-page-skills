#!/usr/bin/env python3
"""Fail if a filled profile or a credential is about to be committed.

`references/company-profile.md` and `references/proof-library.md` are templates
in git and private business documents once filled. A filled profile carries
positioning, pricing posture, unreleased customer names and the claims legal
has not cleared - exactly the material a public fork should not carry. The same
goes for a token pasted into `.env.example`.

The templates are recognised by `filled: no` in their Status block. Flipping
that to `yes` is what a user does when they fill one in, which is also the
signal this check keys on.

    python -m scripts.check_no_secrets
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TEMPLATES = [
    "references/company-profile.md",
    "references/proof-library.md",
    "references/icp-firmographics.md",
    "references/competitor-set.md",
    "references/claims-and-compliance.md",
]

# Credential shapes worth stopping on. Deliberately narrow: a broad entropy
# check on a marketing bundle fires on hashtags and slugs and gets ignored.
PATTERNS = [
    (re.compile(r"\bsk-[A-Za-z0-9]{20,}"), "OpenAI-style secret key"),
    (re.compile(r"\bsk_(?:live|test)_[A-Za-z0-9]{16,}"), "Stripe-style secret key"),
    (re.compile(r"\bapify_api_[A-Za-z0-9]{20,}"), "Apify token"),
    (re.compile(r"\bghp_[A-Za-z0-9]{30,}"), "GitHub personal access token"),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "AWS access key id"),
    (re.compile(r"\bBearer\s+[A-Za-z0-9._\-]{30,}"), "bearer token"),
]

SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv"}
SCAN_SUFFIXES = {".md", ".py", ".json", ".yml", ".yaml", ".txt", ".example", ""}


def main() -> int:
    failures: list[str] = []

    for rel in TEMPLATES:
        path = ROOT / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if re.search(r"^\s*-?\s*filled:\s*yes\b", text, re.I | re.M):
            failures.append(
                f"{rel} is marked `filled: yes`. This is a private business "
                "document now. Add it to .gitignore or move the filled copy "
                "outside the repo before committing."
            )

    for path in ROOT.rglob("*"):
        if not path.is_file() or SKIP_DIRS & set(path.parts):
            continue
        if path.suffix not in SCAN_SUFFIXES:
            continue
        if path.name == "check_no_secrets.py":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for pattern, label in PATTERNS:
            if pattern.search(text):
                failures.append(f"{path.relative_to(ROOT)}: looks like a {label}")

    for failure in failures:
        print(f"FAIL  {failure}")
    print(f"\n{len(failures)} problem(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
