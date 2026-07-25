"""
Gestor de Datasets.

Coordina las operaciones sobre los datasets registrados en Primer.
Actúa como punto de entrada para la gestión del catálogo y del
registro de datasets.
"""

from __future__ import annotations

from .catalog import DatasetCatalog
from .dataset import Dataset
from .registry import DatasetRegistry


class DatasetManager:
    """
    Gestor de Datasets.
    """

    def __init__(self) -> None:
        """
        Inicializa el gestor.
        """

        self._catalog = DatasetCatalog()
        self._registry = DatasetRegistry()

    @property
    def catalog(self) -> DatasetCatalog:
        """
        Devuelve el catálogo de datasets.
        """

        return self._catalog

    @property
    def registry(self) -> DatasetRegistry:
        """
        Devuelve el registro de datasets.
        """

        return self._registry

    # ------------------------------------------------------------------
    # Registro
    # ------------------------------------------------------------------

    def register(
        self,
        dataset: Dataset,
    ) -> None:
        """
        Registra un Dataset.

        El Dataset se añade tanto al catálogo como al registro.
        """

        self._catalog.add(dataset)
        self._registry.register(dataset)

    def unregister(
        self,
        dataset_id: str,
    ) -> None:
        """
        Elimina un Dataset.
        """

        self._catalog.remove(dataset_id)
        self._registry.unregister(dataset_id)

    # ------------------------------------------------------------------
    # Consulta
    # ------------------------------------------------------------------

    def exists(
        self,
        dataset_id: str,
    ) -> bool:
        """
        Comprueba si un Dataset existe.
        """

        return self._catalog.exists(dataset_id)

    def get(
        self,
        dataset_id: str,
    ) -> Dataset | None:
        """
        Devuelve un Dataset.
        """

        return self._catalog.get(dataset_id)

    def datasets(self) -> tuple[Dataset, ...]:
        """
        Devuelve todos los datasets.
        """

        return self._catalog.datasets

    def count(self) -> int:
        """
        Devuelve el número de datasets.
        """

        return self._catalog.count()

    # ------------------------------------------------------------------
    # Gestión
    # ------------------------------------------------------------------

    def clear(self) -> None:
        """
        Elimina todos los datasets.
        """

        self._catalog.clear()
        self._registry.clear()