"""
Lector de entidades INSPIRE NamedPlace.
"""

from __future__ import annotations

from typing import Iterator

from primer.mappers.named_place_mapper import NamedPlaceMapper
from primer.models.geonames.named_place import NamedPlace
from primer.services.wfs.client import WFSClient
from primer.services.wfs.iterator import FeatureIterator
from primer.services.wfs.parser import WFSParser


class NamedPlaceReader:
    """
    Lector de entidades NamedPlace desde un servicio WFS.
    """

    def __init__(
        self,
        client: WFSClient,
        batch_size: int = 100,
    ) -> None:

        self.client = client
        self.batch_size = batch_size

    def read(self) -> Iterator[NamedPlace]:
        """
        Devuelve un iterador de objetos NamedPlace.
        """

        iterator = FeatureIterator(
            client=self.client,
            type_name="gn:NamedPlace",
            batch_size=self.batch_size,
        )

        parser = WFSParser()

        for response in iterator:

            for feature in parser.iter_features(response.text):

                yield NamedPlaceMapper.map(feature)