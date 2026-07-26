"""
Parser GML para servicios WFS.

Este módulo transforma respuestas GML (INSPIRE/WFS) en estructuras
Python fáciles de consumir.

Actualmente implementa el parser para gn:NamedPlace.
"""

from __future__ import annotations

from xml.etree import ElementTree as ET


NS = {
    "wfs": "http://www.opengis.net/wfs/2.0",
    "gml": "http://www.opengis.net/gml/3.2",
    "gn": "urn:x-inspire:specification:gmlas:GeographicalNames:3.0",
    "base": "urn:x-inspire:specification:gmlas:BaseTypes:3.2",
}


class GMLParser:
    """
    Parser para respuestas GML de servicios WFS.
    """

    def parse_named_places(self, xml: str) -> list[dict]:
        """
        Convierte una respuesta GetFeature en una lista de entidades.

        Parameters
        ----------
        xml:
            Documento XML/GML.

        Returns
        -------
        list[dict]
        """

        root = ET.fromstring(xml)

        results: list[dict] = []

        for member in root.findall("wfs:member", NS):

            feature = member.find("gn:NamedPlace", NS)

            if feature is None:
                continue

            gml_id = feature.attrib.get(
                "{http://www.opengis.net/gml/3.2}id"
            )

            local_id = self._text(
                feature,
                "gn:inspireId/base:Identifier/base:localId",
            )

            namespace = self._text(
                feature,
                "gn:inspireId/base:Identifier/base:namespace",
            )

            name = self._text(
                feature,
                "gn:name/gn:GeographicalName/"
                "gn:spelling/gn:SpellingOfName/"
                "gn:text",
            )

            feature_type = self._text(
                feature,
                "gn:type",
            )

            pos = self._text(
                feature,
                "gn:geometry/gml:Point/gml:pos",
            )

            x = None
            y = None

            if pos:
                values = pos.split()

                if len(values) == 2:

                    try:
                        x = float(values[0])
                        y = float(values[1])

                    except ValueError:
                        pass

            results.append(
                {
                    "gml_id": gml_id,
                    "local_id": local_id,
                    "namespace": namespace,
                    "name": name,
                    "feature_type": feature_type,
                    "x": x,
                    "y": y,
                }
            )

        return results

    @staticmethod
    def _text(
        element: ET.Element,
        xpath: str,
    ) -> str | None:

        node = element.find(xpath, NS)

        if node is None:
            return None

        if node.text is None:
            return None

        return node.text.strip()