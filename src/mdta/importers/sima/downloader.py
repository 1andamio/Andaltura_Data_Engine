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

        response = self.session.get(
            url,
            params=params,
            timeout=TIMEOUT,
        )

        response.raise_for_status()

        print("\n================= DEBUG HTTP =================")
        print("URL               :", response.url)
        print("Status            :", response.status_code)
        print("Content-Type      :", response.headers.get("Content-Type"))
        print("Header encoding   :", response.encoding)
        print("Apparent encoding :", response.apparent_encoding)
        print("Primeros bytes    :", response.content[:80])
        print("==============================================")

        # Dejamos que requests haga la decodificación.
        return response.text

    def get_municipality(self, municipality_code: str) -> str:

        return self._download(
            MUNICIPAL_URL,
            {"mun": municipality_code},
        )

    def get_nuclei(self, municipality_code: str) -> str:

        return self._download(
            NUCLEI_URL,
            {"CodMuni": municipality_code},
        )