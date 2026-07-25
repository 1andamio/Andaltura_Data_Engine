"""
Gestión de datasets.

Este paquete proporciona las clases necesarias para representar,
catalogar y gestionar datasets dentro del framework Primer.

Un Dataset representa una fuente de información identificable,
mientras que uno o varios DatasetFile representan los archivos
físicos asociados a dicho dataset.
"""

from .dataset import Dataset
from .dataset_file import DatasetFile

__all__ = [
    "Dataset",
    "DatasetFile",
]