"""
Parser genérico para respuestas WFS/GML.
"""

from __future__ import annotations

from collections.abc import Iterator
from xml.etree import ElementTree as ET


class WFSParser:
    """
    Parser genérico para FeatureCollection.
    """

    NS = {
        "wfs": "http://www.opengis.net/wfs/2.0",
    }

    def parse(self, xml: str | bytes) -> ET.Element:

        if isinstance(xml, bytes):
            xml = xml.decode("utf-8")

        return ET.fromstring(xml)

    def iter_features(self, xml: str | bytes) -> Iterator[ET.Element]:

        root = self.parse(xml)

        for member in root.findall(".//wfs:member", self.NS):

            if len(member):

                yield member[0]

    def count_features(self, xml: str | bytes) -> int:

        return sum(1 for _ in self.iter_features(xml))