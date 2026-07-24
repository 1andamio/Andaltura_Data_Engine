"""
Descarga de páginas del Sistema de Información Multiterritorial de Andalucía (SIMA).
"""

from __future__ import annotations

import requests

from .config import (
    MUNICIPAL_URL,
    NUCLEI_URL,
    HEADERS,
    TIMEOUT,
)


class SIMADownloader:
    """
    Cliente HTTP para descargar fichas del SIMA.
    """

    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    def _download(self, url: str, params: dict) -> str:
        """
        Descarga una página del SIMA.

        Parameters
        ----------
        url
            URL base del servicio.
        params
            Parámetros GET.

        Returns
        -------
        str
            HTML descargado.

        Raises
        ------
        RuntimeError
            Si la descarga falla o la respuesta no parece una página HTML.
        """

        try:
            response = self.session.get(
                url,
                params=params,
                timeout=TIMEOUT,
            )

            response.raise_for_status()

        except requests.RequestException as exc:
            raise RuntimeError(
                f"Error descargando datos del SIMA ({url}) con parámetros {params}."
            ) from exc

        html = response.text

        if "<html" not in html.lower():
            raise RuntimeError(
                "La respuesta recibida no parece una página HTML válida del SIMA."
            )

        return html

    def get_municipality(self, municipality_code: str) -> str:
        """
        Descarga la ficha municipal del SIMA.

        Parameters
        ----------
        municipality_code
            Código INE del municipio.

        Returns
        -------
        str
            HTML de la ficha municipal.
        """

        municipality_code = str(municipality_code).zfill(5)

        return self._download(
            MUNICIPAL_URL,
            {"mun": municipality_code},
        )

    def get_nuclei(self, municipality_code: str) -> str:
        """
        Descarga la ficha de entidades de población del municipio.

        Parameters
        ----------
        municipality_code
            Código INE del municipio.

        Returns
        -------
        str
            HTML de la ficha de entidades de población.
        """

        municipality_code = str(municipality_code).zfill(5)

        return self._download(
            NUCLEI_URL,
            {"CodMuni": municipality_code},
        )