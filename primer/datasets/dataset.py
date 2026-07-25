"""
Representación de un Dataset.

Un Dataset representa una fuente de información identificable,
incluyendo su origen, metadatos, archivos asociados y estado
dentro del framework Primer.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from .dataset_file import DatasetFile


@dataclass(slots=True)
class Dataset:
    """
    Representa un Dataset.
    """

    # ------------------------------------------------------------------
    # Identidad
    # ------------------------------------------------------------------

    #: Identificador único.
    id: str

    #: Nombre del dataset.
    name: str

    #: Descripción.
    description: str = ""

    #: Categoría.
    category: str = ""

    #: Etiquetas.
    tags: list[str] = field(default_factory=list)

    # ------------------------------------------------------------------
    # Origen
    # ------------------------------------------------------------------

    #: Organismo proveedor.
    provider: str = ""

    #: URL oficial.
    url: str = ""

    #: Licencia.
    license: str = ""

    #: Formato principal.
    format: str = ""

    #: Versión publicada.
    version: str = ""

    # ------------------------------------------------------------------
    # Cobertura
    # ------------------------------------------------------------------

    #: Cobertura territorial.
    spatial_coverage: str = ""

    #: Cobertura temporal.
    temporal_coverage: str = ""

    #: Frecuencia de actualización.
    update_frequency: str = ""

    # ------------------------------------------------------------------
    # Estado
    # ------------------------------------------------------------------

    #: Estado actual.
    status: str = "defined"

    #: Prioridad.
    priority: str = "normal"

    # ------------------------------------------------------------------
    # Fechas
    # ------------------------------------------------------------------

    #: Fecha de creación del objeto.
    created_at: datetime = field(default_factory=datetime.utcnow)

    #: Fecha de la última descarga.
    downloaded_at: datetime | None = None

    #: Fecha de la última actualización.
    updated_at: datetime | None = None

    # ------------------------------------------------------------------
    # Archivos
    # ------------------------------------------------------------------

    #: Archivos asociados.
    files: list[DatasetFile] = field(default_factory=list)

    # ------------------------------------------------------------------
    # Información adicional
    # ------------------------------------------------------------------

    #: Metadatos libres.
    metadata: dict[str, object] = field(default_factory=dict)

    # ------------------------------------------------------------------
    # Propiedades
    # ------------------------------------------------------------------

    @property
    def downloaded(self) -> bool:
        """
        Indica si el dataset ha sido descargado.
        """

        return self.downloaded_at is not None

    @property
    def file_count(self) -> int:
        """
        Número de archivos.
        """

        return len(self.files)

    @property
    def total_size(self) -> int:
        """
        Tamaño total de los archivos.
        """

        return sum(file.size for file in self.files)

    # ------------------------------------------------------------------
    # Gestión de archivos
    # ------------------------------------------------------------------

    def add_file(
        self,
        file: DatasetFile,
    ) -> None:
        """
        Añade un archivo al dataset.
        """

        self.files.append(file)

    def remove_file(
        self,
        filename: str,
    ) -> None:
        """
        Elimina un archivo por nombre.
        """

        self.files = [

            file

            for file in self.files

            if file.filename != filename

        ]

    def clear_files(self) -> None:
        """
        Elimina todos los archivos.
        """

        self.files.clear()

    # ------------------------------------------------------------------
    # Metadatos
    # ------------------------------------------------------------------

    def set_metadata(
        self,
        key: str,
        value: object,
    ) -> None:
        """
        Guarda un metadato.
        """

        self.metadata[key] = value

    def get_metadata(
        self,
        key: str,
        default: object = None,
    ) -> object:
        """
        Obtiene un metadato.
        """

        return self.metadata.get(key, default)

    # ------------------------------------------------------------------
    # Estado
    # ------------------------------------------------------------------

    def mark_downloaded(self) -> None:
        """
        Marca el dataset como descargado.
        """

        self.downloaded_at = datetime.utcnow()
        self.status = "downloaded"

    def mark_processed(self) -> None:
        """
        Marca el dataset como procesado.
        """

        self.updated_at = datetime.utcnow()
        self.status = "processed"

    def mark_failed(self) -> None:
        """
        Marca el dataset como fallido.
        """

        self.updated_at = datetime.utcnow()
        self.status = "failed"