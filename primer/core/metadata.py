"""
primer/core/metadata.py

Define el modelo Metadata.

Metadata describe el recurso publicado por una fuente de datos, pero no
describe cómo Primer lo obtuvo.

Es un objeto completamente inmutable y puede compartirse entre múltiples
registros sin riesgo de modificaciones accidentales.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Metadata:
    """
    Describe un recurso publicado por una fuente de datos.

    Esta clase únicamente contiene información descriptiva del recurso.
    No almacena información relacionada con la adquisición realizada por
    Primer.

    Attributes
    ----------
    source:
        Nombre de la fuente de datos.

    provider:
        Organismo o entidad responsable de la publicación.

    dataset:
        Nombre del conjunto de datos.

    url:
        Dirección oficial del recurso.

    format:
        Formato del recurso (JSON, XML, CSV, HTML, GML, GeoJSON...).

    mime_type:
        Tipo MIME del recurso.

    version:
        Versión publicada por la fuente.

    license:
        Licencia del conjunto de datos.

    language:
        Idioma principal del recurso.

    encoding:
        Codificación del contenido.
    """

    # ------------------------------------------------------------------
    # Identificación
    # ------------------------------------------------------------------

    source: str

    provider: str

    dataset: str

    # ------------------------------------------------------------------
    # Localización
    # ------------------------------------------------------------------

    url: str | None = None

    # ------------------------------------------------------------------
    # Información técnica
    # ------------------------------------------------------------------

    format: str | None = None

    mime_type: str | None = None

    version: str | None = None

    encoding: str | None = None

    language: str | None = None

    license: str | None = None

    # ------------------------------------------------------------------
    # Propiedades
    # ------------------------------------------------------------------

    @property
    def has_url(self) -> bool:
        """Indica si el recurso dispone de una URL."""
        return self.url is not None

    @property
    def has_version(self) -> bool:
        """Indica si el recurso dispone de versión."""
        return self.version is not None

    @property
    def has_license(self) -> bool:
        """Indica si el recurso especifica una licencia."""
        return self.license is not None

    @property
    def is_remote(self) -> bool:
        """Indica si el recurso es remoto."""
        return self.url is not None