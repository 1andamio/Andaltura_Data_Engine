"""
Cliente WFS reutilizable para Primer.

Este módulo encapsula toda la comunicación con servicios WFS.

No conoce ningún proveedor concreto (IGN, IECA, Catastro, etc.).
Únicamente sabe hablar el protocolo WFS.
"""

from __future__ import annotations

from urllib.parse import urlencode

import requests


class WFSClient:
    """
    Cliente genérico para servicios WFS.
    """

    def __init__(
        self,
        base_url: str,
        *,
        version: str = "2.0.0",
        timeout: int = 60,
    ) -> None:

        self.base_url = base_url.rstrip("?")
        self.version = version
        self.timeout = timeout

        self.session = requests.Session()

    def request(self, **params) -> requests.Response:
        """
        Ejecuta una petición WFS.
        """

        defaults = {
            "service": "WFS",
            "version": self.version,
        }

        defaults.update(params)

        url = f"{self.base_url}?{urlencode(defaults)}"

        response = self.session.get(
            url,
            timeout=self.timeout,
        )

        response.raise_for_status()

        return response

    def get_capabilities(self) -> str:
        """
        Descarga el documento GetCapabilities.
        """

        response = self.request(
            request="GetCapabilities",
        )

        return response.text

    def get_feature(
        self,
        *,
        type_name: str,
        start_index: int = 0,
        count: int = 1000,
        output_format: str | None = None,
        **extra_params,
    ) -> requests.Response:
        """
        Ejecuta GetFeature.

        Devuelve siempre el objeto Response.
        El parser decidirá posteriormente cómo interpretar
        el contenido (JSON, GML, XML...).
        """

        params = {
            "request": "GetFeature",
            "typeNames": type_name,
            "startIndex": start_index,
            "count": count,
        }

        if output_format:
            params["outputFormat"] = output_format

        params.update(extra_params)

        return self.request(**params)

    def close(self) -> None:
        """
        Libera la sesión HTTP.
        """

        self.session.close()