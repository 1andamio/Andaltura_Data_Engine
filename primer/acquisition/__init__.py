"""
Subsistema de adquisición de datos.

Este paquete proporciona los componentes necesarios para descargar,
verificar, extraer y gestionar archivos procedentes de fuentes
externas.

Responsabilidades:

- Descarga de archivos.
- Verificación de integridad.
- Cálculo de checksums.
- Extracción de archivos comprimidos.
- Gestión del resultado de las descargas.
"""

from .download_result import DownloadResult

__all__ = [
    "DownloadResult",
]