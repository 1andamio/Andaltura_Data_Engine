"""
Utilidades para el cálculo de checksums.

Proporciona funciones para calcular la huella digital de archivos
utilizando distintos algoritmos criptográficos.
"""

from __future__ import annotations

import hashlib
from pathlib import Path


class Checksum:
    """
    Utilidades para el cálculo de checksums.
    """

    BUFFER_SIZE = 1024 * 1024  # 1 MB

    @classmethod
    def calculate(
        cls,
        file: str | Path,
        algorithm: str = "sha256",
    ) -> str:
        """
        Calcula el checksum de un archivo.

        Parameters
        ----------
        file:
            Ruta del archivo.

        algorithm:
            Algoritmo criptográfico.

        Returns
        -------
        str
            Checksum hexadecimal.
        """

        path = Path(file)

        hasher = hashlib.new(algorithm)

        with path.open("rb") as stream:

            while chunk := stream.read(cls.BUFFER_SIZE):

                hasher.update(chunk)

        return hasher.hexdigest()

    @classmethod
    def md5(
        cls,
        file: str | Path,
    ) -> str:
        """
        Calcula el checksum MD5.
        """

        return cls.calculate(file, "md5")

    @classmethod
    def sha1(
        cls,
        file: str | Path,
    ) -> str:
        """
        Calcula el checksum SHA-1.
        """

        return cls.calculate(file, "sha1")

    @classmethod
    def sha256(
        cls,
        file: str | Path,
    ) -> str:
        """
        Calcula el checksum SHA-256.
        """

        return cls.calculate(file, "sha256")

    @classmethod
    def verify(
        cls,
        file: str | Path,
        checksum: str,
        algorithm: str = "sha256",
    ) -> bool:
        """
        Comprueba si el checksum coincide.
        """

        return cls.calculate(file, algorithm) == checksum