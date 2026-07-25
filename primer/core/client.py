"""
Cliente HTTP del framework.

Proporciona una interfaz de alto nivel para realizar peticiones HTTP,
obtener contenido en distintos formatos y descargar recursos desde
fuentes externas.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import requests

from .session import HttpSession
from .settings import settings


class HttpClient:
    """
    Cliente HTTP reutilizable.

    Centraliza las operaciones HTTP comunes utilizadas por el framework,
    delegando la gestión de la conexión en ``HttpSession``.
    """

    def __init__(
        self,
        session: HttpSession,
    ) -> None:
        self.session = session

    # ------------------------------------------------------------------
    # Context Manager
    # ------------------------------------------------------------------

    def __enter__(self) -> "HttpClient":
        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ) -> bool:
        return False

    # ------------------------------------------------------------------
    # Solicitudes HTTP
    # ------------------------------------------------------------------

    def get(
        self,
        url: str,
        **kwargs: Any,
    ) -> requests.Response:
        """
        Realiza una petición HTTP GET.
        """

        return self.session.get(url, **kwargs)

    def post(
        self,
        url: str,
        **kwargs: Any,
    ) -> requests.Response:
        """
        Realiza una petición HTTP POST.
        """

        return self.session.post(url, **kwargs)

    # ------------------------------------------------------------------
    # Contenido
    # ------------------------------------------------------------------

    def get_text(
        self,
        url: str,
        encoding: str | None = None,
        **kwargs: Any,
    ) -> str:
        """
        Obtiene el contenido textual de un recurso.
        """

        response = self.get(url, **kwargs)

        if encoding is not None:
            response.encoding = encoding

        return response.text

    def get_bytes(
        self,
        url: str,
        **kwargs: Any,
    ) -> bytes:
        """
        Obtiene el contenido binario de un recurso.
        """

        response = self.get(url, **kwargs)

        return response.content

    def get_json(
        self,
        url: str,
        **kwargs: Any,
    ) -> Any:
        """
        Obtiene y deserializa un documento JSON.
        """

        response = self.get(url, **kwargs)

        return response.json()

    # ------------------------------------------------------------------
    # Descargas
    # ------------------------------------------------------------------

    def download(
        self,
        url: str,
        destination: Path,
        chunk_size: int | None = None,
        **kwargs: Any,
    ) -> Path:
        """
        Descarga un recurso y lo almacena en el sistema de archivos.
        """

        if chunk_size is None:
            chunk_size = settings.download_chunk_size

        response = self.get(
            url,
            stream=True,
            **kwargs,
        )

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with destination.open("wb") as file:

            for chunk in response.iter_content(chunk_size=chunk_size):

                if chunk:
                    file.write(chunk)

        return destination