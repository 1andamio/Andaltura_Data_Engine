"""
Colección de entidades NamedPlace.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from collections.abc import Iterator

from primer.models.geonames.named_place import NamedPlace


@dataclass(slots=True)
class NamedPlaceDataset:
    """
    Colección de entidades NamedPlace.
    """

    items: list[NamedPlace] = field(default_factory=list)

    def add(self, place: NamedPlace) -> None:
        self.items.append(place)

    def extend(self, places: Iterator[NamedPlace]) -> None:
        self.items.extend(places)

    def __len__(self) -> int:
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def first(self) -> NamedPlace | None:
        if self.items:
            return self.items[0]
        return None