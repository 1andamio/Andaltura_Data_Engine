"""
Modelos base del framework Primer.

Define los objetos comunes utilizados durante la adquisición,
procesamiento y transformación de recursos externos antes de su
integración en otros sistemas.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from .exceptions import PrimerError


@dataclass(slots=True)
class ExternalResource:
    """
    Representa un recurso obtenido desde una fuente externa.

    Este modelo actúa como objeto de intercambio entre los distintos
    componentes del framework y no representa una entidad del modelo
    de datos final.
    """

    # ------------------------------------------------------------------
    # Identificación
    # ------------------------------------------------------------------

    identifier: str

    name: str

    source: str

    resource_type: str = ""

    # ------------------------------------------------------------------
    # Información espacial
    # ------------------------------------------------------------------

    geometry: Any | None = None

    bbox: Any | None = None

    crs: str | None = None

    # ------------------------------------------------------------------
    # Origen
    # ------------------------------------------------------------------

    source_url: str | None = None

    source_file: str | None = None

    # ------------------------------------------------------------------
    # Información adicional
    # ------------------------------------------------------------------

    metadata: dict[str, Any] = field(default_factory=dict)

    attributes: dict[str, Any] = field(default_factory=dict)

    tags: set[str] = field(default_factory=set)

    # ------------------------------------------------------------------
    # Estado
    # ------------------------------------------------------------------

    is_valid: bool = True

    status: str = "new"

    errors: list[PrimerError] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)

    created_at: datetime = field(default_factory=datetime.utcnow)

    updated_at: datetime | None = None

    # ------------------------------------------------------------------
    # Utilidades
    # ------------------------------------------------------------------

    def add_error(self, error: PrimerError) -> None:
        """
        Registra un error asociado al recurso.
        """
        self.is_valid = False
        self.errors.append(error)

    def add_warning(self, message: str) -> None:
        """
        Registra una advertencia.
        """
        self.warnings.append(message)

    def set_attribute(self, key: str, value: Any) -> None:
        """
        Añade o actualiza un atributo.
        """
        self.attributes[key] = value

    def get_attribute(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Recupera un atributo.
        """
        return self.attributes.get(key, default)

    def add_tag(self, tag: str) -> None:
        """
        Añade una etiqueta al recurso.
        """
        self.tags.add(tag)