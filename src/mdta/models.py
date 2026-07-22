"""
MDTA - Core Models

Modelos fundamentales del Motor de Datos Territorial de Andaltura.

Estos modelos representan la estructura lógica del MDTA y son
independientes del motor de almacenamiento utilizado
(SQLite, PostgreSQL, PostGIS, GeoPackage, etc.).
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from typing import Any

from mdta_types import DataType, GeometryType


# =====================================================================
# FIELD
# =====================================================================

@dataclass(slots=True)
class Field:
    """
    Define un campo reutilizable del Diccionario Maestro MDTA.
    """

    # ---------------------------------------------------------
    # Identificación
    # ---------------------------------------------------------

    name: str
    datatype: DataType

    # ---------------------------------------------------------
    # Restricciones
    # ---------------------------------------------------------

    nullable: bool = True
    unique: bool = False
    indexed: bool = False
    primary_key: bool = False

    default: Any = None

    check: str | None = None

    # ---------------------------------------------------------
    # Longitud / precisión
    # ---------------------------------------------------------

    length: int | None = None
    precision: int | None = None
    scale: int | None = None

    # ---------------------------------------------------------
    # Relaciones
    # ---------------------------------------------------------

    foreign_table: str | None = None
    foreign_field: str | None = None

    foreign_on_delete: str | None = None
    foreign_on_update: str | None = None

    # ---------------------------------------------------------
    # Geometría
    # ---------------------------------------------------------

    geometry_type: GeometryType | None = None
    srid: int | None = None

    # ---------------------------------------------------------
    # Documentación
    # ---------------------------------------------------------

    description: str = ""
    comment: str = ""

    # ---------------------------------------------------------
    # Metadatos
    # ---------------------------------------------------------

    metadata: dict[str, Any] = field(default_factory=dict)

    # ---------------------------------------------------------
    # Propiedades calculadas
    # ---------------------------------------------------------

    @property
    def is_geometry(self) -> bool:
        return self.geometry_type is not None

    @property
    def is_foreign_key(self) -> bool:
        return self.foreign_table is not None

    @property
    def is_numeric(self) -> bool:
        return self.datatype in (
            DataType.INTEGER,
            DataType.FLOAT,
            DataType.DECIMAL,
        )

    # ---------------------------------------------------------
    # Utilidades
    # ---------------------------------------------------------

    def clone(self, **changes) -> "Field":
        """
        Devuelve una copia del campo modificando únicamente
        los atributos indicados.
        """
        return replace(self, **changes)


# =====================================================================
# TABLE
# =====================================================================

@dataclass(slots=True)
class Table:
    """
    Representa una tabla lógica del MDTA.
    """

    name: str
    fields: list[Field]

    description: str = ""

    metadata: dict[str, Any] = field(default_factory=dict)

    # ---------------------------------------------------------

    def add_field(self, field: Field) -> None:
        self.fields.append(field)

    # ---------------------------------------------------------

    def add_fields(self, fields: list[Field]) -> None:
        self.fields.extend(fields)

    # ---------------------------------------------------------

    def remove_field(self, name: str) -> None:
        self.fields = [
            field
            for field in self.fields
            if field.name != name
        ]

    # ---------------------------------------------------------

    def get_field(self, name: str) -> Field | None:
        for field in self.fields:
            if field.name == name:
                return field
        return None

    # ---------------------------------------------------------

    def has_field(self, name: str) -> bool:
        return self.get_field(name) is not None

    # ---------------------------------------------------------

    def primary_key_field(self) -> Field | None:
        for field in self.fields:
            if field.primary_key:
                return field
        return None

    # ---------------------------------------------------------

    @property
    def field_names(self) -> list[str]:
        return [field.name for field in self.fields]

    # ---------------------------------------------------------

    def __iter__(self):
        return iter(self.fields)

    # ---------------------------------------------------------

    def __len__(self):
        return len(self.fields)


# =====================================================================
# SCHEMA
# =====================================================================

@dataclass(slots=True)
class Schema:
    """
    Conjunto de tablas que forman un esquema lógico del MDTA.
    """

    name: str

    tables: list[Table]

    description: str = ""

    metadata: dict[str, Any] = field(default_factory=dict)

    # ---------------------------------------------------------

    def add_table(self, table: Table) -> None:
        self.tables.append(table)

    # ---------------------------------------------------------

    def remove_table(self, name: str) -> None:
        self.tables = [
            table
            for table in self.tables
            if table.name != name
        ]

    # ---------------------------------------------------------

    def get_table(self, name: str) -> Table | None:
        for table in self.tables:
            if table.name == name:
                return table
        return None

    # ---------------------------------------------------------

    def has_table(self, name: str) -> bool:
        return self.get_table(name) is not None

    # ---------------------------------------------------------

    @property
    def table_names(self) -> list[str]:
        return [table.name for table in self.tables]

    # ---------------------------------------------------------

    def __iter__(self):
        return iter(self.tables)

    # ---------------------------------------------------------

    def __len__(self):
        return len(self.tables)