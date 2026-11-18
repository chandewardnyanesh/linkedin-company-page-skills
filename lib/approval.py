"""Render the approval card a human reads before anything goes near a Page.

A Page speaks for a company, so the stakes of a bad publish are different from
a personal post: a wrong number in a page post is a claim the business made,
and it is screenshotted before it is deleted. The card exists so the reviewer
can see, in one screen, the three things that are expensive to get wrong -
which Page, which claims, and what happens the moment they say yes - without
scrolling back through the conversation to reconstruct them.

The card is also the only place the bundle promises to name its sources. Every
factual claim in a draft carries the proof-library entry it came from, so the
reviewer approves a claim they can check rather than a sentence they like.
"""
from __future__ import annotations

from .surfaces import SURFACES, fit

__all__ = ["render_approval_card"]

_RULE = "─" * 68


def _wrap_block(text: str) -> str:
    return (text or "").strip("\n")


def render_approval_card(
    *,
    kind: str,
    draft: str,
    page: str | None = None,
    surface: str = "page_post",
    target_url: str | None = None,
    claims: list[dict[str, str]] | None = None,
    format_choice: str | None = None,
    amplification: list[str] | None = None,
    publish_window: str | None = None,
    on_approval: str | None = None,
    warnings: list[str] | None = None,
    extras: dict[str, str] | None = None,
) -> str:
    """Build the card as plain text.

    `claims` is a list of `{"claim": ..., "source": ...}`. A draft that states a
    figure with no entry here is the thing the reviewer most needs to notice,
    so an empty claims list against a draft full of numbers is reported as a
    warning rather than quietly omitted.
    """
    spec = SURFACES.get(surface)
    verdict = fit(draft, surface) if spec else None

    lines: list[str] = [_RULE, f"APPROVAL REQUIRED — {kind}", _RULE]

    meta: list[tuple[str, str]] = []
    if page:
        meta.append(("Page", page))
    if spec:
        meta.append(("Surface", spec.name))
    if format_choice:
        meta.append(("Format", format_choice))
    if verdict:
        shape = f"{verdict['length']} chars"
        if verdict["limit"]:
            shape += f" / {verdict['limit']} limit"
        meta.append(("Length", shape))
    if publish_window:
        meta.append(("Suggested window", publish_window))
    if target_url:
        meta.append(("Target", target_url))
    for key, value in (extras or {}).items():
        meta.append((key, value))

    width = max((len(k) for k, _ in meta), default=0)
    for key, value in meta:
        lines.append(f"  {key.ljust(width)}  {value}")

    lines += ["", "DRAFT", _RULE, _wrap_block(draft), _RULE]

    if claims:
        lines += ["", "CLAIMS IN THIS DRAFT, AND WHERE EACH COMES FROM"]
        for entry in claims:
            claim = (entry.get("claim") or "").strip()
            source = (entry.get("source") or "").strip() or "NO SOURCE RECORDED"
            lines.append(f"  • {claim}")
            lines.append(f"      source: {source}")
    else:
        lines += [
            "",
            "CLAIMS IN THIS DRAFT, AND WHERE EACH COMES FROM",
            "  • none recorded — confirm the draft makes no factual claim about",
            "    results, customers, scale or price before approving.",
        ]

    if amplification:
        lines += ["", "AMPLIFICATION PLAN"]
        lines += [f"  • {item}" for item in amplification]

    collected = list(warnings or [])
    if verdict:
        collected = [*verdict["problems"], *verdict["notes"], *collected]
    if collected:
        lines += ["", "BEFORE YOU APPROVE"]
        lines += [f"  ! {item}" for item in collected]

    lines += [
        "",
        "ON APPROVAL",
        f"  {on_approval or 'Returned as a copy-paste block for you to publish.'}",
        "",
        "Reply 'approve' to proceed, or tell me what to change.",
        _RULE,
    ]
    return "\n".join(lines)
