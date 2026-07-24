"""
Prueba de integración del importador SIMA.

Este script descarga la ficha municipal y la página de núcleos,
las procesa mediante el parser y muestra un resumen del resultado.
"""

from __future__ import annotations

from mdta.importers.sima.downloader import SIMADownloader
from mdta.importers.sima.parser import SIMAParser


def main() -> None:
    """
    Ejecuta una prueba completa del importador SIMA.
    """

    municipality_code = "04066"  # Níjar

    print("=" * 70)
    print("PRUEBA DE INTEGRACIÓN DEL IMPORTADOR SIMA")
    print("=" * 70)
    print()

    downloader = SIMADownloader()
    parser = SIMAParser()

    print("Descargando ficha municipal...")
    municipality_html = downloader.get_municipality(
        municipality_code
    )

    print("Descargando núcleos de población...")
    nuclei_html = downloader.get_nuclei(
        municipality_code
    )

    print("Procesando información...")
    print()

    municipality = parser.parse(
        municipality_code=municipality_code,
        municipality_html=municipality_html,
        nuclei_html=nuclei_html,
    )

    print("=" * 70)
    print("MUNICIPIO")
    print("=" * 70)

    print(f"Código : {municipality.code}")
    print(f"Nombre : {municipality.name}")

    print()

    print("=" * 70)
    print("INDICADORES")
    print("=" * 70)

    print(f"Secciones : {len(municipality.sections)}")

    total_indicators = sum(
        len(section.indicators)
        for section in municipality.sections
    )

    print(f"Indicadores : {total_indicators}")

    print()

    for section in municipality.sections:
        print(
            f"  • {section.name}"
            f" ({len(section.indicators)} indicadores)"
        )

    print()

    print("=" * 70)
    print("NÚCLEOS")
    print("=" * 70)

    print(
        f"Número de núcleos: "
        f"{len(municipality.population_entities)}"
    )

    print()

    for entity in municipality.population_entities:

        print(
            f"{entity.official_code:>11} | "
            f"{entity.name:<35} | "
            f"{entity.population_total:>7}"
        )

    print()

    print("=" * 70)
    print("PRUEBA FINALIZADA")
    print("=" * 70)


if __name__ == "__main__":
    main()