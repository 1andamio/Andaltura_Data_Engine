"""
Crawler del SIMA.

Recorre el catálogo oficial de municipios y descarga la información
HTML del SIMA, manteniendo un manifest para poder reanudar el proceso
en cualquier momento.
"""

from __future__ import annotations

import time
from pathlib import Path

from .catalog import MunicipalityCatalog
from .downloader import SIMADownloader
from .manifest import Manifest


class SIMACrawler:

    def __init__(
        self,
        excel_file: str | Path,
        output_directory: str | Path = "data/raw/sima",
    ) -> None:

        self.output_directory = Path(output_directory)

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.catalog = MunicipalityCatalog(excel_file)

        self.downloader = SIMADownloader()

        self.manifest = Manifest(
            manifest_file=self.output_directory / "manifest.json",
            data_directory=self.output_directory,
        )

    # ---------------------------------------------------------

    def run(self) -> None:

        municipalities = self.catalog.load()

        total = len(municipalities)

        print()
        print("=" * 70)
        print("IMPORTADOR SIMA")
        print("=" * 70)
        print(f"Municipios : {total}")
        print()

        for index, municipality in enumerate(
            municipalities,
            start=1,
        ):

            code = municipality.code

            self.manifest.start(
                code=municipality.code,
                name=municipality.name,
                province=municipality.province,
            )

            municipality_folder = self.output_directory / code

            ficha_file = municipality_folder / "ficha.html"
            nucleos_file = municipality_folder / "nucleos.html"

            # -------------------------------------------------
            # Verificar que el manifest coincide con el disco
            # -------------------------------------------------

            if self.manifest.is_completed(code):

                if ficha_file.exists() and nucleos_file.exists():

                    print(
                        f"[{index:03}/{total}] "
                        f"{code} "
                        f"{municipality.name} "
                        f"(ya descargado)"
                    )

                    continue

                print(
                    f"[{index:03}/{total}] "
                    f"{code} "
                    f"{municipality.name}"
                )

                print("    Manifest correcto pero faltan archivos.")
                print("    Se volverá a descargar.")

            else:

                print(
                    f"[{index:03}/{total}] "
                    f"{code} "
                    f"{municipality.name}"
                )

            start_time = time.perf_counter()

            self.manifest.begin(code)

            municipality_folder.mkdir(
                parents=True,
                exist_ok=True,
            )

            try:

                # -------------------------------------------------
                # Descarga ficha
                # -------------------------------------------------

                ficha = self.downloader.get_municipality(code)

                ficha_file.write_text(
                    ficha,
                    encoding="utf-8",
                )

                self.manifest.set_download(
                    code=code,
                    document="ficha",
                    file=str(
                        ficha_file.relative_to(
                            self.output_directory
                        )
                    ),
                    size=ficha_file.stat().st_size,
                )

                # -------------------------------------------------
                # Descarga núcleos
                # -------------------------------------------------

                nucleos = self.downloader.get_nuclei(code)

                nucleos_file.write_text(
                    nucleos,
                    encoding="utf-8",
                )

                self.manifest.set_download(
                    code=code,
                    document="nucleos",
                    file=str(
                        nucleos_file.relative_to(
                            self.output_directory
                        )
                    ),
                    size=nucleos_file.stat().st_size,
                )

                elapsed = time.perf_counter() - start_time

                self.manifest.complete(
                    code,
                    elapsed,
                )

                print(
                    f"    ✓ OK ({elapsed:.2f} s)"
                )

            except Exception as exc:

                self.manifest.fail(
                    code,
                    str(exc),
                )

                print(
                    f"    ✗ ERROR: {exc}"
                )

            finally:

                # Guardamos SIEMPRE el manifest,
                # incluso si ocurre un error.

                self.manifest.save()

        self._print_summary()

    # ---------------------------------------------------------

    def _print_summary(self) -> None:

        summary = self.manifest.summary

        print()
        print("=" * 70)
        print("RESUMEN")
        print("=" * 70)

        print(f"Total       : {summary['total']}")
        print(f"Completados : {summary['completed']}")
        print(f"Fallidos    : {summary['failed']}")
        print(f"Pendientes  : {summary['pending']}")
        print(f"En proceso  : {summary['running']}")

        print("=" * 70)