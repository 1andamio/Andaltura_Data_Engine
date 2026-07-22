"""
Importa un único municipio desde el SIMA.
"""

from __future__ import annotations

import sys
from pathlib import Path

from mdta.importers.sima.service import SIMAImportService


def main() -> None:

    if len(sys.argv) != 2:

        print(
            "Uso:\n"
            "python -m mdta.importers.sima.import_one 04066"
        )

        return

    municipality_code = sys.argv[1]

    print(f"\nImportando {municipality_code}...\n")

    service = SIMAImportService()

    municipality = service.import_municipality(
        municipality_code
    )

    output = (
        Path("data")
        / "sima"
        / f"{municipality_code}.json"
    )

    service.save_json(
        municipality,
        output,
    )

    print()
    print("Municipio :", municipality.name)
    print("Secciones :", len(municipality.sections))
    print("JSON      :", output.resolve())
    print()
    print("Finalizado.")


if __name__ == "__main__":
    main()