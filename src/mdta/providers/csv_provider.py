"""
MDTA - CSV Provider

Proveedor genérico para leer archivos CSV.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterator


class CSVProvider:
    """
    Lee un archivo CSV y devuelve cada registro como un diccionario.
    """

    def __init__(
        self,
        filename: str | Path,
        *,
        encoding: str = "utf-8",
        delimiter: str = ",",
    ):

        self.filename = Path(filename)

        self.encoding = encoding

        self.delimiter = delimiter

    # ---------------------------------------------------------

    def exists(self) -> bool:

        return self.filename.exists()

    # ---------------------------------------------------------

    def headers(self) -> list[str]:

        with open(
            self.filename,
            encoding=self.encoding,
            newline="",
        ) as file:

            reader = csv.reader(
                file,
                delimiter=self.delimiter,
            )

            return next(reader)

    # ---------------------------------------------------------

    def rows(self) -> Iterator[dict[str, str]]:

        with open(
            self.filename,
            encoding=self.encoding,
            newline="",
        ) as file:

            reader = csv.DictReader(
                file,
                delimiter=self.delimiter,
            )

            yield from reader

    # ---------------------------------------------------------

    def __iter__(self):

        return self.rows()

    # ---------------------------------------------------------

    def __len__(self):

        with open(
            self.filename,
            encoding=self.encoding,
            newline="",
        ) as file:

            return sum(1 for _ in file) - 1