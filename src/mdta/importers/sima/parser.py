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

        title = soup.title.get_text(" ", strip=True)

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
                section_name = previous.get_text(
                    " ",
                    strip=True,
                )
            else:
                section_name = "Sin sección"

            section = Section(
                name=section_name,
            )

            rows = table.find_all("tr")

            for row in rows:

                cells = row.find_all(
                    ["th", "td"]
                )

                if len(cells) < 2:
                    continue

                label = cells[0].get_text(
                    " ",
                    strip=True,
                )

                value = cells[1].get_text(
                    " ",
                    strip=True,
                )

                indicator = indicator_parser.parse(
                    section_name,
                    label,
                    value,
                )

                section.indicators.append(
                    indicator
                )

            municipality.sections.append(
                section
            )

        return municipality