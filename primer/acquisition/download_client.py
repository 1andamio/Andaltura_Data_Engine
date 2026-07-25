"""
Cliente de descarga.

Implementa las operaciones de descarga de recursos remotos utilizando
HTTP/HTTPS. No conoce el modelo Dataset ni realiza ninguna lógica de
negocio; únicamente descarga archivos.
"""

from __future__ import annotations

from pathlib import Path

import requests


class DownloadClient:
    """
    Cliente de descarga HTTP/HTTPS.
    """

    DEFAULT_TIMEOUT = 30
    DEFAULT_CHUNK_SIZE = 1024 * 1024  # 1 MB

    def __init__(
        self,
        *,
        timeout: int = DEFAULT_TIMEOUT,
        chunk_size: int = DEFAULT_CHUNK_SIZE,
        verify_ssl: bool = True,
    ) -> None:
        """
        Inicializa el cliente.
        """

        self._timeout = timeout
        self._chunk_size = chunk_size
        self._verify_ssl = verify_ssl

        self._session = requests.Session()

    @property
    def timeout(self) -> int:
        """
        Tiempo máximo de espera.
        """

        return self._timeout

    @property
    def chunk_size(self) -> int:
        """
        Tamaño de los bloques de descarga.
        """

        return self._chunk_size

    @property
    def verify_ssl(self) -> bool:
        """
        Indica si se verifica el certificado SSL.
        """

        return self._verify_ssl

    def download(
        self,
        url: str,
        destination: str | Path,
    ) -> Path:
        """
        Descarga un recurso remoto.

        Parameters
        ----------
        url:
            URL del recurso.

        destination:
            Ruta completa donde guardar el archivo.

        Returns
        -------
        Path
            Ruta del archivo descargado.
        """

        destination = Path(destination)
        destination.parent.mkdir(parents=True, exist_ok=True)

        with self._session.get(
            url,
            stream=True,
            timeout=self._timeout,
            verify=self._verify_ssl,
        ) as response:

            response.raise_for_status()

            with destination.open("wb") as file:

                for chunk in response.iter_content(
                    chunk_size=self._chunk_size
                ):

                    if chunk:

                        file.write(chunk)

        return destination

    def exists(
        self,
        url: str,
    ) -> bool:
        """
        Comprueba si un recurso remoto existe.

        Parameters
        ----------
        url:
            URL del recurso.

        Returns
        -------
        bool
        """

        response = self._session.head(
            url,
            allow_redirects=True,
            timeout=self._timeout,
            verify=self._verify_ssl,
        )

        return response.ok

    def close(self) -> None:
        """
        Cierra la sesión HTTP.
        """

        self._session.close()

    def __enter__(self) -> "DownloadClient":
        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ) -> None:
        self.close()