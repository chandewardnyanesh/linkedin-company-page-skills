#!/usr/bin/env python3
"""Verify the bundle's instructions stay consistent with each other.

These are the failures that no amount of careful writing prevents on its own,
because they appear when a *different* file changes:

  * A skill names a sibling skill that no longer exists, so the handoff dead
    ends and the model improvises.
  * A rule gets copied into two files, which is how two paths quietly stop
    agreeing (`references/precedence.md` §Handoffs says the fix goes in the
    receiver and is cited by both).
  * A skill that reads outside text loses its untrusted-content rule.
  * A writing skill stops citing the proof library, which is the one gate that
    keeps a fabricated figure out of a company's public claims.

Run with: python -m tests.test_instruction_integrity
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Skills that pull in text the business did not write. Each must carry the
# untrusted-content rule, because the same session can publish as the Page.
READS_OUTSIDE_TEXT = {
    "page-profile-builder",
    "trend-radar",
    "competitor-page-analyzer",
    "page-repurposer",
    "page-asset-extractor",
    "page-engagement-desk",
    "page-performance-report",
}

# Skills that put words into public. Each must gate claims on the proof library.
PRODUCES_PUBLIC_COPY = {
    "page-optimizer",
    "page-post-writer",
    "authority-article-writer",
    "page-humanizer",
    "page-repurposer",
    "employee-amplification",
    "page-engagement-desk",
}

failures: list[str] = []
checks = 0


def check(condition: bool, message: str) -> None:
    global checks
    checks += 1
    if not condition:
        failures.append(message)


def skill_dirs() -> list[Path]:
    return sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())


def main() -> int:
    skills = {p.name: (p / "SKILL.md").read_text(encoding="utf-8") for p in skill_dirs()}
    names = set(skills)
    root_skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")

    check(len(skills) == 13, f"expected 13 skills, found {len(skills)}")

    # --- every skill is routable from the root ---------------------------
    for name in names:
        check(
            name in root_skill,
            f"root SKILL.md does not route to {name}; it will never be found via the router",
        )

    # --- cross-skill references point at skills that exist ---------------
    # Backticked lowercase-hyphen tokens that look like one of our skill names.
    token = re.compile(r"`([a-z][a-z0-9-]{6,})`")
    for name, text in skills.items():
        for ref in set(token.findall(text)):
            if ref == name or ref in names:
                continue
            # Ignore things that are plainly not skill names.
            if "." in ref or "/" in ref or ref.startswith("--"):
                continue
            looks_like_skill = ref.startswith(("page-", "trend-", "authority-", "employee-", "competitor-"))
            check(
                not looks_like_skill,
                f"{name}/SKILL.md names `{ref}`, which is not a skill in this bundle",
            )

    # --- reading skills carry the untrusted-content rule -----------------
    for name in READS_OUTSIDE_TEXT:
        check(name in names, f"{name} is listed as a reading skill but does not exist")
        text = skills.get(name, "")
        check(
            "untrusted-content.md" in text,
            f"{name} reads outside text but does not cite untrusted-content.md",
        )

    # --- the untrusted-content rule names the same skills ----------------
    untrusted = (ROOT / "references" / "untrusted-content.md").read_text(encoding="utf-8")
    for name in READS_OUTSIDE_TEXT:
        check(
            name in untrusted,
            f"untrusted-content.md does not name {name}, so its list has drifted from the skills",
        )

    # --- writing skills gate on the proof library ------------------------
    for name in PRODUCES_PUBLIC_COPY:
        check(name in names, f"{name} is listed as a writing skill but does not exist")
        check(
            "proof-library.md" in skills.get(name, ""),
            f"{name} produces public copy but does not cite proof-library.md",
        )

    # --- precedence is the single source of the resolution order ---------
    # Only precedence.md may enumerate the order; a second copy is how two
    # paths stop agreeing.
    order_phrase = "Reach heuristics last"
    holders = [
        p.relative_to(ROOT)
        for p in ROOT.rglob("*.md")
        if ".git" not in p.parts and order_phrase in p.read_text(encoding="utf-8")
    ]
    check(
        len(holders) <= 1,
        f"the precedence order is stated in more than one file: {holders}. "
        "Keep it in references/precedence.md and cite it.",
    )

    # --- the detector honesty claim is not contradicted anywhere ---------
    # Only an AFFIRMATIVE claim is a problem. The bundle states the negated
    # form ("does not beat AI detectors") on purpose and in several places, so
    # a bare substring search flags the honesty itself — which is how a
    # well-meaning check ends up training people to ignore the test.
    claim = re.compile(
        r"(?P<lead>.{0,60})(?P<hit>beats? ai detector|bypass(?:es|ing)? ai detect|undetectable)"
        r"(?P<trail>.{0,160})",
        re.I | re.S,
    )
    negations = ("not", "never", "no ", "cannot", "can't", "without", "nothing", "refus", "does not")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for match in claim.finditer(path.read_text(encoding="utf-8")):
            # The disclaimer is sometimes phrased as a question whose negation
            # lives in the answer ("Will this make posts undetectable? No."), so
            # look both sides of the hit rather than only behind it.
            context = (match.group("lead") + " " + match.group("trail")).lower()
            check(
                any(n in context for n in negations),
                f"{path.relative_to(ROOT)} appears to claim it defeats AI detectors "
                f"({match.group('hit').strip()!r}); the bundle explicitly does not make "
                "that claim",
            )

    # --- the two manual-only surfaces are stated as such -----------------
    surfaces = (ROOT / "references" / "page-surfaces.md").read_text(encoding="utf-8")
    for surface in ("Article", "Newsletter"):
        check(
            surface in surfaces,
            f"page-surfaces.md no longer documents the {surface} surface",
        )
    check(
        "no publishing API" in surfaces,
        "page-surfaces.md no longer states that articles and newsletters have no API",
    )

    for failure in failures:
        print(f"FAIL  {failure}")
    print(f"\n{checks - len(failures)}/{checks} integrity checks passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
