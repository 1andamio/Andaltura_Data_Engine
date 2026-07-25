"""
Gestor de descargas.

Coordina la adquisición de datasets utilizando DownloadClient.
"""

from __future__ import annotations

from pathlib import Path

from primer.datasets.dataset import Dataset
from primer.datasets.dataset_file import DatasetFile
from primer.types.dataset_status import DatasetStatus

from .checksum import Checksum
from .download_client import DownloadClient
from .download_result import DownloadResult


class DownloadManager:
    """
    Gestor de descargas de datasets.
    """

    def __init__(
        self,
        download_directory: str | Path = "data/raw",
        *,
        overwrite: bool = False,
        verify_checksum: bool = True,
        client: DownloadClient | None = None,
    ) -> None:

        self._download_directory = Path(download_directory)

        self._overwrite = overwrite

        self._verify_checksum = verify_checksum

        self._client = client or DownloadClient()

    @property
    def download_directory(self) -> Path:
        """
        Directorio donde se almacenan las descargas.
        """

        return self._download_directory

    def download(
        self,
        dataset: Dataset,
    ) -> DownloadResult:
        """
        Descarga un dataset.
        """

        if not dataset.url:
            return DownloadResult(
                success=False,
                message="El Dataset no tiene URL."
            )

        destination_dir = (
            self._download_directory /
            dataset.id
        )

        destination_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        filename = Path(dataset.url).name

        destination = destination_dir / filename

        if destination.exists() and not self._overwrite:

            return DownloadResult(
                success=True,
                file=destination,
                size=destination.stat().st_size,
                checksum=Checksum.sha256(destination),
                message="El archivo ya existe."
            )

        try:

            dataset.status = DatasetStatus.DOWNLOADING

            file = self._client.download(
                dataset.url,
                destination,
            )

            checksum = None

            if self._verify_checksum:

                checksum = Checksum.sha256(file)

            dataset_file = DatasetFile(
                name=file.name,
                path=file,
                size=file.stat().st_size,
                checksum=checksum,
            )

            dataset.add_file(dataset_file)

            dataset.mark_downloaded()

            return DownloadResult(
                success=True,
                file=file,
                size=dataset_file.size,
                checksum=checksum,
                message="Descarga completada."
            )

        except Exception as exc:

            dataset.mark_failed()

            return DownloadResult(
                success=False,
                message=str(exc),
            )

    def exists(
        self,
        dataset: Dataset,
    ) -> bool:
        """
        Comprueba si el dataset ya existe.
        """

        if not dataset.url:

            return False

        filename = Path(dataset.url).name

        path = (
            self._download_directory /
            dataset.id /
            filename
        )

        return path.exists()

    def remove(
        self,
        dataset: Dataset,
    ) -> None:
        """
        Elimina el archivo descargado.
        """

        if not dataset.url:
            return

        filename = Path(dataset.url).name

        path = (
            self._download_directory /
            dataset.id /
            filename
        )

        if path.exists():

            path.unlink()

    def close(self) -> None:
        """
        Libera recursos.
        """

        self._client.close()

    def __enter__(self) -> "DownloadManager":

        return self

    def __exit__(
        self,
        exc_type,
        exc,
        tb,
    ) -> None:

        self.close()