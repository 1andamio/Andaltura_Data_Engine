"""
Parser principal del SIMA.
"""

from __future__ import annotations

from bs4 import BeautifulSoup

from mdta.importers.sima.indicator_parser import IndicatorParser
from mdta.importers.sima.models import (
    MunicipalityData,
    Section,
)
from mdta.utils.text_normalizer import normalize_text


class SIMAParser:
    """
    Convierte el HTML del SIMA en un objeto MunicipalityData.
    """

    def parse(
        self,
        municipality_code: str,
        html: str,
    ) -> MunicipalityData:

        soup = BeautifulSoup(html, "lxml")

        raw_title = soup.title.get_text(" ", strip=True)

        print("\n=========== DEBUG PARSER ===========")
        print("TITLE repr :", repr(raw_title))
        print("TITLE bytes:", raw_title.encode("unicode_escape"))
        print("====================================")

        print("\n=========== DEBUG NORMALIZE ===========")

        print("RAW TITLE:")
        print(repr(raw_title))
        print(raw_title.encode("unicode_escape"))

        title = normalize_text(raw_title)

        print("\nNORMALIZED:")
        print(repr(title))
        print(title.encode("unicode_escape"))

        municipio = soup.select_one("h3.nomMuni")

        if municipio:
            nombre = municipio.get_text(" ", strip=True)

            print("\nH3 ORIGINAL:")
            print(repr(nombre))
            print(nombre.encode("unicode_escape"))

            nombre2 = normalize_text(nombre)

            print("\nH3 NORMALIZADO:")
            print(repr(nombre2))
            print(nombre2.encode("unicode_escape"))

        print("=======================================\n")

        municipality_name = (
            title.replace("SIMA - ", "")
            .split("(")[0]
            .strip()
        )

        municipality = MunicipalityData(
            code=municipality_code,
            name=municipality_name,
        )

        indicator_parser = IndicatorParser()

        tables = soup.find_all("table")

        for table in tables:

            previous = table.find_previous(
                ["h1", "h2", "h3", "h4", "strong", "b"]
            )

            if previous:
                section_name = normalize_text(
                    previous.get_text(" ", strip=True)
                )
            else:
                section_name = "Sin sección"

            section = Section(
                name=section_name,
            )

            rows = table.find_all("tr")

            for row in rows:

                cells = row.find_all(["th", "td"])

                if len(cells) < 2:
                    continue

                label = normalize_text(
                    cells[0].get_text(" ", strip=True)
                )

                value = normalize_text(
                    cells[1].get_text(" ", strip=True)
                )

                indicator = indicator_parser.parse(
                    section_name,
                    label,
                    value,
                )

                section.indicators.append(indicator)

            municipality.sections.append(section)

        return municipality