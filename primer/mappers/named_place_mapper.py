"""
Conversión de una entidad XML INSPIRE NamedPlace a un objeto NamedPlace.
"""

from __future__ import annotations

from datetime import datetime
from xml.etree import ElementTree as ET

from primer.models.common.geometry import Point
from primer.models.common.geographical_name import GeographicalName
from primer.models.common.identifier import Identifier
from primer.models.geonames.named_place import NamedPlace


NAMESPACES = {
    "gn": "urn:x-inspire:specification:gmlas:GeographicalNames:3.0",
    "base": "urn:x-inspire:specification:gmlas:BaseTypes:3.2",
    "gml": "http://www.opengis.net/gml/3.2",
    "gmd": "http://www.isotc211.org/2005/gmd",
}


class NamedPlaceMapper:
    """
    Convierte un elemento XML <gn:NamedPlace> en un objeto NamedPlace.
    """

    @staticmethod
    def map(feature: ET.Element) -> NamedPlace:
        """
        Convierte una entidad XML en un objeto NamedPlace.
        """

        def text(path: str, required: bool = True) -> str:
            element = feature.find(path, NAMESPACES)

            if element is None or element.text is None:
                if required:
                    raise ValueError(
                        f"No se encontró el elemento XML requerido: {path}"
                    )
                return ""

            return element.text.strip()

        identifier = Identifier(
            namespace=text(".//base:namespace"),
            local_id=text(".//base:localId"),
        )

        name = GeographicalName(
            text=text(".//gn:text"),
            language=text(".//gn:language"),
            nativeness=text(".//gn:nativeness"),
            name_status=text(".//gn:nameStatus"),
            source=text(".//gn:sourceOfName"),
            script=text(".//gn:script"),
        )

        geometry = Point.from_pos(
            text(".//gml:pos")
        )

        return NamedPlace(
            identifier=identifier,
            name=name,
            geometry=geometry,
            local_type=text(".//gmd:LocalisedCharacterString"),
            feature_type=text(".//gn:type"),
            begin_lifespan_version=datetime.fromisoformat(
                text(".//gn:beginLifespanVersion").replace("Z", "+00:00")
            ),
        )