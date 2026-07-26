"""
Construye el catálogo local del Nomenclátor Geográfico de Andalucía.

El programa:

- Descarga páginas del WFS.
- Analiza el GML.
- Inserta las entidades en SQLite.
- Continúa hasta que no haya más registros.

Puede interrumpirse en cualquier momento.
Los registros ya almacenados permanecen en la base de datos.
"""

from __future__ import annotations

import time
from pathlib import Path

from primer.services.wfs import WFSClient
from primer.services.wfs.parser import GMLParser
from primer.storage import CatalogDatabase


WFS_URL = "https://www.ideandalucia.es/wfs-nga-inspire/services"

TYPE_NAME = "gn:NamedPlace"

PAGE_SIZE = 1000

DATABASE = Path("data/catalog/catalog.sqlite")


def main() -> None:

    DATABASE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    client = WFSClient(WFS_URL)

    parser = GMLParser()

    database = CatalogDatabase(DATABASE)

    start_index = database.count()

    print()
    print("=" * 80)
    print("CONSTRUCCIÓN DEL CATÁLOGO")
    print("=" * 80)
    print()

    print(f"Base de datos : {DATABASE}")
    print(f"Inicio        : {start_index}")
    print(f"Tamaño página : {PAGE_SIZE}")
    print()

    total_inserted = 0

    started = time.perf_counter()

    while True:

        print(f"Descargando página desde {start_index}...")

        response = client.get_feature(
            type_name=TYPE_NAME,
            start_index=start_index,
            count=PAGE_SIZE,
        )

        xml = response.text

        features = parser.parse_named_places(xml)

        if not features:

            print()
            print("No quedan más registros.")
            break

        inserted = database.insert_many(features)

        total_inserted += inserted

        start_index += inserted

        elapsed = time.perf_counter() - started

        print(
            f"Insertados: {inserted:5d} | "
            f"Total BD: {database.count():6d} | "
            f"Tiempo: {elapsed:8.1f} s"
        )

    print()
    print("=" * 80)
    print("FINALIZADO")
    print("=" * 80)
    print()

    print(f"Registros nuevos : {total_inserted}")
    print(f"Registros totales: {database.count()}")

    database.close()
    client.close()


if __name__ == "__main__":
    main()