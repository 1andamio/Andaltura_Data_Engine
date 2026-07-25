"""
Motor de ejecución del pipeline.

Coordina la ejecución secuencial de las etapas que componen un flujo
de procesamiento en Primer.
"""

from __future__ import annotations

from .context import PipelineContext
from .result import PipelineResult
from .stage import PipelineStage


class Pipeline:
    """
    Motor de ejecución del pipeline.
    """

    def __init__(self) -> None:

        self._stages: list[PipelineStage] = []

    @property
    def stages(self) -> tuple[PipelineStage, ...]:
        """
        Devuelve las etapas registradas.
        """

        return tuple(self._stages)

    def add_stage(
        self,
        stage: PipelineStage,
    ) -> None:
        """
        Añade una etapa al pipeline.
        """

        self._stages.append(stage)

    def remove_stage(
        self,
        name: str,
    ) -> None:
        """
        Elimina una etapa.
        """

        self._stages = [

            stage

            for stage in self._stages

            if stage.name != name

        ]

    def clear(self) -> None:
        """
        Elimina todas las etapas.
        """

        self._stages.clear()

    def run(self) -> PipelineResult:
        """
        Ejecuta el pipeline.
        """

        context = PipelineContext()

        for stage in self._stages:

            if not stage.enabled:
                continue

            #
            # Aquí cada componente ejecutará su lógica.
            #
            # Lo implementaremos cuando desarrollemos los
            # componentes concretos.
            #

        result = PipelineResult()

        result.resources.extend(
            context.resources
        )

        result.warnings.extend(
            context.warnings
        )

        result.errors.extend(
            context.errors
        )

        result.statistics.update(
            context.statistics
        )

        result.success = not context.errors

        return result