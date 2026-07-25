"""
Catálogo de Datasets.

Gestiona la colección de datasets conocidos por Primer.
El catálogo representa el inventario permanente de datasets
disponibles, independientemente de su estado de descarga.
"""

from __future__ import annotations

from .dataset import Dataset


class DatasetCatalog:
    """
    Catálogo de Datasets.
    """

    def __init__(self) -> None:
        """
        Inicializa un catálogo vacío.
        """

        self._datasets: dict[str, Dataset] = {}

    @property
    def datasets(self) -> tuple[Dataset, ...]:
        """
        Devuelve todos los datasets del catálogo.
        """

        return tuple(self._datasets.values())

    def add(
        self,
        dataset: Dataset,
    ) -> None:
        """
        Añade un Dataset al catálogo.

        Si ya existe un Dataset con el mismo identificador,
        será reemplazado.
        """

        self._datasets[dataset.id] = dataset

    def remove(
        self,
        dataset_id: str,
    ) -> None:
        """
        Elimina un Dataset del catálogo.
        """

        self._datasets.pop(dataset_id, None)

    def get(
        self,
        dataset_id: str,
    ) -> Dataset | None:
        """
        Devuelve un Dataset por su identificador.

        Si no existe, devuelve None.
        """

        return self._datasets.get(dataset_id)

    def exists(
        self,
        dataset_id: str,
    ) -> bool:
        """
        Comprueba si un Dataset existe en el catálogo.
        """

        return dataset_id in self._datasets

    def find_by_provider(
        self,
        provider: str,
    ) -> tuple[Dataset, ...]:
        """
        Devuelve todos los datasets de un proveedor.
        """

        return tuple(
            dataset
            for dataset in self._datasets.values()
            if dataset.provider == provider
        )

    def find_by_category(
        self,
        category: str,
    ) -> tuple[Dataset, ...]:
        """
        Devuelve todos los datasets de una categoría.
        """

        return tuple(
            dataset
            for dataset in self._datasets.values()
            if dataset.category == category
        )

    def count(self) -> int:
        """
        Devuelve el número de datasets del catálogo.
        """

        return len(self._datasets)

    def clear(self) -> None:
        """
        Elimina todos los datasets.
        """

        self._datasets.clear()