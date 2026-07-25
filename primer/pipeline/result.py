"""
Resultado de la ejecución del pipeline.

Representa el resultado completo de una ejecución del pipeline,
incluyendo los recursos generados, el estado de la ejecución y la
información de diagnóstico.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from ..core.models import ExternalResource


@dataclass(slots=True)
class PipelineResult:
    """
    Resultado de una ejecución del pipeline.
    """

    #: Indica si la ejecución finalizó correctamente.
    success: bool = True

    #: Recursos generados.
    resources: list[ExternalResource] = field(
        default_factory=list
    )

    #: Advertencias producidas durante la ejecución.
    warnings: list[str] = field(
        default_factory=list
    )

    #: Errores producidos durante la ejecución.
    errors: list[str] = field(
        default_factory=list
    )

    #: Estadísticas de la ejecución.
    statistics: dict[str, object] = field(
        default_factory=dict
    )

    def add_resource(
        self,
        resource: ExternalResource,
    ) -> None:
        """
        Añade un recurso al resultado.
        """

        self.resources.append(resource)

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

        La presencia de errores marca automáticamente la ejecución
        como no satisfactoria.
        """

        self.success = False
        self.errors.append(message)

    def set_statistic(
        self,
        key: str,
        value: object,
    ) -> None:
        """
        Registra una estadística.
        """

        self.statistics[key] = value

    @property
    def resource_count(self) -> int:
        """
        Devuelve el número de recursos generados.
        """

        return len(self.resources)

    @property
    def warning_count(self) -> int:
        """
        Devuelve el número de advertencias.
        """

        return len(self.warnings)

    @property
    def error_count(self) -> int:
        """
        Devuelve el número de errores.
        """

        return len(self.errors)