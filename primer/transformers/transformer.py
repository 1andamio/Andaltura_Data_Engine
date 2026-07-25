"""
Clase base para todos los transformadores.

Define el contrato que deben implementar los componentes encargados
de convertir estructuras de datos normalizadas en el modelo interno
utilizado por Primer.
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any

from ..core.component import BaseComponent
from ..core.models import ExternalResource


class BaseTransformer(BaseComponent):
    """
    Clase base para cualquier transformador.

    Un transformador convierte estructuras de datos normalizadas en uno
    o varios objetos del modelo interno del framework.
    """

    @classmethod
    def validate_definition(cls) -> None:
        """
        Comprueba que la definición del transformador es válida.
        """

        super().validate_definition()

    @abstractmethod
    def transform(
        self,
        data: Any,
    ) -> ExternalResource | list[ExternalResource]:
        """
        Convierte una estructura de datos normalizada en uno o varios
        objetos del modelo interno.
        """