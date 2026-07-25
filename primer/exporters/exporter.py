"""
Clase base para todos los exportadores.

Define el contrato que deben implementar los componentes encargados
de exportar el modelo interno de Primer a distintos formatos.
"""

from __future__ import annotations

from abc import abstractmethod
from pathlib import Path
from typing import Iterable

from ..core.component import BaseComponent
from ..core.models import ExternalResource


class BaseExporter(BaseComponent):
    """
    Clase base para cualquier exportador.

    Un exportador convierte uno o varios objetos del modelo interno
    en un formato de salida determinado.
    """

    #: Formatos soportados por el exportador.
    supported_formats: tuple[str, ...] = ()

    @classmethod
    def validate_definition(cls) -> None:
        """
        Comprueba que la definición del exportador es válida.
        """

        super().validate_definition()

        if not cls.supported_formats:
            raise ValueError(
                f"{cls.__name__} debe definir "
                "'supported_formats'."
            )

    @abstractmethod
    def export(
        self,
        resources: Iterable[ExternalResource],
        destination: str | Path,
    ) -> None:
        """
        Exporta una colección de recursos al destino indicado.
        """

    def can_export(
        self,
        extension: str,
    ) -> bool:
        """
        Indica si el exportador soporta una determinada extensión.
        """

        extension = extension.lower().lstrip(".")

        return extension in {
            fmt.lower().lstrip(".")
            for fmt in self.supported_formats
        }