"""
MDTA - Diccionario Maestro
Campos Geográficos

Campos reutilizables relacionados con la localización, geometría
y características físicas del territorio.
"""

from models import Field
from mdta_types import DataType, GeometryType


class Geography:

    # ======================================================
    # COORDENADAS
    # ======================================================

    LATITUD = Field(
        name="latitud",
        datatype=DataType.REAL,
        description="Latitud en grados decimales."
    )

    LONGITUD = Field(
        name="longitud",
        datatype=DataType.REAL,
        description="Longitud en grados decimales."
    )

    X = Field(
        name="x",
        datatype=DataType.REAL,
        description="Coordenada X."
    )

    Y = Field(
        name="y",
        datatype=DataType.REAL,
        description="Coordenada Y."
    )

    Z = Field(
        name="z",
        datatype=DataType.REAL,
        description="Coordenada Z o altitud."
    )

    SRID = Field(
        name="srid",
        datatype=DataType.INTEGER,
        default=4326,
        description="Sistema de referencia espacial."
    )

    # ======================================================
    # GEOMETRÍA
    # ======================================================

    GEOMETRY = Field(
        name="geometry",
        datatype=DataType.GEOMETRY,
        geometry_type=GeometryType.GEOMETRYCOLLECTION,
        description="Geometría de la entidad."
    )

    POINT = Field(
        name="geometry",
        datatype=DataType.GEOMETRY,
        geometry_type=GeometryType.POINT,
        description="Geometría puntual."
    )

    LINESTRING = Field(
        name="geometry",
        datatype=DataType.GEOMETRY,
        geometry_type=GeometryType.LINESTRING,
        description="Geometría lineal."
    )

    POLYGON = Field(
        name="geometry",
        datatype=DataType.GEOMETRY,
        geometry_type=GeometryType.POLYGON,
        description="Geometría poligonal."
    )

    MULTIPOLYGON = Field(
        name="geometry",
        datatype=DataType.GEOMETRY,
        geometry_type=GeometryType.MULTIPOLYGON,
        description="Geometría multipoligonal."
    )

    # ======================================================
    # DIMENSIONES
    # ======================================================

    SUPERFICIE_KM2 = Field(
        name="superficie_km2",
        datatype=DataType.REAL,
        description="Superficie en kilómetros cuadrados."
    )

    PERIMETRO_KM = Field(
        name="perimetro_km",
        datatype=DataType.REAL,
        description="Perímetro en kilómetros."
    )

    LONGITUD_KM = Field(
        name="longitud_km",
        datatype=DataType.REAL,
        description="Longitud en kilómetros."
    )

    ANCHURA_MEDIA_M = Field(
        name="anchura_media_m",
        datatype=DataType.REAL,
        description="Anchura media en metros."
    )

    # ======================================================
    # ALTITUD
    # ======================================================

    ALTITUD_MIN = Field(
        name="altitud_min",
        datatype=DataType.REAL,
        description="Altitud mínima."
    )

    ALTITUD_MAX = Field(
        name="altitud_max",
        datatype=DataType.REAL,
        description="Altitud máxima."
    )

    ALTITUD_MEDIA = Field(
        name="altitud_media",
        datatype=DataType.REAL,
        description="Altitud media."
    )

    DESNIVEL = Field(
        name="desnivel",
        datatype=DataType.REAL,
        description="Desnivel total."
    )

    PENDIENTE_MEDIA = Field(
        name="pendiente_media",
        datatype=DataType.REAL,
        description="Pendiente media."
    )

    ORIENTACION = Field(
        name="orientacion",
        datatype=DataType.TEXT,
        description="Orientación predominante."
    )

    # ======================================================
    # CENTROIDE
    # ======================================================

    CENTROIDE_LAT = Field(
        name="centroide_lat",
        datatype=DataType.REAL,
        description="Latitud del centroide."
    )

    CENTROIDE_LON = Field(
        name="centroide_lon",
        datatype=DataType.REAL,
        description="Longitud del centroide."
    )

    BBOX_MIN_X = Field(
        name="bbox_min_x",
        datatype=DataType.REAL,
        description="Bounding Box mínimo X."
    )

    BBOX_MIN_Y = Field(
        name="bbox_min_y",
        datatype=DataType.REAL,
        description="Bounding Box mínimo Y."
    )

    BBOX_MAX_X = Field(
        name="bbox_max_x",
        datatype=DataType.REAL,
        description="Bounding Box máximo X."
    )

    BBOX_MAX_Y = Field(
        name="bbox_max_y",
        datatype=DataType.REAL,
        description="Bounding Box máximo Y."
    )