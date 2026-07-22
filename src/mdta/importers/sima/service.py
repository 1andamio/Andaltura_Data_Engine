"""
Servicio de importación del Sistema de Información Multiterritorial
de Andalucía (SIMA).
"""

from __future__ import annotations

from pathlib import Path

from mdta.importers.exporter import Exporter
from mdta.importers.sima.downloader import SIMADownloader
from mdta.importers.sima.models import MunicipalityData
from mdta.importers.sima.parser import SIMAParser


class SIMAImportService:
    """
    Servicio encargado de importar municipios desde el SIMA.

    Centraliza toda la lógica de descarga, análisis y exportación
    para que pueda reutilizarse desde la línea de comandos,
    validadores y futuros procesos masivos.
    """

    def __init__(self) -> None:
        self._downloader = SIMADownloader()
        self._parser = SIMAParser()

    def import_municipality(
        self,
        municipality_code: str,
    ) -> MunicipalityData:
        """
        Descarga y procesa un municipio.

        Parameters
        ----------
        municipality_code
            Código INE del municipio.

        Returns
        -------
        MunicipalityData
            Municipio completamente procesado.
        """

        html = self._downloader.get_municipality(
            municipality_code
        )

        municipality = self._parser.parse(
            municipality_code,
            html,
        )

        return municipality

    def save_json(
        self,
        municipality: MunicipalityData,
        output: str | Path,
    ) -> Path:
        """
        Exporta un municipio a JSON.
        """

        return Exporter.save_json(
            municipality,
            output,
        )