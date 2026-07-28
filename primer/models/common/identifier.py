"""
Modelo INSPIRE Identifier.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Identifier:
    """
    Identificador INSPIRE.

    Ejemplo:

        namespace = ES.ES61.NGA
        local_id = 242130
    """

    namespace: str
    local_id: str

    @property
    def full_id(self) -> str:
        """
        Devuelve el identificador completo.
        """

        return f"{self.namespace}:{self.local_id}"

    def __str__(self) -> str:
        return self.full_id