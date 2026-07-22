"""
=========================================================
Andaltura Data Engine

Campos base reutilizables del MDTA
=========================================================
"""

from models import Field
from mdta_types import DataType


class BaseFields:
    """
    Campos reutilizables por todas las entidades del MDTA.
    """

    # =====================================================
    # CAMPOS INDIVIDUALES
    # =====================================================

    @staticmethod
    def id() -> Field:
        return Field(
            name="id",
            datatype=DataType.INTEGER,
            primary_key=True,
            nullable=False,
            description="Identificador interno"
        )

    @staticmethod
    def codigo_ine() -> Field:
        return Field(
            name="codigo_ine",
            datatype=DataType.TEXT,
            nullable=False,
            unique=True,
            indexed=True,
            description="Código oficial INE"
        )

    @staticmethod
    def codigo_iso() -> Field:
        return Field(
            name="codigo_iso",
            datatype=DataType.TEXT,
            unique=True,
            indexed=True,
            description="Código ISO 3166-2"
        )

    @staticmethod
    def nombre() -> Field:
        return Field(
            name="nombre",
            datatype=DataType.TEXT,
            nullable=False,
            indexed=True,
            description="Nombre oficial"
        )

    @staticmethod
    def slug() -> Field:
        return Field(
            name="slug",
            datatype=DataType.TEXT,
            nullable=False,
            unique=True,
            indexed=True,
            description="Slug SEO"
        )

    @staticmethod
    def created_at() -> Field:
        return Field(
            name="created_at",
            datatype=DataType.DATETIME,
            description="Fecha de creación"
        )

    @staticmethod
    def updated_at() -> Field:
        return Field(
            name="updated_at",
            datatype=DataType.DATETIME,
            description="Fecha de última actualización"
        )

    @staticmethod
    def activo() -> Field:
        return Field(
            name="activo",
            datatype=DataType.BOOLEAN,
            nullable=False,
            default=1,
            description="Registro activo"
        )

    @staticmethod
    def version() -> Field:
        return Field(
            name="version",
            datatype=DataType.TEXT,
            default="1.0",
            description="Versión del registro"
        )

    @staticmethod
    def fuente() -> Field:
        return Field(
            name="fuente",
            datatype=DataType.TEXT,
            description="Fuente de los datos"
        )

    # =====================================================
    # GRUPOS DE CAMPOS
    # =====================================================

    @staticmethod
    def identity() -> list[Field]:
        """
        Campos de identidad comunes.
        """
        return [
            BaseFields.id(),
            BaseFields.codigo_ine(),
            BaseFields.codigo_iso(),
            BaseFields.nombre(),
            BaseFields.slug(),
        ]

    @staticmethod
    def audit() -> list[Field]:
        """
        Campos de auditoría.
        """
        return [
            BaseFields.created_at(),
            BaseFields.updated_at(),
        ]

    @staticmethod
    def lifecycle() -> list[Field]:
        """
        Estado del registro.
        """
        return [
            BaseFields.activo(),
            BaseFields.version(),
            BaseFields.fuente(),
        ]
        @staticmethod
    def identity() -> list[Field]:
        """
        Identidad común de cualquier entidad.
        """
        return [
            BaseFields.id(),
            BaseFields.nombre(),
            BaseFields.slug(),
        ]

    @staticmethod
    def administrative() -> list[Field]:
        """
        Identificadores administrativos oficiales.
        """
        return [
            BaseFields.codigo_ine(),
            BaseFields.codigo_iso(),
        ]