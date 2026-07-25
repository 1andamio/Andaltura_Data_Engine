"""
Clase base para todos los analizadores.

Define el contrato que deben implementar los componentes encargados
de interpretar formatos de datos soportados por Primer.
"""

from __future__ import annotations

from abc import abstractmethod
from pathlib import Path
from typing import Any

from ..core.component import BaseComponent


class BaseParser(BaseComponent):
    """
    Clase base para cualquier analizador.

    Un analizador interpreta un formato de datos y lo convierte en una
    estructura Python que pueda ser procesada por el resto del
    framework.
    """

    #: Formatos soportados.
    supported_formats: tuple[str, ...] = ()

    @classmethod
    def validate_definition(cls) -> None:
        """
        Comprueba que la definición del analizador es válida.
        """

        super().validate_definition()

        if not cls.supported_formats:
            raise ValueError(
                f"{cls.__name__} debe definir "
                "'supported_formats'."
            )

    @abstractmethod
    def parse(
        self,
        source: str | Path | bytes,
    ) -> Any:
        """
        Analiza una fuente de datos y devuelve una estructura Python.
        """

    def can_parse(
        self,
        extension: str,
    ) -> bool:
        """
        Indica si el analizador soporta una determinada extensión.
        """

        extension = extension.lower().lstrip(".")

        return extension in {
            fmt.lower().lstrip(".")
            for fmt in self.supported_formats
        }