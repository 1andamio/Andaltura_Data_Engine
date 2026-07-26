"""
Descubre las entidades presentes en un Model.
"""

from __future__ import annotations

from dataclasses import dataclass

from primer.core.model import Model
from primer.discoverers.base import Discoverer


@dataclass(slots=True)
class Entity:
    """
    Representa una entidad descubierta.
    """

    name: str
    namespace: str | None
    occurrences: int


class EntityDiscoverer(Discoverer):
    """
    Descubre entidades presentes dentro de un modelo.
    """

    def discover(self, model: Model) -> list[Entity]:

        entities: list[Entity] = []

        for node in model.walk():

            entities.append(
                Entity(
                    name=node.name,
                    namespace=node.namespace,
                    occurrences=node.occurrences,
                )
            )

        entities.sort(key=lambda entity: entity.name)

        return entities