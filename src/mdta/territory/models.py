"""
Modelos territoriales básicos del MDTA.

Estas entidades representan el territorio de Andalucía y son
independientes de cualquier fuente de datos (SIMA, IECA, IGN, etc.).
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Province:
    """
    Provincia de Andalucía.
    """

    code: str
    name: str


@dataclass(slots=True, frozen=True)
class Comarca:
    """
    Comarca de Andalucía.
    """

    code: str
    name: str
    province_code: str


@dataclass(slots=True, frozen=True)
class Municipality:
    """
    Municipio de Andalucía.

    Representa únicamente la entidad territorial.
    No contiene indicadores estadísticos ni información
    procedente de fuentes externas.
    """

    code: str
    name: str
    province_code: str

    comarca_code: str | None = None

    ine_code: str | None = None

    ine_name: str | None = None