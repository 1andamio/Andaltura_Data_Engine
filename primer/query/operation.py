"""
Clase base para todas las operaciones del Query Engine.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Operation(ABC):
    """
    Representa una operación ejecutable del Query Engine.
    """

    @abstractmethod
    def apply(self, dataset):
        """
        Aplica la operación sobre un dataset y devuelve
        un nuevo dataset.
        """
        raise NotImplementedError