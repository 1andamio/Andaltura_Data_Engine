"""
Parser principal del SIMA.
"""

from __future__ import annotations

from bs4 import BeautifulSoup

from mdta.importers.sima.indicator_parser import IndicatorParser
from mdta.importers.sima.models import MunicipalityData
from mdta.importers.sima.nuclei import SIMANucleiParser
from mdta.utils.text_normalizer import normalize_text


class SIMAParser:
    """
    Convierte los documentos del SIMA en un objeto MunicipalityData.

    Cada tipo de información (indicadores, núcleos, etc.) se obtiene de un
    documento independiente y es procesado por su parser especializado.
    """

    def __init__(self) -> None:

        self._indicator_parser = IndicatorParser()
        self._nuclei_parser = SIMANucleiParser()

    # ------------------------------------------------------------------

    def parse(
        self,
        municipality_code: str,
        municipality_html: str,
        nuclei_html: str | None = None,
    ) -> MunicipalityData:
        """
        Procesa los documentos de un municipio del SIMA.

        Parameters
        ----------
        municipality_code
            Código INE del municipio.

        municipality_html
            HTML de la ficha municipal.

        nuclei_html
            HTML de la página de núcleos de población.
            Es opcional porque no todas las pruebas necesitan cargarla.

        Returns
        -------
        MunicipalityData
        """

        soup = BeautifulSoup(
            municipality_html,
            "lxml",
        )

        municipality = MunicipalityData(
            code=municipality_code,
            name=self._get_municipality_name(soup),
        )

        # ----------------------------------------------------------
        # Indicadores
        # ----------------------------------------------------------

        municipality.sections.extend(
            self._indicator_parser.parse(soup)
        )

        # ----------------------------------------------------------
        # Núcleos de población
        # ----------------------------------------------------------

        if nuclei_html is not None:

            municipality.population_entities.extend(
                self._nuclei_parser.parse(nuclei_html)
            )

        return municipality

    # ------------------------------------------------------------------

    def _get_municipality_name(
        self,
        soup: BeautifulSoup,
    ) -> str:
        """
        Extrae el nombre del municipio desde el título de la ficha.
        """

        title = soup.title

        if title is None:
            return ""

        text = normalize_text(
            title.get_text(" ", strip=True)
        )

        text = text.replace("SIMA - ", "")

        return text.split("(")[0].strip()