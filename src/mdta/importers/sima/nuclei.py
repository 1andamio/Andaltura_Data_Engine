"""
Parser de los núcleos de población del SIMA.
"""

from __future__ import annotations

import re

from bs4 import BeautifulSoup
from bs4.element import Tag

from .models import PopulationEntity


class SIMANucleiParser:
    """
    Parser de la página de núcleos del SIMA.
    """

    # -------------------------------------------------------------

    def parse(self, html: str) -> list[PopulationEntity]:
        """
        Extrae todos los núcleos de población del municipio.

        Parameters
        ----------
        html
            HTML de la página de núcleos.

        Returns
        -------
        list[PopulationEntity]
        """

        soup = BeautifulSoup(html, "lxml")

        table = self._find_table(soup)

        entities: list[PopulationEntity] = []

        tbody = table.find("tbody")

        if tbody is None:
            return entities

        for row in tbody.find_all("tr", recursive=False):

            entity = self._parse_row(row)

            if entity is not None:
                entities.append(entity)

        return entities

    # -------------------------------------------------------------

    def _find_table(self, soup: BeautifulSoup) -> Tag:
        """
        Localiza la tabla de núcleos.
        """

        container = soup.find("div", id="nucleos_tabla")

        if container is None:
            raise RuntimeError(
                "No se encontró el contenedor de núcleos."
            )

        table = container.find("table")

        if table is None:
            raise RuntimeError(
                "No se encontró la tabla de núcleos."
            )

        return table

    # -------------------------------------------------------------

    def _parse_row(self, row: Tag) -> PopulationEntity | None:
        """
        Convierte una fila HTML en un PopulationEntity.
        """

        first_cell = row.find("td")

        if first_cell is None:
            return None

        # Solo interesan los núcleos reales
        if "indentado" not in first_cell.get("class", []):
            return None

        link = first_cell.find("a")

        if link is None:
            return None

        name = self._clean_text(link.get_text())

        onclick = link.get("onclick", "")

        official_code = self._extract_code(onclick)

        cells = row.find_all("td")

        if len(cells) < 4:
            return None

        total = self._to_int(cells[1].get_text())
        male = self._to_int(cells[2].get_text())
        female = self._to_int(cells[3].get_text())

        return PopulationEntity(
            official_code=official_code,
            name=name,
            entity_type="nucleus",
            population_total=total,
            population_male=male,
            population_female=female,
            year=None,
            is_main_entity=False,
            notes=None,
        )

    # -------------------------------------------------------------

    @staticmethod
    def _extract_code(onclick: str) -> str:
        """
        Extrae el código oficial del núcleo.
        """

        match = re.search(r'"(\d{11})"', onclick)

        if match:
            return match.group(1)

        return ""

    # -------------------------------------------------------------

    @staticmethod
    def _clean_text(text: str) -> str:
        """
        Limpia espacios repetidos.
        """

        return " ".join(text.split())

    # -------------------------------------------------------------

    @staticmethod
    def _to_int(value: str) -> int:
        """
        Convierte valores como:

            8.628
            1.245
            -
            ""

        en enteros.
        """

        value = value.strip()

        if value in ("", "-"):
            return 0

        value = value.replace(".", "")
        value = value.replace(",", ".")

        try:
            return int(float(value))
        except ValueError:
            return 0