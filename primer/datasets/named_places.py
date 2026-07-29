"""
Dataset de entidades NamedPlace.
"""

from __future__ import annotations

from primer.datasets.base import BaseDataset
from primer.models.geonames.named_place import NamedPlace


class NamedPlaceDataset(BaseDataset[NamedPlace]):
    """
    Colección de entidades NamedPlace.
    """

    pass