"""
Parser de indicadores del SIMA.
"""

from __future__ import annotations

import re

from bs4 import BeautifulSoup
from bs4.element import Tag

from mdta.importers.sima.models import (
    Indicator,
    Section,
)
from mdta.importers.sima.normalizer import ValueNormalizer
from mdta.utils.text_normalizer import normalize_text


YEAR_PATTERN = re.compile(
    r"\.\s*(\d{4}(?:-\d{4})?)$"
)

UNIT_PATTERN = re.compile(
    r"\(([^()]*)\)"
)


class IndicatorParser:
    """
    Extrae todos los indicadores de una ficha SIMA.
    """

    def __init__(self) -> None:

        self.normalizer = ValueNormalizer()

    # -------------------------------------------------------------

    def parse(
        self,
        soup: BeautifulSoup,
    ) -> list[Section]:
        """
        Devuelve todas las secciones encontradas en la ficha.
        """

        sections: list[Section] = []

        for table in soup.find_all("table"):

            section = self._parse_table(table)

            if section.indicators:
                sections.append(section)

        return sections

    # -------------------------------------------------------------

    def _parse_table(
        self,
        table: Tag,
    ) -> Section:
        """
        Convierte una tabla HTML en una sección.
        """

        heading = table.find_previous(
            ["h1", "h2", "h3", "h4", "strong", "b"]
        )

        if heading:
            section_name = normalize_text(
                heading.get_text(" ", strip=True)
            )
        else:
            section_name = "Sin sección"

        section = Section(name=section_name)

        for row in table.find_all("tr"):

            indicator = self._parse_row(
                row,
                section_name,
            )

            if indicator is not None:
                section.add_indicator(indicator)

        return section

    # -------------------------------------------------------------

    def _parse_row(
        self,
        row: Tag,
        section: str,
    ) -> Indicator | None:
        """
        Convierte una fila en un indicador.
        """

        cells = row.find_all(["th", "td"])

        if len(cells) < 2:
            return None

        label = normalize_text(
            cells[0].get_text(" ", strip=True)
        )

        value = normalize_text(
            cells[1].get_text(" ", strip=True)
        )

        return self._build_indicator(
            section,
            label,
            value,
        )

    # -------------------------------------------------------------

    def _build_indicator(
        self,
        section: str,
        label: str,
        value: str,
    ) -> Indicator:
        """
        Construye un indicador.
        """

        year = None
        unit = None

        match = YEAR_PATTERN.search(label)

        if match:

            year = match.group(1)

            label = label[:match.start()].strip()

        match = UNIT_PATTERN.search(label)

        if match:

            unit = match.group(1)

            label = (
                label[:match.start()]
                + label[match.end():]
            ).strip()

        value = self.normalizer.normalize(value)

        return Indicator(
            section=section,
            name=label,
            value=value,
            year=year,
            unit=unit,
        )