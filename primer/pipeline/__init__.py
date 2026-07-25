"""
Motor de ejecución de Primer.

Este paquete proporciona la infraestructura necesaria para coordinar
la ejecución de los distintos componentes del framework dentro de un
flujo de procesamiento.
"""

from .context import PipelineContext
from .pipeline import Pipeline
from .result import PipelineResult
from .stage import PipelineStage

__all__ = [
    "Pipeline",
    "PipelineContext",
    "PipelineResult",
    "PipelineStage",
]