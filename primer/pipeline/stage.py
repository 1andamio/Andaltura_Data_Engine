"""
Definición de una etapa del pipeline.

Representa un componente que participa en una ejecución del pipeline,
indicando su nombre y la instancia asociada.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..core.component import BaseComponent


@dataclass(slots=True)
class PipelineStage:
    """
    Representa una etapa del pipeline.
    """

    #: Nombre de la etapa.
    name: str

    #: Componente asociado.
    component: BaseComponent

    #: Indica si la etapa está habilitada.
    enabled: bool = True