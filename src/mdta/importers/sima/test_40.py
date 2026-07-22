"""
Importa un conjunto de municipios desde el SIMA para verificar
el funcionamiento del importador.
"""

from __future__ import annotations

from pathlib import Path

from mdta.importers.sima.service import SIMAImportService


MUNICIPALITIES = [
    "04003",  # Adra
    "04013",  # El Ejido
    "04032",  # Huércal-Overa
    "04049",  # Roquetas de Mar
    "04066",  # Níjar

    "11004",  # Arcos de la Frontera
    "11012",  # Jerez de la Frontera
    "11022",  # Tarifa
    "11027",  # Vejer de la Frontera

    "14005",  # Baena
]


def main() -> None:

    service = SIMAImportService()

    for code in MUNICIPALITIES:

        print(f"\nImportando {code}...")

        try:

            municipality = service.import_municipality(code)

            output = (
                Path("data")
                / "sima"
                / f"{code}.json"
            )

            service.save_json(
                municipality,
                output,
            )

            print(f"✓ {municipality.name}")

        except Exception as exc:

            print(f"✗ ERROR: {exc}")

    print("\nFinalizado.")


if __name__ == "__main__":
    main()