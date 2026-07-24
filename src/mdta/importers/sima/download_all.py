"""
Descarga completa del SIMA.

Punto de entrada oficial del importador.

Ejemplo:

    python -m mdta.importers.sima.download_all

También puede ejecutarse indicando otras rutas:

    python -m mdta.importers.sima.download_all \
        --excel data/input/smex99.xlsx \
        --output data/raw/sima
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .crawler import SIMACrawler


# ---------------------------------------------------------
# Argumentos
# ---------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(
        prog="mdta.importers.sima.download_all",
        description="Descarga completa del SIMA.",
    )

    parser.add_argument(
        "--excel",
        type=Path,
        default=Path("data/input/smex99.xlsx"),
        help="Archivo Excel con el catálogo de municipios.",
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/raw/sima"),
        help="Directorio donde se guardarán los HTML.",
    )

    return parser


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

def main() -> int:

    parser = build_parser()

    args = parser.parse_args()

    if not args.excel.exists():

        print()
        print("ERROR")
        print("-" * 60)
        print(f"No existe el archivo Excel:")
        print(args.excel)
        print()

        return 1

    print()
    print("=" * 70)
    print("MDTA · IMPORTADOR SIMA")
    print("=" * 70)
    print(f"Excel : {args.excel}")
    print(f"Salida: {args.output}")
    print()

    crawler = SIMACrawler(
        excel_file=args.excel,
        output_directory=args.output,
    )

    crawler.run()

    print()
    print("=" * 70)
    print("Proceso finalizado.")
    print("=" * 70)
    print()

    return 0


# ---------------------------------------------------------

if __name__ == "__main__":
    sys.exit(main())