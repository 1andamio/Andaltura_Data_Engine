"""
MDTA - Diccionario Maestro
Lifecycle

Campos relacionados con el ciclo de vida de cualquier entidad.
"""

from models import Field
from mdta_types import DataType


class Lifecycle:

    # ==========================================================
    # ESTADO GENERAL
    # ==========================================================

    STATUS = Field(
        name="status",
        datatype=DataType.TEXT,
        nullable=False,
        default="draft",
        indexed=True,
        description="Estado general del registro."
    )

    ACTIVE = Field(
        name="active",
        datatype=DataType.BOOLEAN,
        nullable=False,
        default=True,
        indexed=True,
        description="Indica si el registro está activo."
    )

    VISIBLE = Field(
        name="visible",
        datatype=DataType.BOOLEAN,
        nullable=False,
        default=True,
        indexed=True,
        description="Controla la visibilidad."
    )

    PUBLISHED = Field(
        name="published",
        datatype=DataType.BOOLEAN,
        nullable=False,
        default=False,
        indexed=True,
        description="Indica si está publicado."
    )

    FEATURED = Field(
        name="featured",
        datatype=DataType.BOOLEAN,
        nullable=False,
        default=False,
        indexed=True,
        description="Elemento destacado."
    )

    # ==========================================================
    # FECHAS
    # ==========================================================

    PUBLICATION_DATE = Field(
        name="publication_date",
        datatype=DataType.DATETIME,
        description="Fecha de publicación."
    )

    EXPIRATION_DATE = Field(
        name="expiration_date",
        datatype=DataType.DATETIME,
        description="Fecha de expiración."
    )

    ARCHIVED_DATE = Field(
        name="archived_date",
        datatype=DataType.DATETIME,
        description="Fecha de archivado."
    )

    # ==========================================================
    # CONTROL
    # ==========================================================

    LOCKED = Field(
        name="locked",
        datatype=DataType.BOOLEAN,
        default=False,
        description="Registro bloqueado para edición."
    )

    READ_ONLY = Field(
        name="read_only",
        datatype=DataType.BOOLEAN,
        default=False,
        description="Solo lectura."
    )

    ARCHIVED = Field(
        name="archived",
        datatype=DataType.BOOLEAN,
        default=False,
        indexed=True,
        description="Registro archivado."
    )

    DELETED = Field(
        name="deleted",
        datatype=DataType.BOOLEAN,
        default=False,
        indexed=True,
        description="Eliminación lógica."
    )

    # ==========================================================
    # SINCRONIZACIÓN
    # ==========================================================

    SYNC_REQUIRED = Field(
        name="sync_required",
        datatype=DataType.BOOLEAN,
        default=False,
        description="Pendiente de sincronización."
    )

    LAST_SYNC = Field(
        name="last_sync",
        datatype=DataType.DATETIME,
        description="Última sincronización."
    )

    EXTERNAL_ID = Field(
        name="external_id",
        datatype=DataType.TEXT,
        indexed=True,
        description="Identificador en sistemas externos."
    )