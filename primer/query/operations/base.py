"""
Clase base para todas las operaciones del Query Engine.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Operation(ABC, Generic[T]):
    """
    Representa una operación del Query Engine.

    Las operaciones describen QUÉ hacer,
    pero no CÓMO hacerlo.
    """

    @abstractmethod
    def apply(self, dataset):
        """
        Aplica la operación sobre un dataset.
        """
        raise NotImplementedError