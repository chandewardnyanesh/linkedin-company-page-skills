"""Where an approved draft goes.

This bundle ships draft-first on purpose, and that is not a missing feature on
most surfaces - it is the platform. Page *posts* and *comments* can be
published by an API given the `w_organization_social` scope and an admin role.
Articles and newsletters cannot: LinkedIn exposes no publishing API for either,
so every tool that claims to automate a LinkedIn article is either driving a
browser or wrong. Document posts need a file upload through the composer.

So the honest split is:

  * **Surfaces an API could reach** - page post, comment. The bundle returns a
    paste block by default and hands off to a custom poster if one is wired up.
  * **Surfaces nothing can reach** - article, newsletter, poll, event, and the
    Page's own fields (tagline, About, tabs). These are manual for everyone.
    Saying "paste this" here is the complete and correct answer, and a skill
    should not apologise for it or imply a key would fix it.

Extending this is deliberately a shell-level act. Export
`LINKEDIN_PAGE_CUSTOM_POSTER` in a trusted shell before starting the agent and
approved drafts for API-reachable surfaces are piped to that command as JSON on
stdin. The variable is ignored when it appears in a `.env` file (see
`lib._env.SHELL_ONLY`), because a file on disk choosing which executable runs
is a code-execution hole dressed as configuration.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess

__all__ = [
    "active_backend",
    "api_reachable",
    "manual_instructions",
    "publish",
    "backend_report",
]

# Surfaces a publishing API could serve, given scope and an admin role.
_API_REACHABLE = frozenset({"page_post", "comment", "document_post"})

_MANUAL_STEPS: dict[str, str] = {
    "page_post": (
        "Open the Page in admin view, click Start a post, paste the body, then "
        "publish or use LinkedIn's own scheduler (the clock icon)."
    ),
    "document_post": (
        "Start a post on the Page, choose Add a document, upload the PDF, give "
        "it a document title (it shows as the carousel's label), paste the "
        "caption, publish. Keep any link in the caption: a link inside the PDF "
        "is not tappable."
    ),
    "article": (
        "From the Page's Super or Content admin view, click Write article, "
        "paste the headline and body, add the cover image, publish. There is "
        "no API for Page articles, so this step is manual for everyone."
    ),
    "newsletter": (
        "Start an article as the Page, then Manage -> Create newsletter (first "
        "issue only), fill in the newsletter details, then paste and publish "
        "the issue. Newsletters are an extension of articles and have no API "
        "either. Eligibility: Super Admin, at least 150 followers, and a "
        "recent history of original content on the Page."
    ),
    "poll": (
        "Start a post on the Page, choose Create a poll, paste the question and "
        "options, set the duration, publish."
    ),
    "event": (
        "Page admin view -> Events -> Create an event, paste the details, "
        "publish, then post the event to the feed separately."
    ),
    "comment": (
        "Open the target post while signed in as the Page (switch identity in "
        "the comment box), paste the comment, post."
    ),
    "page_fields": (
        "Page admin view -> Edit page. Paste each field into its box and save. "
        "Tagline, About, specialties, custom button and the tabs all live here."
    ),
}


def active_backend() -> str:
    """`custom` when a poster command is exported and runnable, else `manual`."""
    command = os.environ.get("LINKEDIN_PAGE_CUSTOM_POSTER", "").strip()
    if not command:
        return "manual"
    head = command.split()[0]
    if shutil.which(head) or os.path.isfile(head):
        return "custom"
    return "manual"


def api_reachable(surface: str) -> bool:
    """Could any API publish this surface, regardless of what is configured?"""
    return surface in _API_REACHABLE


def manual_instructions(surface: str) -> str:
    return _MANUAL_STEPS.get(
        surface,
        "Paste the block below into the matching field in the Page's admin view.",
    )


def backend_report() -> dict[str, object]:
    """What a skill can honestly tell the user about publishing right now."""
    backend = active_backend()
    return {
        "backend": backend,
        "custom_poster_configured": backend == "custom",
        "api_reachable_surfaces": sorted(_API_REACHABLE),
        "always_manual_surfaces": sorted(set(_MANUAL_STEPS) - _API_REACHABLE),
    }


def publish(
    *,
    kind: str,
    draft_text: str,
    surface: str = "page_post",
    page: str | None = None,
    target_url: str | None = None,
    attachments: list[str] | None = None,
    scheduled_time: str | None = None,
) -> dict[str, object]:
    """Hand off an **already-approved** draft. Never call this before approval.

    Returns a record describing what happened and what the user still has to
    do. On the manual path nothing leaves the machine, which is why the default
    path of this bundle makes no network call at all.
    """
    payload = {
        "kind": kind,
        "surface": surface,
        "page": page,
        "target_url": target_url,
        "text": draft_text,
        "attachments": attachments or [],
        "scheduled_time": scheduled_time,
    }

    backend = active_backend()
    if backend == "custom" and api_reachable(surface):
        command = os.environ["LINKEDIN_PAGE_CUSTOM_POSTER"].strip()
        try:
            completed = subprocess.run(  # noqa: S603 - operator-supplied by design
                command,
                shell=True,
                input=json.dumps(payload),
                text=True,
                capture_output=True,
                timeout=120,
                check=False,
            )
        except subprocess.TimeoutExpired:
            return {
                "mode": "custom",
                "ok": False,
                "error": "The custom poster did not return within 120 seconds.",
                "paste_block": draft_text,
                "next_step": manual_instructions(surface),
            }
        ok = completed.returncode == 0
        return {
            "mode": "custom",
            "ok": ok,
            "stdout": completed.stdout.strip(),
            "stderr": completed.stderr.strip(),
            "error": None if ok else f"Poster exited {completed.returncode}.",
            "paste_block": None if ok else draft_text,
            "next_step": None if ok else manual_instructions(surface),
        }

    record: dict[str, object] = {
        "mode": "manual",
        "ok": True,
        "paste_block": draft_text,
        "attachments": attachments or [],
        "next_step": manual_instructions(surface),
        "api_reachable": api_reachable(surface),
    }
    if not api_reachable(surface):
        record["why_manual"] = (
            f"LinkedIn exposes no publishing API for {surface.replace('_', ' ')}. "
            "This is the platform, not a gap in setup, so no key or connector "
            "changes it."
        )
    elif backend == "manual":
        record["why_manual"] = (
            "No publishing backend is wired up. This surface could be "
            "automated by exporting LINKEDIN_PAGE_CUSTOM_POSTER in your shell; "
            "pasting is a supported way to work, not a degraded one."
        )
    return record
