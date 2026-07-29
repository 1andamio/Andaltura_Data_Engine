"""
Motor de consultas sobre datasets.
"""

from __future__ import annotations

from typing import Generic, TypeVar

from primer.query.expression import Expression
from primer.query.fieldset import FieldSet
from primer.query.limit_operation import LimitOperation
from primer.query.memory_executor import MemoryExecutor
from primer.query.offset_operation import OffsetOperation
from primer.query.order import OrderBy
from primer.query.order_by_operation import OrderByOperation
from primer.query.select_operation import SelectOperation
from primer.query.where_operation import WhereOperation

T = TypeVar("T")


class Query(Generic[T]):

    def __init__(self, dataset, operations=None):
        self._dataset = dataset
        self._operations = list(operations) if operations else []

    @property
    def dataset(self):
        return self._dataset

    def where(self, expression: Expression[T]) -> "Query[T]":

        operations = self._operations.copy()
        operations.append(
            WhereOperation(expression)
        )

        return Query(
            self._dataset,
            operations,
        )

    def order_by(self, order: OrderBy) -> "Query[T]":

        operations = self._operations.copy()
        operations.append(
            OrderByOperation(order)
        )

        return Query(
            self._dataset,
            operations,
        )

    def limit(self, value: int) -> "Query[T]":

        operations = self._operations.copy()
        operations.append(
            LimitOperation(value)
        )

        return Query(
            self._dataset,
            operations,
        )

    def offset(self, value: int) -> "Query[T]":

        operations = self._operations.copy()
        operations.append(
            OffsetOperation(value)
        )

        return Query(
            self._dataset,
            operations,
        )

    def select(self, *fields) -> "Query[T]":
        """
        Proyecta la consulta sobre un conjunto de campos.
        """

        operations = self._operations.copy()

        operations.append(
            SelectOperation(
                FieldSet(*fields)
            )
        )

        return Query(
            self._dataset,
            operations,
        )

    def all(self):

        executor = MemoryExecutor()

        return executor.execute(
            self._dataset,
            self._operations,
        )

    def first(self):
        return self.all().first()

    def last(self):
        return self.all().last()

    def count(self):
        return len(self.all())

    def exists(self):
        return bool(self.all())

    def to_list(self):
        return self.all().to_list()

    def __iter__(self):
        return iter(self.all())

    def __len__(self):
        return len(self.all())

    def __bool__(self):
        return self.exists()

    def __repr__(self):

        return (
            f"Query("
            f"operations={len(self._operations)}, "
            f"dataset={self._dataset!r})"
        )