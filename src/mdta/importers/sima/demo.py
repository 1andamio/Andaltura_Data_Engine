"""
Programa de prueba del importador SIMA.
"""

from mdta.importers.sima.downloader import SIMADownloader
from mdta.importers.sima.parser import SIMAParser


def main():

    municipality_code = "04066"

    downloader = SIMADownloader()

    html = downloader.get_municipality(
        municipality_code
    )

    parser = SIMAParser()

    municipality = parser.parse(
        municipality_code,
        html,
    )

    print()
    print("=" * 80)
    print("MUNICIPIO")
    print("=" * 80)

    print("Código :", municipality.code)
    print("Nombre :", municipality.name)

    print()

    print("=" * 80)
    print("SECCIONES")
    print("=" * 80)

    for section in municipality.sections:

        print()
        print(section.name)
        print("-" * len(section.name))

        for indicator in section.indicators:

            print(
                f"{indicator.name}"
                f" | unidad={indicator.unit}"
                f" | año={indicator.year}"
                f" | valor={indicator.value}"
            )


if __name__ == "__main__":
    main()