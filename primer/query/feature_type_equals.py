"""
Predicado que filtra por tipo de entidad.
"""

from __future__ import annotations

from primer.models.geonames.named_place import NamedPlace
from primer.query.predicate import Predicate


class FeatureTypeEquals(Predicate[NamedPlace]):
    """
    Comprueba si una entidad pertenece a un determinado tipo.
    """

    def __init__(self, feature_type: str) -> None:
        self.feature_type = feature_type

    def __call__(self, item: NamedPlace) -> bool:
        return item.feature_type == self.feature_type