"""
Catálogo oficial de municipios del SIMA.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass(slots=True)
class Municipality:

    province: str
    code: str
    name: str
    iaph_url: str


class MunicipalityCatalog:

    def __init__(self, excel_file: str | Path):

        self.excel_file = Path(excel_file)

    def load(self) -> list[Municipality]:

        df = pd.read_excel(
            self.excel_file,
            header=2,
            dtype=str,
        )

        municipalities = []

        for _, row in df.iterrows():

            code = str(row["CodMun"]).zfill(5)

            municipalities.append(
                Municipality(
                    province=str(row["Provincia"]).strip(),
                    code=code,
                    name=str(row["Municipio"]).strip(),
                    iaph_url=str(row["Url. 2025"]).strip(),
                )
            )

        municipalities.sort(
            key=lambda m: m.code
        )

        return municipalities