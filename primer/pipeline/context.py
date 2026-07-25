"""
Contexto de ejecución del pipeline.

Contiene el estado compartido durante la ejecución de un pipeline,
permitiendo que los distintos componentes intercambien información
de forma estructurada.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ..core.models import ExternalResource


@dataclass(slots=True)
class PipelineContext:
    """
    Estado compartido de una ejecución del pipeline.
    """

    #: Datos originales obtenidos por el proveedor.
    source: Any = None

    #: Datos interpretados por el parser.
    data: Any = None

    #: Datos normalizados.
    normalized_data: Any = None

    #: Recursos generados por el transformador.
    resources: list[ExternalResource] = field(
        default_factory=list
    )

    #: Metadatos de la ejecución.
    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    #: Estadísticas de la ejecución.
    statistics: dict[str, Any] = field(
        default_factory=dict
    )

    #: Advertencias producidas durante el proceso.
    warnings: list[str] = field(
        default_factory=list
    )

    #: Errores producidos durante el proceso.
    errors: list[str] = field(
        default_factory=list
    )

    def add_warning(
        self,
        message: str,
    ) -> None:
        """
        Añade una advertencia.
        """

        self.warnings.append(message)

    def add_error(
        self,
        message: str,
    ) -> None:
        """
        Añade un error.
        """

        self.errors.append(message)

    def set_metadata(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Establece un metadato.
        """

        self.metadata[key] = value

    def get_metadata(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Obtiene un metadato.
        """

        return self.metadata.get(key, default)

    def set_statistic(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Establece una estadística.
        """

        self.statistics[key] = value

    def get_statistic(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Obtiene una estadística.
        """

        return self.statistics.get(key, default)

    def clear(self) -> None:
        """
        Restablece el contexto a su estado inicial.
        """

        self.source = None
        self.data = None
        self.normalized_data = None

        self.resources.clear()
        self.metadata.clear()
        self.statistics.clear()
        self.warnings.clear()
        self.errors.clear()