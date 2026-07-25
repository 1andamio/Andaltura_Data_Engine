"""
Recurso de un Dataset.

Representa un archivo o recurso asociado a un Dataset. Un mismo Dataset
puede estar formado por uno o varios recursos.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class DatasetResource:
    """
    Recurso asociado a un Dataset.
    """

    #: Identificador del recurso.
    id: str

    #: URL del recurso.
    url: str

    #: Nombre del archivo.
    filename: str

    #: Descripción.
    description: str = ""

    #: Checksum esperado.
    checksum: str | None = None

    #: Algoritmo utilizado para el checksum.
    checksum_algorithm: str = "sha256"

    #: Tamaño esperado en bytes.
    size: int | None = None

    #: Indica si el recurso es obligatorio.
    required: bool = True

    #: Metadatos adicionales.
    metadata: dict[str, object] = field(default_factory=dict)

    @property
    def has_checksum(self) -> bool:
        """
        Indica si el recurso dispone de checksum.
        """

        return self.checksum is not None

    @property
    def has_size(self) -> bool:
        """
        Indica si el recurso tiene tamaño conocido.
        """

        return self.size is not None

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
        default: object | None = None,
    ) -> object | None:
        """
        Recupera un metadato.
        """

        return self.metadata.get(key, default)