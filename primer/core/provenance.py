"""
primer/core/provenance.py

Define el modelo Provenance.

Provenance describe cómo Primer obtuvo un recurso.

A diferencia de Metadata, la información contenida aquí puede variar
cada vez que un mismo recurso es adquirido nuevamente.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC
from datetime import datetime
from types import MappingProxyType
from typing import Any
from typing import Mapping


@dataclass(slots=True, frozen=True)
class Provenance:
    """
    Describe la trazabilidad de la adquisición de un recurso.

    Attributes
    ----------
    retrieved_at:
        Fecha y hora en la que Primer obtuvo el recurso.

    source_updated_at:
        Fecha de actualización publicada por la fuente.

    checksum:
        Huella digital del contenido (SHA256, MD5, etc.).

    etag:
        Valor ETag devuelto por el servidor.

    http_status:
        Código HTTP recibido.

    elapsed:
        Tiempo empleado en la adquisición, en segundos.

    request_id:
        Identificador de la petición, cuando exista.

    extras:
        Información específica del proveedor o del protocolo.
    """

    # ------------------------------------------------------------------
    # Fechas
    # ------------------------------------------------------------------

    retrieved_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    source_updated_at: datetime | None = None

    # ------------------------------------------------------------------
    # Integridad
    # ------------------------------------------------------------------

    checksum: str | None = None

    etag: str | None = None

    # ------------------------------------------------------------------
    # Información de la adquisición
    # ------------------------------------------------------------------

    http_status: int | None = None

    elapsed: float | None = None

    request_id: str | None = None

    # ------------------------------------------------------------------
    # Extensiones
    # ------------------------------------------------------------------

    extras: Mapping[str, Any] = field(
        default_factory=lambda: MappingProxyType({})
    )

    # ------------------------------------------------------------------
    # Propiedades
    # ------------------------------------------------------------------

    @property
    def has_checksum(self) -> bool:
        """Indica si existe una huella digital."""
        return self.checksum is not None

    @property
    def has_etag(self) -> bool:
        """Indica si existe un ETag."""
        return self.etag is not None

    @property
    def has_http_status(self) -> bool:
        """Indica si existe un código HTTP."""
        return self.http_status is not None

    @property
    def was_downloaded(self) -> bool:
        """Indica si el recurso ha sido adquirido por Primer."""
        return self.retrieved_at is not None