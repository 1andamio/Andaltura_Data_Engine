"""
Clase base para todos los datasets del motor.
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from primer.query.query import Query

T = TypeVar("T")


class BaseDataset(Generic[T]):

    def __init__(self, items: Iterable[T] | None = None):
        self._items = list(items) if items else []

    def query(self) -> "Query[T]":
        """
        Inicia una consulta.
        """
        # Importación diferida para evitar dependencias circulares.
        from primer.query.query import Query

        return Query(self)

    # ---------------------------------------------------------
    # Compatibilidad (se eliminará en v2)
    # ---------------------------------------------------------

    def where(self, expression):
        return self.query().where(expression).all()

    def order_by(self, order):
        return self.query().order_by(order).all()

    # ---------------------------------------------------------

    def add(self, item: T):
        self._items.append(item)

    def extend(self, items):
        self._items.extend(items)

    def clear(self):
        self._items.clear()

    def first(self):
        return self._items[0] if self._items else None

    def last(self):
        return self._items[-1] if self._items else None

    def to_list(self):
        return list(self._items)

    def __len__(self):
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __bool__(self):
        return bool(self._items)

    def __repr__(self):
        return f"{self.__class__.__name__}(items={len(self)})"