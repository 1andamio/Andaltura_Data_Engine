"""
MDTA - Diccionario Maestro
Campos de Auditoría

Campos utilizados para registrar la trazabilidad de cada registro.
"""

from models import Field
from mdta_types import DataType


class Audit:

    # ==========================================================
    # FECHAS
    # ==========================================================

    CREATED_AT = Field(
        name="created_at",
        datatype=DataType.DATETIME,
        nullable=False,
        description="Fecha de creación del registro."
    )

    UPDATED_AT = Field(
        name="updated_at",
        datatype=DataType.DATETIME,
        description="Última fecha de modificación."
    )

    DELETED_AT = Field(
        name="deleted_at",
        datatype=DataType.DATETIME,
        description="Fecha de eliminación lógica."
    )

    # ==========================================================
    # USUARIOS
    # ==========================================================

    CREATED_BY = Field(
        name="created_by",
        datatype=DataType.TEXT,
        description="Usuario que creó el registro."
    )

    UPDATED_BY = Field(
        name="updated_by",
        datatype=DataType.TEXT,
        description="Último usuario que modificó el registro."
    )

    DELETED_BY = Field(
        name="deleted_by",
        datatype=DataType.TEXT,
        description="Usuario que eliminó el registro."
    )

    # ==========================================================
    # CONTROL
    # ==========================================================

    VERSION = Field(
        name="version",
        datatype=DataType.INTEGER,
        nullable=False,
        default=1,
        description="Versión del registro."
    )

    REVISION = Field(
        name="revision",
        datatype=DataType.INTEGER,
        nullable=False,
        default=0,
        description="Número de revisiones."
    )

    HASH = Field(
        name="hash",
        datatype=DataType.TEXT,
        indexed=True,
        description="Hash del contenido del registro."
    )

    CHECKSUM = Field(
        name="checksum",
        datatype=DataType.TEXT,
        description="Checksum para verificar integridad."
    )

    # ==========================================================
    # IMPORTACIÓN
    # ==========================================================

    SOURCE = Field(
        name="source",
        datatype=DataType.TEXT,
        description="Origen de los datos."
    )

    SOURCE_FILE = Field(
        name="source_file",
        datatype=DataType.TEXT,
        description="Archivo de origen."
    )

    SOURCE_ID = Field(
        name="source_id",
        datatype=DataType.TEXT,
        indexed=True,
        description="Identificador del registro en el origen."
    )

    IMPORT_BATCH = Field(
        name="import_batch",
        datatype=DataType.TEXT,
        indexed=True,
        description="Lote de importación."
    )

    IMPORT_DATE = Field(
        name="import_date",
        datatype=DataType.DATETIME,
        description="Fecha de importación."
    )

    # ==========================================================
    # CALIDAD
    # ==========================================================

    VALIDATED = Field(
        name="validated",
        datatype=DataType.BOOLEAN,
        default=False,
        indexed=True,
        description="Indica si el registro ha sido validado."
    )

    VALIDATION_DATE = Field(
        name="validation_date",
        datatype=DataType.DATETIME,
        description="Fecha de validación."
    )

    QUALITY_SCORE = Field(
        name="quality_score",
        datatype=DataType.REAL,
        description="Puntuación de calidad del registro."
    )