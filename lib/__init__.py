"""Shared helpers for LinkedIn Page Skills.

The public surface is small by design. This bundle's default path makes no
network call and needs nothing installed beyond the standard library, so
`import lib` works on a clean machine and the draft-only tier is a first-class
way to work rather than a fallback.

    from lib import fit, render_approval_card, publish, parse_page_url
"""
from ._env import load_env, repo_root, utf8_stdio
from .approval import render_approval_card
from .backend_selector import (
    active_backend,
    api_reachable,
    backend_report,
    manual_instructions,
    publish,
)
from .surfaces import DOCUMENT_SPEC, LIMITS, SOURCE, SURFACES, Surface, fit, fold_preview
from .url_parser import ParseError, organization_urn, parse_page_url

load_env()
utf8_stdio()

__all__ = [
    "load_env",
    "repo_root",
    "utf8_stdio",
    "render_approval_card",
    "active_backend",
    "api_reachable",
    "backend_report",
    "manual_instructions",
    "publish",
    "DOCUMENT_SPEC",
    "LIMITS",
    "SOURCE",
    "SURFACES",
    "Surface",
    "fit",
    "fold_preview",
    "ParseError",
    "organization_urn",
    "parse_page_url",
]
