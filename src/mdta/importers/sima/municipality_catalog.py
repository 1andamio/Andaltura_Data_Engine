"""
Catálogo de municipios del SIMA.

Responsabilidades
-----------------
- Leer el fichero Excel oficial del SIMA.
- Devolver la lista de municipios disponibles.

No descarga datos.
No parsea HTML.
No conoce el downloader.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass(slots=True)
class Municipality:
    """
    Municipio disponible en el SIMA.
    """

    code: str
    name: str


class MunicipalityCatalog:
    """
    Lee el catálogo oficial de municipios del SIMA.
    """

    def __init__(self, excel_file: str | Path):

        self.excel_file = Path(excel_file)

        if not self.excel_file.exists():
            raise FileNotFoundError(
                f"No existe el fichero: {self.excel_file}"
            )

    def load(self) -> list[Municipality]:
        """
        Devuelve todos los municipios del catálogo.
        """

        dataframe = pd.read_excel(
            self.excel_file,
            dtype=str,
        )

        # Normalizamos nombres de columnas
        dataframe.columns = [
            column.strip()
            for column in dataframe.columns
        ]

        # Estas dos columnas son las que esperamos encontrar
        code_column = "CodMun"
        name_column = "Municipio"

        if code_column not in dataframe.columns:
            raise ValueError(
                f"No existe la columna '{code_column}'."
            )

        if name_column not in dataframe.columns:
            raise ValueError(
                f"No existe la columna '{name_column}'."
            )

        municipalities: list[Municipality] = []

        for _, row in dataframe.iterrows():

            code = str(row[code_column]).zfill(5)
            name = str(row[name_column]).strip()

            municipalities.append(
                Municipality(
                    code=code,
                    name=name,
                )
            )

        return municipalities