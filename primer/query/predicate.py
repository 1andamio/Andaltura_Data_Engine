"""
Predicados reutilizables para consultas sobre datasets.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Predicate(ABC, Generic[T]):
    """
    Clase base para cualquier condición de filtrado.
    """

    @abstractmethod
    def __call__(self, item: T) -> bool:
        """
        Devuelve True si el elemento cumple la condición.
        """
        raise NotImplementedError