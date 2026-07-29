"""
Clase base para todos los datasets del motor.
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Generic, TypeVar

from primer.query.expression import Expression
from primer.query.order import OrderBy

T = TypeVar("T")


class BaseDataset(Generic[T]):
    """
    Colección genérica de entidades.
    """

    def __init__(self, items: Iterable[T] | None = None) -> None:
        self._items: list[T] = list(items) if items else []

    def add(self, item: T) -> None:
        self._items.append(item)

    def extend(self, items: Iterable[T]) -> None:
        self._items.extend(items)

    def clear(self) -> None:
        self._items.clear()

    def first(self) -> T | None:
        return self._items[0] if self._items else None

    def last(self) -> T | None:
        return self._items[-1] if self._items else None

    def where(self, expression: Expression[T]) -> "BaseDataset[T]":
        return self.__class__(
            item for item in self._items if expression(item)
        )

    def order_by(self, order: OrderBy) -> "BaseDataset[T]":
        """
        Devuelve un nuevo dataset ordenado.
        """
        return self.__class__(
            sorted(
                self._items,
                key=order.key,
                reverse=not order.ascending,
            )
        )

    def to_list(self) -> list[T]:
        return list(self._items)

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __bool__(self) -> bool:
        return bool(self._items)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(items={len(self)})"