"""
Modelos de datos para el importador del SIMA.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Indicator:
    """
    Representa un indicador individual del SIMA.
    """

    section: str
    name: str
    value: object
    year: str | None = None
    unit: str | None = None


@dataclass(slots=True)
class Section:
    """
    Agrupa indicadores pertenecientes a una misma sección.
    """

    name: str
    indicators: list[Indicator] = field(default_factory=list)


@dataclass(slots=True)
class MunicipalityData:
    """
    Información completa de un municipio.
    """

    code: str
    name: str
    sections: list[Section] = field(default_factory=list)