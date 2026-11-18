#!/usr/bin/env python3
"""One command that says whether the bundle is wired up correctly.

Runs the structural checks, exercises the library on known inputs, and reports
which publishing path is active. Everything here works offline, because the
default path of this bundle is offline.

    python -m scripts.selftest
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from lib import (  # noqa: E402
    DOCUMENT_SPEC,
    SURFACES,
    backend_report,
    fit,
    organization_urn,
    parse_page_url,
    render_approval_card,
)
from lib.url_parser import ParseError  # noqa: E402
from scripts import check_frontmatter, check_markdown_references, check_no_secrets  # noqa: E402

PASS, FAIL = "pass", "FAIL"
_results: list[tuple[str, str, str]] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    _results.append((PASS if condition else FAIL, label, detail))


def main() -> int:
    # --- library behaviour on inputs whose answers are known ---------------
    page = parse_page_url("https://www.linkedin.com/company/cybercore-digital/")
    check("page URL -> slug", page["page_slug"] == "cybercore-digital", str(page["page_slug"]))
    check(
        "slug carries no invented URN",
        page["organization_urn"] is None,
        "a slug cannot be converted to an organization URN without a lookup",
    )

    numeric = parse_page_url("https://www.linkedin.com/company/107107343/admin/")
    check("admin URL -> surface", numeric["surface"] == "page-admin", str(numeric["surface"]))
    check(
        "numeric id -> URN",
        numeric["organization_urn"] == "urn:li:organization:107107343",
        str(numeric["organization_urn"]),
    )

    post = parse_page_url(
        "https://www.linkedin.com/posts/cybercore-digital_ai-ops-activity-7448123456789012345-AbCd"
    )
    check("page post URL -> urn", post["post_urn"] == "urn:li:activity:7448123456789012345", str(post["post_urn"]))
    check("page post URL -> slug", post["page_slug"] == "cybercore-digital", str(post["page_slug"]))

    ugc = parse_page_url("https://www.linkedin.com/feed/update/urn:li:ugcPost:7447000000000000000/")
    check("ugcPost URL keeps its type", ugc["post_urn"] == "urn:li:ugcPost:7447000000000000000", str(ugc["post_urn"]))

    comment = parse_page_url(
        "https://www.linkedin.com/feed/update/urn:li:activity:7448000000000000000"
        "?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7448000000000000000%2C7449000000000000000%29"
    )
    check("comment URL -> comment id", comment["comment_id"] == "7449000000000000000", str(comment["comment_id"]))

    try:
        organization_urn("cybercore-digital")
        check("slug -> URN refuses to guess", False, "it returned a URN for a slug")
    except ParseError:
        check("slug -> URN refuses to guess", True)

    # --- surface limits ----------------------------------------------------
    over = fit("x" * 2100, "about")
    check("About over 2,000 fails", not over["ok"], str(over["problems"][:1]))
    tagline = fit("x" * 119, "tagline")
    check("tagline at 119 passes", tagline["ok"])
    hook = fit("A" * 400, "page_post")
    check(
        "long hook flagged behind the fold",
        any("see more" in n for n in hook["notes"]),
        str(hook["notes"]),
    )
    check("every surface has a name", all(s.name for s in SURFACES.values()))
    check("document spec present", DOCUMENT_SPEC["max_pages"] == 300)

    card = render_approval_card(
        kind="Page post",
        draft="A short draft with no numbers in it.",
        page="CyberCore Digital",
        surface="page_post",
    )
    check("approval card names the Page", "CyberCore Digital" in card)
    check(
        "approval card warns on unsourced claims",
        "none recorded" in card,
        "a draft with no claim list must say so",
    )

    # --- structural checks -------------------------------------------------
    check("frontmatter", check_frontmatter.main() == 0, "see output above")
    check("markdown references resolve", check_markdown_references.main() == 0, "see output above")
    check("no secrets staged", check_no_secrets.main() == 0, "see output above")

    # --- report ------------------------------------------------------------
    print("\n" + "=" * 64)
    print("linkedin-company-page-skills selftest")
    print("=" * 64)
    for status, label, detail in _results:
        suffix = f"  — {detail}" if detail and status == FAIL else ""
        print(f"  [{status}] {label}{suffix}")

    report = backend_report()
    print("\npublishing")
    print(f"  backend: {report['backend']}")
    print(f"  API-reachable surfaces: {', '.join(report['api_reachable_surfaces'])}")
    print(f"  always manual (no LinkedIn API exists): {', '.join(report['always_manual_surfaces'])}")
    if report["backend"] == "manual":
        print(
            "\n  Draft-only is the default and is fully supported. Approved "
            "drafts come back as paste blocks."
        )

    failed = sum(1 for status, _, _ in _results if status == FAIL)
    print(f"\n{len(_results) - failed}/{len(_results)} checks passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
