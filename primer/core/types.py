"""
Tipos de datos universales de Primer.

Representan los tipos lógicos utilizados por cualquier
origen de datos.
"""

from __future__ import annotations

from enum import Enum


class DataType(str, Enum):
    """
    Tipos de datos universales.
    """

    UNKNOWN = "unknown"

    STRING = "string"

    INTEGER = "integer"

    FLOAT = "float"

    DECIMAL = "decimal"

    BOOLEAN = "boolean"

    DATE = "date"

    TIME = "time"

    DATETIME = "datetime"

    UUID = "uuid"

    URI = "uri"

    EMAIL = "email"

    JSON = "json"

    XML = "xml"

    BINARY = "binary"

    GEOMETRY = "geometry"

    ENUM = "enum"