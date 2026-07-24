"""
Parser de la estructura de población del SIMA.

Este parser interpreta la tabla completa de población del municipio y
genera entidades homogéneas para:

- Total municipal
- Población en núcleos
- Núcleos de población
- Población diseminada
"""

from __future__ import annotations

import re

from bs4 import BeautifulSoup
from bs4.element import Tag

from .models import (
    PopulationEntity,
    PopulationEntityType,
)


class SIMAPopulationParser:
    """
    Parser de la estructura de población del SIMA.
    """

    # ------------------------------------------------------------------

    def parse(
        self,
        municipality_code: str,
        municipality_name: str,
        html: str,
    ) -> list[PopulationEntity]:
        """
        Procesa la tabla completa de población.
        """

        soup = BeautifulSoup(html, "lxml")

        table = self._find_table(soup)

        entities: list[PopulationEntity] = []

        tbody = table.find("tbody")

        if tbody is None:
            return entities

        for row in tbody.find_all("tr", recursive=False):

            entity = self._parse_row(
                municipality_code,
                municipality_name,
                row,
            )

            if entity is not None:
                entities.append(entity)

        return entities

    # ------------------------------------------------------------------

    def _find_table(
        self,
        soup: BeautifulSoup,
    ) -> Tag:

        container = soup.find(
            "div",
            id="nucleos_tabla",
        )

        if container is None:
            raise RuntimeError(
                "No se encontró el contenedor de población."
            )

        table = container.find("table")

        if table is None:
            raise RuntimeError(
                "No se encontró la tabla de población."
            )

        return table

    # ------------------------------------------------------------------

    def _parse_row(
        self,
        municipality_code: str,
        municipality_name: str,
        row: Tag,
    ) -> PopulationEntity | None:

        first_cell = row.find("td")

        if first_cell is None:
            return None

        cells = row.find_all("td")

        if len(cells) < 4:
            return None

        name = self._extract_name(first_cell)

        entity_type = self._classify_row(
            municipality_name,
            first_cell,
            name,
        )

        if entity_type is None:
            return None

        official_code = municipality_code

        if entity_type == PopulationEntityType.NUCLEUS:

            link = first_cell.find("a")

            if link is None:
                return None

            official_code = self._extract_code(
                link.get("onclick", "")
            )

        return PopulationEntity(
            official_code=official_code,
            parent_code=municipality_code,
            name=name,
            entity_type=entity_type,
            population_total=self._to_int(cells[1].get_text()),
            population_male=self._to_int(cells[2].get_text()),
            population_female=self._to_int(cells[3].get_text()),
            source="SIMA",
            is_main_entity=(
                entity_type
                == PopulationEntityType.MUNICIPALITY_TOTAL
            ),
        )

    # ------------------------------------------------------------------

    def _classify_row(
        self,
        municipality_name: str,
        first_cell: Tag,
        name: str,
    ) -> PopulationEntityType | None:

        classes = first_cell.get("class", [])

        if "indentado" in classes:
            return PopulationEntityType.NUCLEUS

        normalized = name.casefold()

        if normalized == municipality_name.casefold():
            return PopulationEntityType.MUNICIPALITY_TOTAL

        if "población en núcleos" in normalized:
            return PopulationEntityType.NUCLEI_TOTAL

        if "población en diseminados" in normalized:
            return PopulationEntityType.DISSEMINATED

        return None

    # ------------------------------------------------------------------

    def _extract_name(
        self,
        cell: Tag,
    ) -> str:

        link = cell.find("a")

        if link is not None:
            return self._clean_text(link.get_text())

        return self._clean_text(cell.get_text())

    # ------------------------------------------------------------------

    @staticmethod
    def _extract_code(
        onclick: str,
    ) -> str:

        match = re.search(
            r'"(\d{11})"',
            onclick,
        )

        if match:
            return match.group(1)

        return ""

    # ------------------------------------------------------------------

    @staticmethod
    def _clean_text(
        text: str,
    ) -> str:

        return " ".join(text.split())

    # ------------------------------------------------------------------

    @staticmethod
    def _to_int(
        value: str,
    ) -> int:

        value = value.strip()

        if value in ("", "-"):
            return 0

        value = value.replace(".", "")
        value = value.replace(",", ".")

        try:
            return int(float(value))
        except ValueError:
            return 0