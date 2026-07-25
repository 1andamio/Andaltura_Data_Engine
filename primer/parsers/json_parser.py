"""
Analizador de documentos JSON.

Implementa el análisis de recursos en formato JSON, tanto desde
cadenas de texto como desde archivos del sistema.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ..core.exceptions import ParseError
from .parser import BaseParser


class JsonParser(BaseParser):
    """
    Analizador de documentos JSON.
    """

    name = "json"

    version = "1.0"

    description = "Analizador para documentos JSON."

    supported_formats = (
        "json",
    )

    def parse(
        self,
        source: str | Path | bytes,
    ) -> Any:
        """
        Analiza un documento JSON.
        """

        if isinstance(source, bytes):

            try:
                source = source.decode("utf-8")

            except UnicodeDecodeError as exc:
                raise ParseError(
                    "No se pudo decodificar el contenido JSON."
                ) from exc

        if isinstance(source, Path):
            return self._parse_file(source)

        if isinstance(source, str):

            path = Path(source)

            if path.exists():
                return self._parse_file(path)

            try:
                return json.loads(source)

            except json.JSONDecodeError as exc:
                raise ParseError(
                    "El contenido no es un JSON válido."
                ) from exc

        raise ParseError(
            f"Tipo de fuente no soportado: "
            f"{type(source).__name__}."
        )

    def _parse_file(
        self,
        path: Path,
    ) -> Any:
        """
        Analiza un archivo JSON.
        """

        try:

            with path.open(
                "r",
                encoding="utf-8",
            ) as file:

                return json.load(file)

        except OSError as exc:
            raise ParseError(
                f"No se pudo leer el archivo '{path}'."
            ) from exc

        except json.JSONDecodeError as exc:
            raise ParseError(
                f"El archivo '{path}' no contiene un JSON válido."
            ) from exc