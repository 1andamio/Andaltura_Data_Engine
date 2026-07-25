from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass(slots=True)
class Denomination:
    """
    Denominación de una entidad geográfica.
    """

    name: str

    language: Optional[str] = None

    name_class: Optional[str] = None

    status: Optional[str] = None

    version: Optional[str] = None

    pronunciation: Optional[str] = None

    etymology: Optional[str] = None


@dataclass(slots=True)
class Location:
    """
    Localización de una entidad.
    """

    province: Optional[str] = None

    municipality: Optional[str] = None

    municipality_code: Optional[str] = None

    map_series: Optional[str] = None

    map_sheet: Optional[str] = None

    x: Optional[float] = None

    y: Optional[float] = None


@dataclass(slots=True)
class NomenclatorEntity:
    """
    Entidad del Nomenclátor Geográfico de Andalucía.
    """

    id: str

    entity_type: Optional[str] = None

    source: str = "Nomenclátor Geográfico de Andalucía"

    denominations: list[Denomination] = field(default_factory=list)

    locations: list[Location] = field(default_factory=list)