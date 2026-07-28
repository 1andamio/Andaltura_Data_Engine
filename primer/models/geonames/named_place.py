"""
Modelo INSPIRE NamedPlace.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from primer.models.common.geometry import Point
from primer.models.common.geographical_name import GeographicalName
from primer.models.common.identifier import Identifier


@dataclass(slots=True, frozen=True)
class NamedPlace:
    """
    Entidad INSPIRE NamedPlace.
    """

    identifier: Identifier
    name: GeographicalName
    geometry: Point

    local_type: str
    feature_type: str

    begin_lifespan_version: datetime

    @property
    def local_id(self) -> str:
        return self.identifier.local_id

    @property
    def namespace(self) -> str:
        return self.identifier.namespace

    @property
    def text(self) -> str:
        return self.name.text

    @property
    def x(self) -> float:
        return self.geometry.x

    @property
    def y(self) -> float:
        return self.geometry.y

    def __str__(self) -> str:
        return self.text