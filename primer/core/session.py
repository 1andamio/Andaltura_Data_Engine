"""
Gestión de sesiones HTTP del framework.

Proporciona una sesión HTTP reutilizable para todas las comunicaciones
con recursos externos, gestionando conexiones persistentes, cabeceras,
cookies y tiempos de espera.
"""

from __future__ import annotations

from typing import Any

import requests
from requests import RequestException

from .exceptions import ConnectionError
from .settings import settings


class HttpSession:
    """
    Gestiona una sesión HTTP reutilizable.

    Todas las operaciones HTTP del framework deben realizarse mediante
    una única instancia de esta clase.
    """

    def __init__(
        self,
        timeout: int | None = None,
        user_agent: str | None = None,
    ) -> None:

        self.timeout = timeout or settings.default_timeout

        self.session = requests.Session()

        self.session.headers.update(
            {
                "User-Agent": (
                    user_agent
                    or settings.user_agent
                )
            }
        )

    # ------------------------------------------------------------------
    # Métodos HTTP
    # ------------------------------------------------------------------

    def get(
        self,
        url: str,
        **kwargs: Any,
    ) -> requests.Response:
        """
        Realiza una petición HTTP GET.
        """

        kwargs.setdefault("timeout", self.timeout)

        try:

            response = self.session.get(
                url,
                **kwargs,
            )

            response.raise_for_status()

            return response

        except RequestException as exc:

            raise ConnectionError(
                f"Error durante la petición GET a '{url}'."
            ) from exc

    def post(
        self,
        url: str,
        **kwargs: Any,
    ) -> requests.Response:
        """
        Realiza una petición HTTP POST.
        """

        kwargs.setdefault("timeout", self.timeout)

        try:

            response = self.session.post(
                url,
                **kwargs,
            )

            response.raise_for_status()

            return response

        except RequestException as exc:

            raise ConnectionError(
                f"Error durante la petición POST a '{url}'."
            ) from exc

    # ------------------------------------------------------------------
    # Cabeceras
    # ------------------------------------------------------------------

    def set_header(
        self,
        key: str,
        value: str,
    ) -> None:
        """
        Añade o modifica una cabecera HTTP.
        """

        self.session.headers[key] = value

    def remove_header(
        self,
        key: str,
    ) -> None:
        """
        Elimina una cabecera HTTP.
        """

        self.session.headers.pop(key, None)

    # ------------------------------------------------------------------
    # Cookies
    # ------------------------------------------------------------------

    def clear_cookies(self) -> None:
        """
        Elimina todas las cookies almacenadas.
        """

        self.session.cookies.clear()

    # ------------------------------------------------------------------
    # Utilidades
    # ------------------------------------------------------------------

    def close(self) -> None:
        """
        Cierra la sesión HTTP.
        """

        self.session.close()

    def __enter__(self) -> "HttpSession":
        """
        Inicia un contexto de sesión.
        """

        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ) -> None:
        """
        Finaliza automáticamente la sesión.
        """

        self.close()