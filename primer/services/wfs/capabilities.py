"""
Capabilities Analyzer para servicios WFS.

Analiza el documento GetCapabilities y devuelve un modelo
Python con la información relevante del servicio.
"""

from __future__ import annotations

from dataclasses import dataclass
from xml.etree import ElementTree as ET

import requests

from .client import WFSClient

NS = {
    "ows": "http://www.opengis.net/ows/1.1",
    "wfs": "http://www.opengis.net/wfs/2.0",
}


@dataclass(slots=True)
class WFSCapabilities:
    service_title: str
    service_abstract: str
    version: str
    provider: str

    supports_paging: bool
    supports_sorting: bool

    count_default: int | None

    feature_types: list[str]


class CapabilitiesAnalyzer:
    """
    Analiza un documento GetCapabilities.
    """

    def __init__(self, client: WFSClient) -> None:
        self.client = client

    def load(self) -> WFSCapabilities:
        """
        Descarga y analiza el documento GetCapabilities.
        """

        xml = self.client.get_capabilities()

        # Compatibilidad con cualquier implementación del cliente
        if isinstance(xml, requests.Response):
            xml = xml.text
        elif isinstance(xml, bytes):
            xml = xml.decode("utf-8")

        root = ET.fromstring(xml)

        service_title = root.findtext(
            ".//ows:Title",
            default="",
            namespaces=NS,
        )

        service_abstract = root.findtext(
            ".//ows:Abstract",
            default="",
            namespaces=NS,
        )

        provider = root.findtext(
            ".//ows:ProviderName",
            default="",
            namespaces=NS,
        )

        version = root.attrib.get("version", "")

        constraints: dict[str, str] = {}

        for constraint in root.findall(".//ows:Constraint", NS):

            name = constraint.attrib.get("name", "")

            value = (
                constraint.findtext(
                    "ows:DefaultValue",
                    default="",
                    namespaces=NS,
                )
                or constraint.findtext(
                    "ows:Value",
                    default="",
                    namespaces=NS,
                )
                or ""
            )

            constraints[name] = value

        supports_paging = (
            constraints.get("ImplementsResultPaging", "").upper() == "TRUE"
        )

        supports_sorting = (
            constraints.get("ImplementsSorting", "").upper() == "TRUE"
        )

        count_default = None

        value = constraints.get("CountDefault")

        if value:
            try:
                count_default = int(value)
            except ValueError:
                pass

        feature_types: list[str] = []

        for feature in root.findall(".//wfs:FeatureType", NS):

            name = feature.findtext(
                "wfs:Name",
                default="",
                namespaces=NS,
            )

            if name:
                feature_types.append(name)

        return WFSCapabilities(
            service_title=service_title,
            service_abstract=service_abstract,
            version=version,
            provider=provider,
            supports_paging=supports_paging,
            supports_sorting=supports_sorting,
            count_default=count_default,
            feature_types=feature_types,
        )