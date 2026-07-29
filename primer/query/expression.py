"""
Expresiones base del motor de consultas.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Expression(ABC, Generic[T]):
    """
    Clase base para cualquier expresión evaluable.
    """

    @abstractmethod
    def evaluate(self, item: T) -> bool:
        raise NotImplementedError

    def __call__(self, item: T) -> bool:
        return self.evaluate(item)

    def __and__(self, other: "Expression[T]") -> "Expression[T]":
        from primer.query.logical import And

        return And(self, other)

    def __or__(self, other: "Expression[T]") -> "Expression[T]":
        from primer.query.logical import Or

        return Or(self, other)

    def __invert__(self) -> "Expression[T]":
        from primer.query.logical import Not

        return Not(self)