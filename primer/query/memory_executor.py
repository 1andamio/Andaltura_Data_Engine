"""
Ejecutor de consultas en memoria.
"""

from __future__ import annotations


class MemoryExecutor:
    """
    Ejecuta una consulta sobre un dataset en memoria.
    """

    def execute(self, dataset, operations):

        result = dataset

        for operation in operations:
            result = operation.apply(result)

        return result