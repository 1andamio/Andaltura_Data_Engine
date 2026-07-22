"""
MDTA - Master Data Types

Define los tipos de datos soportados por el Modelo de Datos Territorial
de Andaltura.

Estos tipos son independientes del motor de almacenamiento
(SQLite, PostgreSQL, GeoPackage, etc.).
"""

from enum import Enum


class DataType(str, Enum):
    """Tipos de datos básicos."""

    UNKNOWN = "UNKNOWN"
    INTEGER = "INTEGER"
    FLOAT = "FLOAT"
    DECIMAL = "DECIMAL"
    TEXT = "TEXT"
    BOOLEAN = "BOOLEAN"
    DATE = "DATE"
    TIME = "TIME"
    DATETIME = "DATETIME"
    UUID = "UUID"
    ENUM = "ENUM"
    JSON = "JSON"
    BLOB = "BLOB"
    GEOMETRY = "GEOMETRY"


class GeometryType(str, Enum):
    """Tipos geométricos."""

    POINT = "POINT"
    MULTIPOINT = "MULTIPOINT"

    LINESTRING = "LINESTRING"
    MULTILINESTRING = "MULTILINESTRING"

    POLYGON = "POLYGON"
    MULTIPOLYGON = "MULTIPOLYGON"

    GEOMETRYCOLLECTION = "GEOMETRYCOLLECTION"


class SRID(int, Enum):
    """Sistemas de referencia más habituales."""

    WGS84 = 4326
    WEB_MERCATOR = 3857
    ETRS89_30N = 25830
    ETRS89_29N = 25829
    ETRS89_31N = 25831