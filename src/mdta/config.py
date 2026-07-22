"""
=========================================================
Andaltura Data Engine
Archivo: config.py
Descripción:
    Configuración global del proyecto.

Autor: Andaltura
=========================================================
"""

from pathlib import Path


# =========================================================
# INFORMACIÓN DEL PROYECTO
# =========================================================

PROJECT_NAME = "Andaltura Data Engine"
VERSION = "1.0.0"

# =========================================================
# RUTAS PRINCIPALES
# =========================================================

# Carpeta raíz del proyecto
ROOT_DIR = Path(__file__).resolve().parent.parent

# Carpetas principales
DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
SQLITE_DIR = DATA_DIR / "sqlite"
EXPORT_DIR = DATA_DIR / "export"

LOG_DIR = ROOT_DIR / "logs"

SRC_DIR = ROOT_DIR / "src"

# =========================================================
# BASE DE DATOS
# =========================================================

DATABASE_NAME = "andaltura.db"
DATABASE_PATH = SQLITE_DIR / DATABASE_NAME

# =========================================================
# EXPORTACIONES
# =========================================================

CSV_EXPORT = EXPORT_DIR / "csv"
EXCEL_EXPORT = EXPORT_DIR / "excel"
GEOPACKAGE_EXPORT = EXPORT_DIR / "gpkg"
GEOJSON_EXPORT = EXPORT_DIR / "geojson"

# =========================================================
# LOGS
# =========================================================

LOG_FILE = LOG_DIR / "andaltura.log"

# =========================================================
# CODIFICACIÓN
# =========================================================

DEFAULT_ENCODING = "utf-8"

# =========================================================
# CREAR CARPETAS SI NO EXISTEN
# =========================================================

FOLDERS = [
    DATA_DIR,
    RAW_DIR,
    SQLITE_DIR,
    EXPORT_DIR,
    CSV_EXPORT,
    EXCEL_EXPORT,
    GEOPACKAGE_EXPORT,
    GEOJSON_EXPORT,
    LOG_DIR,
]

for folder in FOLDERS:
    folder.mkdir(parents=True, exist_ok=True)