"""
Utilidades para ordenar datasets.
"""

from __future__ import annotations

from typing import Any


class OrderBy:
    """
    Representa un criterio de ordenación.
    """

    def __init__(self, field, ascending: bool = True):
        self.field = field
        self.ascending = ascending

    def key(self, item: Any) -> Any:
        return self.field.value(item)