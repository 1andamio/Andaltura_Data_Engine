"""
Registro de Datasets.

Permite registrar y recuperar definiciones de Dataset disponibles
dentro del framework Primer.
"""

from __future__ import annotations

from .dataset import Dataset


class DatasetRegistry:
    """
    Registro de Datasets.
    """

    def __init__(self) -> None:
        """
        Inicializa el registro.
        """

        self._datasets: dict[str, Dataset] = {}

    def register(
        self,
        dataset: Dataset,
    ) -> None:
        """
        Registra un Dataset.
        """

        self._datasets[dataset.id] = dataset

    def unregister(
        self,
        dataset_id: str,
    ) -> None:
        """
        Elimina un Dataset del registro.
        """

        self._datasets.pop(dataset_id, None)

    def exists(
        self,
        dataset_id: str,
    ) -> bool:
        """
        Comprueba si un Dataset está registrado.
        """

        return dataset_id in self._datasets

    def get(
        self,
        dataset_id: str,
    ) -> Dataset:
        """
        Devuelve un Dataset registrado.
        """

        return self._datasets[dataset_id]

    def all(self) -> tuple[Dataset, ...]:
        """
        Devuelve todos los Datasets registrados.
        """

        return tuple(self._datasets.values())

    def ids(self) -> tuple[str, ...]:
        """
        Devuelve los identificadores registrados.
        """

        return tuple(self._datasets.keys())

    def count(self) -> int:
        """
        Devuelve el número de Datasets registrados.
        """

        return len(self._datasets)

    def clear(self) -> None:
        """
        Elimina todos los Datasets.
        """

        self._datasets.clear()