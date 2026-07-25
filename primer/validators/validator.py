"""
Clase base para todos los validadores.

Define el contrato que deben implementar los componentes encargados
de validar los objetos del modelo interno utilizados por Primer.
"""

from __future__ import annotations

from abc import abstractmethod

from ..core.component import BaseComponent
from ..core.models import ExternalResource


class BaseValidator(BaseComponent):
    """
    Clase base para cualquier validador.

    Un validador comprueba la integridad, consistencia y calidad de los
    objetos del modelo interno del framework.
    """

    @classmethod
    def validate_definition(cls) -> None:
        """
        Comprueba que la definición del validador es válida.
        """

        super().validate_definition()

    @abstractmethod
    def validate(
        self,
        resource: ExternalResource,
    ) -> ExternalResource:
        """
        Valida un objeto del modelo interno y devuelve el recurso
        validado.
        """