"""Environment loading and stdio hygiene.

Kept deliberately dependency-free. A user on the draft-only tier should be
able to `import lib` with nothing installed beyond the standard library,
because the default path through this bundle never makes a network call.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

# Variables that are honoured ONLY from the real shell environment, never from
# a .env file on disk. The custom poster executes a command, so letting an
# unrelated project's .env choose that command would be a code-execution hole.
SHELL_ONLY = frozenset({"LINKEDIN_PAGE_CUSTOM_POSTER"})

_LOADED = False


def repo_root() -> Path:
    """The bundle root (the directory holding lib/, references/, skills/)."""
    return Path(__file__).resolve().parent.parent


def load_env(path: str | os.PathLike[str] | None = None) -> dict[str, str]:
    """Load `.env` from the bundle root into os.environ without overwriting.

    Returns the keys it set, so a caller can report what came from disk.
    Values already present in the environment always win: an explicit export
    should beat a stale file. Keys in SHELL_ONLY are skipped entirely.
    """
    global _LOADED
    target = Path(path) if path else repo_root() / ".env"
    applied: dict[str, str] = {}
    if not target.is_file():
        _LOADED = True
        return applied

    for raw in target.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip("'\"")
        if not key or key in SHELL_ONLY or key in os.environ:
            continue
        os.environ[key] = value
        applied[key] = value

    _LOADED = True
    return applied


def utf8_stdio() -> None:
    """Make stdout/stderr UTF-8 tolerant.

    Approval cards carry box-drawing characters and the occasional emoji. On a
    Windows console the default code page raises UnicodeEncodeError mid-print,
    which looks like the skill crashed when it merely could not draw a border.
    """
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):  # pragma: no cover - platform dependent
                pass
