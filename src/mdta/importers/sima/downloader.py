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

    def get_municipality(self, municipality_code: str) -> str:
        """
        Descarga la ficha de un municipio.
        """

        response = self.session.get(
            MUNICIPAL_URL,
            params={"mun": municipality_code},
            timeout=TIMEOUT,
        )

        response.raise_for_status()

        # Fuerza la codificación correcta
        response.encoding = response.apparent_encoding

        return response.text

    def get_nuclei(self, municipality_code: str) -> str:
        """
        Descarga la página de núcleos urbanos.
        """

        response = self.session.get(
            NUCLEI_URL,
            params={"CodMuni": municipality_code},
            timeout=TIMEOUT,
        )

        response.raise_for_status()

        response.encoding = response.apparent_encoding

        return response.text