"""
Representación de un archivo perteneciente a un dataset.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class DatasetFile:
    """
    Representa un archivo físico perteneciente a un Dataset.
    """

    #: Nombre del archivo.
    name: str

    #: Ruta del archivo.
    path: Path

    #: Tamaño en bytes.
    size: int = 0

    #: Checksum SHA256.
    checksum: str | None = None

    #: Tipo MIME.
    mime_type: str | None = None

    #: Indica si el archivo existe.
    @property
    def exists(self) -> bool:
        """
        Comprueba si el archivo existe.
        """

        return self.path.exists()

    @property
    def suffix(self) -> str:
        """
        Devuelve la extensión del archivo.
        """

        return self.path.suffix.lower()

    @property
    def filename(self) -> str:
        """
        Devuelve el nombre del archivo.
        """

        return self.path.name