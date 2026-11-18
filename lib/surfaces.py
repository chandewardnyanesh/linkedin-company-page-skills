"""Hard limits for every LinkedIn Page surface, and a checker for a draft.

Why this is code rather than a line in a reference file: character counting by
eye is the single most reliable way to ship a broken page asset. A tagline that
runs to 134 characters is silently truncated, an About section written to the
personal 2,600-character limit loses its last paragraph on a Page, and a hook
that sits at 240 characters has its payoff hidden behind "...see more" on every
mobile feed it reaches. None of those failures look like failures in a draft.

Every number carries its source in `SOURCE`, so a reader can check it rather
than trust it, and so a stale limit is findable when LinkedIn moves one. These
are platform limits observed in 2026; LinkedIn changes them without notice.

Usage from a skill:

    from lib import fit
    verdict = fit(draft, "page_post")
    if not verdict["ok"]:
        ...                       # verdict["problems"] says what to cut

CLI equivalent, for when a skill would rather not hold the text in context:

    python -m scripts.fit --surface page_post --file draft.md
"""
from __future__ import annotations

from dataclasses import dataclass, field

__all__ = ["LIMITS", "SURFACES", "fit", "fold_preview", "Surface"]


@dataclass(frozen=True)
class Surface:
    """One writable surface on a LinkedIn Page."""

    name: str
    limit: int | None
    fold_desktop: int | None = None
    fold_mobile: int | None = None
    sweet_spot: tuple[int, int] | None = None
    unit: str = "characters"
    note: str = ""
    extras: dict[str, object] = field(default_factory=dict)


SOURCE = (
    "Character limits cross-checked across AuthoredUp, socialcal, unil.ink, "
    "viralbrain and link.boo 2026 limit tables (they agree on Page fields). "
    "Document-post specs from Oktopost 2026 carousel best practices and "
    "LinkedIn Help. Fold thresholds from the 210-character '...see more' "
    "reference tables. Where sources disagree the bundle takes the lower "
    "number, because the cost of being 20 characters short is nothing and the "
    "cost of being 20 over is a truncated sentence in public."
)

SURFACES: dict[str, Surface] = {
    "page_name": Surface("Page name", 100),
    "tagline": Surface(
        "Page tagline",
        120,
        note="Sits under the logo and is the one line that appears beside the "
        "Page in search and in the follow prompt. No fold: it either fits or "
        "it is cut.",
    ),
    "about": Surface(
        "Page About / description",
        2000,
        fold_desktop=300,
        note="A Page gets 2,000 characters, not the 2,600 a personal profile "
        "gets. Templates written for a personal About will overflow. The first "
        "~300 characters carry the whole pitch, because the rest sits behind "
        "the section's own 'see more'.",
    ),
    "page_post": Surface(
        "Page post",
        3000,
        fold_desktop=210,
        fold_mobile=140,
        sweet_spot=(900, 1300),
        note="Same 3,000-character cap as a personal post. The sweet spot is a "
        "default for when nobody has asked for a length, never a ceiling over "
        "an explicit request.",
    ),
    "comment": Surface("Comment (as the Page)", 1250, sweet_spot=(200, 400)),
    "article_title": Surface(
        "Article headline",
        100,
        note="Sources split between 100 and 150 here. The bundle uses 100 so a "
        "headline is never silently clipped.",
    ),
    "article_body": Surface(
        "Article body",
        110000,
        sweet_spot=(7000, 15000),
        note="Effectively unlimited. The sweet spot is roughly 1,200-2,500 "
        "words, which is where an authority piece is long enough to be the "
        "reference on its subject and short enough to be finished.",
    ),
    "newsletter_title": Surface("Newsletter title", 100),
    "poll_question": Surface("Poll question", 140),
    "job_description": Surface("Job posting description", 25000),
}

LIMITS: dict[str, int | None] = {key: s.limit for key, s in SURFACES.items()}

# Document posts (PDF carousels) are measured in pages and megabytes, not
# characters, so they live apart from the text surfaces.
DOCUMENT_SPEC: dict[str, object] = {
    "accepted_types": ["PDF", "PPTX", "DOC", "DOCX"],
    "max_file_size_mb": 100,
    "practical_file_size_mb": 10,
    "max_pages": 300,
    "sweet_spot_pages": (5, 12),
    "dropoff_after_pages": 20,
    "caption_words": (100, 200),
    "link_placement": "caption",
    "note": (
        "A link inside the PDF is not tappable, so it has to live in the "
        "caption. LinkedIn deprecated the native multi-image carousel creator, "
        "so a swipeable carousel in 2026 means a multi-page document post."
    ),
}


def _count(text: str) -> int:
    """Characters as LinkedIn counts them: spaces, newlines and emoji included."""
    return len(text or "")


def fold_preview(text: str, surface: str = "page_post") -> dict[str, object]:
    """What a reader sees before deciding whether to expand.

    Returns the above-fold slice for desktop and mobile plus whether the text
    is short enough that there is no fold at all. A hook that needs the reader
    to expand before it makes sense has already lost most of them.
    """
    spec = SURFACES.get(surface)
    if spec is None:
        raise KeyError(f"Unknown surface {surface!r}. Known: {sorted(SURFACES)}")
    body = text or ""
    out: dict[str, object] = {"surface": surface, "length": _count(body)}
    for label, threshold in (("desktop", spec.fold_desktop), ("mobile", spec.fold_mobile)):
        if threshold is None:
            continue
        out[label] = {
            "threshold": threshold,
            "visible": body[:threshold],
            "truncated": _count(body) > threshold,
        }
    return out


def fit(text: str, surface: str = "page_post", *, target: int | None = None) -> dict[str, object]:
    """Check a draft against one surface. Never rewrites; only reports.

    `target` lets a caller assert a requested length (a 1,800-character post
    the user asked for) so the sweet-spot advice does not override an explicit
    brief. Problems are hard failures; notes are advice.
    """
    spec = SURFACES.get(surface)
    if spec is None:
        raise KeyError(f"Unknown surface {surface!r}. Known: {sorted(SURFACES)}")

    length = _count(text)
    problems: list[str] = []
    notes: list[str] = []

    if spec.limit is not None and length > spec.limit:
        problems.append(
            f"{length} characters is {length - spec.limit} over the "
            f"{spec.limit}-character limit for {spec.name}. The overflow is "
            "dropped, not wrapped."
        )

    if target is not None:
        drift = length - target
        if abs(drift) > max(60, target * 0.15):
            notes.append(
                f"Asked for about {target} characters, came in at {length} "
                f"({drift:+d})."
            )
    elif spec.sweet_spot and spec.limit is not None:
        low, high = spec.sweet_spot
        if length < low:
            notes.append(
                f"{length} characters is under the {low}-{high} range this "
                "surface usually rewards. Short is fine if it is deliberate."
            )
        elif length > high:
            notes.append(
                f"{length} characters is above the {low}-{high} default range. "
                "Fine when the length was asked for or the substance needs it."
            )

    fold = fold_preview(text, surface) if (spec.fold_desktop or spec.fold_mobile) else None
    if fold:
        mobile = fold.get("mobile") or fold.get("desktop")
        if isinstance(mobile, dict) and mobile.get("truncated"):
            notes.append(
                f"Only the first {mobile['threshold']} characters show before "
                "'...see more'. Check the hook pays off inside that window."
            )

    return {
        "surface": surface,
        "surface_name": spec.name,
        "length": length,
        "limit": spec.limit,
        "remaining": None if spec.limit is None else spec.limit - length,
        "ok": not problems,
        "problems": problems,
        "notes": notes,
        "fold": fold,
    }
