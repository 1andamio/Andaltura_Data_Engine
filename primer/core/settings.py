"""
Configuración global del framework Primer.

Centraliza los parámetros de configuración compartidos por todos los
componentes del framework.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class Settings:
    """
    Configuración global del framework.
    """

    # ------------------------------------------------------------------
    # Identidad
    # ------------------------------------------------------------------

    framework_name: str = "Primer"

    framework_version: str = "0.1.0"

    user_agent: str = "Primer/0.1.0"

    # ------------------------------------------------------------------
    # Red
    # ------------------------------------------------------------------

    default_timeout: int = 30

    max_retries: int = 3

    retry_delay: float = 2.0

    verify_ssl: bool = True

    # ------------------------------------------------------------------
    # Descargas
    # ------------------------------------------------------------------

    download_chunk_size: int = 8192

    overwrite_files: bool = False

    # ------------------------------------------------------------------
    # Directorios
    # ------------------------------------------------------------------

    root_directory: Path = Path("primer")

    data_directory: Path = Path("primer/data")

    raw_directory: Path = Path("primer/data/raw")

    cache_directory: Path = Path("primer/data/cache")

    staging_directory: Path = Path("primer/data/staging")

    processed_directory: Path = Path("primer/data/processed")

    log_directory: Path = Path("primer/logs")

    temporary_directory: Path = Path("primer/tmp")

    # ------------------------------------------------------------------
    # Caché
    # ------------------------------------------------------------------

    use_cache: bool = True

    cache_expiration_hours: int = 24

    # ------------------------------------------------------------------
    # Registro
    # ------------------------------------------------------------------

    enable_logging: bool = True

    log_level: str = "INFO"

    # ------------------------------------------------------------------
    # HTTP
    # ------------------------------------------------------------------

    headers: dict[str, str] = field(default_factory=dict)

    # ------------------------------------------------------------------
    # Utilidades
    # ------------------------------------------------------------------

    def ensure_directories(self) -> None:
        """
        Crea automáticamente la estructura de directorios del framework.
        """

        directories = (
            self.root_directory,
            self.data_directory,
            self.raw_directory,
            self.cache_directory,
            self.staging_directory,
            self.processed_directory,
            self.log_directory,
            self.temporary_directory,
        )

        for directory in directories:
            directory.mkdir(
                parents=True,
                exist_ok=True,
            )


#
# Configuración global del framework.
#

settings = Settings()