"""
Resultado de una descarga.

Representa el resultado de una operación de adquisición de un Dataset.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class DownloadResult:
    """
    Resultado de una descarga.
    """

    #: Indica si la descarga fue correcta.
    success: bool = False

    #: Ruta del archivo descargado.
    file: Path | None = None

    #: Tamaño del archivo en bytes.
    size: int = 0

    #: SHA-256 del archivo.
    checksum: str | None = None

    #: Tiempo empleado en segundos.
    elapsed: float = 0.0

    #: Mensaje descriptivo.
    message: str = ""

    @property
    def downloaded(self) -> bool:
        """
        Indica si existe un archivo descargado.
        """

        return self.file is not None

    @property
    def filename(self) -> str | None:
        """
        Devuelve el nombre del archivo.
        """

        if self.file is None:
            return None

        return self.file.name