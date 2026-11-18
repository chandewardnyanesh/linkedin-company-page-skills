"""Parse LinkedIn Page URLs into the identifiers the API and the UI use.

A company page is addressed three different ways depending on where you found
it, and the three are not interchangeable:

  * **vanity slug** - `linkedin.com/company/cybercore-digital/`. What a human
    copies out of the address bar. Stable-ish, but the owner can change it.
  * **numeric id** - `linkedin.com/company/107107343/`. What admin URLs and
    Campaign Manager use.
  * **organization URN** - `urn:li:organization:107107343`. What any publishing
    API wants as the post author.

Only the numeric id converts cleanly into the URN. A slug does not, so this
module says so rather than guessing: a fabricated URN posts to the wrong page
or to nothing at all, and both failures are silent until someone checks the
feed. `organization_urn` is therefore `None` for a slug-only URL, and callers
are expected to ask the user for the numeric id (Page admin view -> the URL
bar) instead of inventing one.
"""
from __future__ import annotations

import re
from urllib.parse import parse_qs, unquote, urlparse

__all__ = ["parse_page_url", "organization_urn", "ParseError"]


class ParseError(ValueError):
    """The URL is not a LinkedIn surface this bundle knows how to address."""


_ACTIVITY = re.compile(r"(?:activity|share|ugcPost)[:\-](\d{6,})", re.I)
_URN = re.compile(r"urn:li:(organization|organizationBrand|company):(\d+)", re.I)
_NUMERIC = re.compile(r"^\d+$")
_COMMENT_URN = re.compile(
    r"urn:li:comment:\((?:activity|share|ugcPost):(\d+),(\d+)\)", re.I
)
_TRAILING_ID = re.compile(r"-(\d{6,})/?$")


def _urn_kind(fragment: str) -> str:
    low = fragment.lower()
    if "ugcpost" in low:
        return "ugcPost"
    if "share" in low:
        return "share"
    return "activity"


def parse_page_url(url: str) -> dict[str, object]:
    """Return every identifier that can be read out of `url`.

    Keys always present: `surface`, `url`. The rest appear when the URL
    actually carries them, and are `None` otherwise, so a caller can test for
    what it needs without catching KeyError.

    `surface` is one of: page, page-admin, page-post, feed-post, comment,
    newsletter, article, event, job, showcase, unknown.
    """
    if not url or not isinstance(url, str):
        raise ParseError("No URL given.")

    raw = url.strip()
    if raw.startswith("urn:li:"):
        m = _URN.search(raw)
        if m:
            return {
                "surface": "page",
                "url": raw,
                "page_slug": None,
                "page_id": m.group(2),
                "organization_urn": f"urn:li:organization:{m.group(2)}",
                "post_urn": None,
                "comment_id": None,
            }
        m = _COMMENT_URN.search(raw)
        if m:
            return {
                "surface": "comment",
                "url": raw,
                "page_slug": None,
                "page_id": None,
                "organization_urn": None,
                "post_urn": f"urn:li:activity:{m.group(1)}",
                "comment_id": m.group(2),
            }
        raise ParseError(f"Unrecognised URN: {raw!r}")

    if "://" not in raw:
        raw = "https://" + raw.lstrip("/")

    parsed = urlparse(raw)
    if "linkedin.com" not in (parsed.netloc or "").lower():
        raise ParseError(f"Not a linkedin.com URL: {url!r}")

    segments = [s for s in (parsed.path or "").split("/") if s]
    query = parse_qs(parsed.query or "")

    out: dict[str, object] = {
        "surface": "unknown",
        "url": url.strip(),
        "page_slug": None,
        "page_id": None,
        "organization_urn": None,
        "post_urn": None,
        "comment_id": None,
    }

    # A comment URN rides in the query string and wins over the path, because a
    # comment URL is also a post URL and the caller asked about the comment.
    for key in ("commentUrn", "highlightedUpdateUrn", "replyUrn"):
        for value in query.get(key, []):
            m = _COMMENT_URN.search(unquote(value))
            if m:
                out["surface"] = "comment"
                out["post_urn"] = f"urn:li:activity:{m.group(1)}"
                out["comment_id"] = m.group(2)
                return out

    if not segments:
        raise ParseError(f"No path to read in {url!r}")

    head = segments[0].lower()

    if head in {"company", "school", "showcase"}:
        if len(segments) < 2:
            raise ParseError(f"No page identifier in {url!r}")
        ident = segments[1]
        if _NUMERIC.match(ident):
            out["page_id"] = ident
            out["organization_urn"] = f"urn:li:organization:{ident}"
        else:
            out["page_slug"] = ident
        tail = {s.lower() for s in segments[2:]}
        if head == "showcase":
            out["surface"] = "showcase"
        elif tail & {"admin", "admin_v2"}:
            out["surface"] = "page-admin"
        else:
            out["surface"] = "page"
        return out

    if head == "posts":
        # /posts/<slug>_<text>-activity-7448...-AbCd
        out["surface"] = "page-post"
        if len(segments) >= 2:
            tail = segments[1]
            out["page_slug"] = tail.split("_", 1)[0] or None
            m = _ACTIVITY.search(tail)
            if m:
                out["post_urn"] = f"urn:li:{_urn_kind(tail)}:{m.group(1)}"
        return out

    if head == "feed" and len(segments) >= 2 and segments[1].lower() == "update":
        out["surface"] = "feed-post"
        fragment = unquote("/".join(segments[2:]))
        m = _ACTIVITY.search(fragment)
        if m:
            out["post_urn"] = f"urn:li:{_urn_kind(fragment)}:{m.group(1)}"
        return out

    if head in {"newsletters", "pulse", "events", "jobs"}:
        out["surface"] = {
            "newsletters": "newsletter",
            "pulse": "article",
            "events": "event",
            "jobs": "job",
        }[head]
        tail = "/".join(segments[1:])
        m = _TRAILING_ID.search(tail) or re.search(r"(\d{6,})", tail)
        if m:
            out["page_id" if head == "events" else "post_urn"] = (
                m.group(1) if head == "events" else f"urn:li:activity:{m.group(1)}"
            )
        return out

    raise ParseError(
        f"Unsupported LinkedIn surface {parsed.path!r}. Known surfaces: "
        "company page, page admin, page post, feed post, comment, newsletter, "
        "article, event, job, showcase."
    )


def organization_urn(value: str) -> str:
    """Coerce a numeric page id or an existing URN into an organization URN.

    Raises on a vanity slug. Resolving a slug needs a LinkedIn call this bundle
    does not make, and a guessed URN is worse than an error: it publishes
    somewhere nobody is looking.
    """
    text = (value or "").strip()
    if not text:
        raise ParseError("No page identifier given.")
    m = _URN.search(text)
    if m:
        return f"urn:li:organization:{m.group(2)}"
    if _NUMERIC.match(text):
        return f"urn:li:organization:{text}"
    parsed = parse_page_url(text) if "linkedin.com" in text else {}
    if parsed.get("organization_urn"):
        return str(parsed["organization_urn"])
    raise ParseError(
        f"{text!r} is a vanity slug, not a numeric page id. Open the Page in "
        "admin view and read the number out of the URL, or ask the Page admin "
        "for it. Do not guess the id."
    )
