"""
Configuración del importador del SIMA.
"""

from __future__ import annotations

BASE_URL = "https://ws089.juntadeandalucia.es/sima"

MUNICIPAL_URL = f"{BASE_URL}/ficha.htm"

NUCLEI_URL = f"{BASE_URL}/nucleos.htm"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/145.0 Safari/537.36"
    )
}

TIMEOUT = 30