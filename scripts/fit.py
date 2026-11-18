#!/usr/bin/env python3
"""Check a draft against a LinkedIn Page surface limit.

    python -m scripts.fit --surface page_post --file draft.md
    python -m scripts.fit --surface tagline --text "Your tagline here"
    python -m scripts.fit --list

Exit code is 1 when the draft breaks a hard limit, so this can gate a step.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lib.surfaces import DOCUMENT_SPEC, SOURCE, SURFACES, fit  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--surface", default="page_post")
    parser.add_argument("--file")
    parser.add_argument("--text")
    parser.add_argument("--target", type=int, help="Length the user asked for.")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--list", action="store_true", help="Show every surface.")
    args = parser.parse_args(argv)

    if args.list:
        print("LinkedIn Page surfaces\n")
        for key, spec in SURFACES.items():
            limit = "no limit" if spec.limit is None else f"{spec.limit} chars"
            fold = f", fold {spec.fold_desktop}" if spec.fold_desktop else ""
            sweet = f", sweet spot {spec.sweet_spot[0]}-{spec.sweet_spot[1]}" if spec.sweet_spot else ""
            print(f"  {key:<18} {spec.name} — {limit}{fold}{sweet}")
        print("\nDocument post (measured in pages, not characters):")
        for key, value in DOCUMENT_SPEC.items():
            if key != "note":
                print(f"  {key}: {value}")
        print(f"\n{DOCUMENT_SPEC['note']}\n\nSources: {SOURCE}")
        return 0

    if args.file:
        text = Path(args.file).read_text(encoding="utf-8")
    elif args.text is not None:
        text = args.text
    else:
        text = sys.stdin.read()

    try:
        verdict = fit(text, args.surface, target=args.target)
    except KeyError as exc:
        print(exc, file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(verdict, indent=2))
        return 0 if verdict["ok"] else 1

    remaining = verdict["remaining"]
    tail = "" if remaining is None else f"  ({remaining:+d} to the limit)"
    print(f"{verdict['surface_name']}: {verdict['length']} characters{tail}")
    for problem in verdict["problems"]:
        print(f"  FAIL  {problem}")
    for note in verdict["notes"]:
        print(f"  note  {note}")
    fold = verdict.get("fold") or {}
    for label in ("mobile", "desktop"):
        window = fold.get(label)
        if isinstance(window, dict):
            marker = "…" if window["truncated"] else ""
            print(f"\n  above the fold ({label}, {window['threshold']} chars):")
            print(f"    {window['visible'].strip()}{marker}")
    return 0 if verdict["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
