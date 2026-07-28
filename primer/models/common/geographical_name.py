"""
Modelo INSPIRE GeographicalName.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class GeographicalName:
    """
    Nombre geográfico INSPIRE.
    """

    text: str
    language: str
    nativeness: str
    name_status: str
    source: str
    script: str

    def __str__(self) -> str:
        return self.text