#!/usr/bin/env python3
"""Verify every SKILL.md has usable frontmatter.

A skill with a missing or malformed `description` does not fail loudly - it
simply never triggers, which is the hardest class of bug to notice in a skill
bundle. This check runs in a second and catches it.

    python -m scripts.check_frontmatter
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MIN_DESCRIPTION = 60
MAX_DESCRIPTION = 1024
MAX_BODY_LINES = 500


def parse_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end]
    data: dict[str, str] = {}
    key = None
    for line in block.splitlines():
        if not line.strip():
            continue
        match = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if match:
            key = match.group(1)
            data[key] = match.group(2).strip().strip("\"'")
        elif key:
            data[key] += " " + line.strip().strip("\"'")
    return data


def check_plugin_manifests(failures: list[str]) -> int:
    """Validate the plugin manifests against the host's own limits.

    claude.ai rejects a plugin whose description exceeds 500 characters, and it
    rejects it at upload time with a validation error rather than truncating.
    That is a long way from where the description is written, so the limit is
    worth enforcing here instead of discovering it in a browser.
    """
    import json

    checked = 0
    limit = 500
    for rel in (".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"):
        path = ROOT / rel
        if not path.is_file():
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            failures.append(f"{rel}: invalid JSON — {exc}")
            continue

        entries: list[tuple[str, str]] = []
        if isinstance(data.get("description"), str):
            entries.append(("description", data["description"]))
        if isinstance(data.get("metadata"), dict) and isinstance(
            data["metadata"].get("description"), str
        ):
            entries.append(("metadata.description", data["metadata"]["description"]))
        for plugin in data.get("plugins", []) or []:
            if isinstance(plugin.get("description"), str):
                entries.append((f"plugins[{plugin.get('name', '?')}].description", plugin["description"]))

        for label, text in entries:
            checked += 1
            if len(text) > limit:
                failures.append(
                    f"{rel}: {label} is {len(text)} characters, "
                    f"{len(text) - limit} over the {limit}-character limit. "
                    "claude.ai refuses the plugin at upload rather than truncating."
                )
            elif not text.strip():
                failures.append(f"{rel}: {label} is empty")
    return checked


def main() -> int:
    targets = sorted(ROOT.glob("skills/*/SKILL.md")) + [ROOT / "SKILL.md"]
    failures: list[str] = []
    checked = 0

    for path in targets:
        if not path.is_file():
            failures.append(f"{path.relative_to(ROOT)}: missing")
            continue
        checked += 1
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        data = parse_frontmatter(text)
        if data is None:
            failures.append(f"{rel}: no YAML frontmatter block")
            continue

        name = data.get("name", "")
        description = data.get("description", "")

        if not name:
            failures.append(f"{rel}: no `name`")
        elif path.parent.name != "skills" and path.parent != ROOT and name != path.parent.name:
            failures.append(
                f"{rel}: name {name!r} does not match directory {path.parent.name!r}"
            )

        if not description:
            failures.append(f"{rel}: no `description` — this skill will never trigger")
        elif len(description) < MIN_DESCRIPTION:
            failures.append(
                f"{rel}: description is {len(description)} chars, under {MIN_DESCRIPTION}. "
                "Say what it does AND when to use it, or it will undertrigger."
            )
        elif len(description) > MAX_DESCRIPTION:
            failures.append(f"{rel}: description is {len(description)} chars, over {MAX_DESCRIPTION}")

        body_lines = text[text.find("\n---", 3) + 4 :].strip().splitlines()
        if len(body_lines) > MAX_BODY_LINES:
            failures.append(
                f"{rel}: body is {len(body_lines)} lines, over {MAX_BODY_LINES}. "
                "Move detail into references/ and point at it."
            )

    manifest_fields = check_plugin_manifests(failures)

    for failure in failures:
        print(f"FAIL  {failure}")
    print(
        f"\nchecked {checked} skill files and {manifest_fields} manifest field(s), "
        f"{len(failures)} problem(s)"
    )
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
