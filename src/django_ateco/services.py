"""Thin Django-facing helpers over the pure-Python ``ateco`` library."""

from __future__ import annotations

from datetime import date
from typing import Any

import ateco


def lookup(
    code: str,
    *,
    edition: str | None = None,
    as_of: date | str | None = None,
) -> Any:
    """Lookup an ATECO node (default edition 2025)."""
    return ateco.lookup(code, edition=edition, as_of=as_of)


def validate(
    code: str,
    *,
    edition: str | None = None,
    as_of: date | str | None = None,
) -> bool:
    """Return True if ``code`` exists in the selected edition."""
    return ateco.validate(code, edition=edition, as_of=as_of)


def map_code(
    code: str,
    from_edition: str,
    to_edition: str,
    *,
    table: str = "theoretical",
) -> Any:
    """Map a code between editions (see ``ateco.map_code``)."""
    return ateco.map_code(
        code, from_edition, to_edition, table=table  # type: ignore[arg-type]
    )


def editions() -> list[Any]:
    return ateco.editions()
