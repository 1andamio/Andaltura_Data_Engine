"""
Clase base para todos los normalizadores.

Define el contrato que deben implementar los componentes encargados
de homogeneizar las estructuras de datos producidas por los
analizadores.
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Any

from ..core.component import BaseComponent


class BaseNormalizer(BaseComponent):
    """
    Clase base para cualquier normalizador.

    Un normalizador transforma estructuras de datos heterogéneas en
    una representación uniforme que pueda ser utilizada por los
    transformadores del framework.
    """

    @classmethod
    def validate_definition(cls) -> None:
        """
        Comprueba que la definición del normalizador es válida.
        """

        super().validate_definition()

    @abstractmethod
    def normalize(
        self,
        data: Any,
    ) -> Any:
        """
        Normaliza una estructura de datos y devuelve una representación
        homogénea.
        """