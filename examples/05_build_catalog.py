"""
Construye el catálogo local del Nomenclátor Geográfico de Andalucía.

Versión de diagnóstico.

Comprueba:

- Entidades recibidas.
- Entidades insertadas.
- Primer y último localId.
- Repetición de páginas.
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
    print("CONSTRUCCIÓN DEL CATÁLOGO (MODO DIAGNÓSTICO)")
    print("=" * 80)
    print()

    print(f"Base de datos : {DATABASE}")
    print(f"Inicio        : {start_index}")
    print(f"Tamaño página : {PAGE_SIZE}")
    print()

    total_inserted = 0

    started = time.perf_counter()

    # Para detectar páginas repetidas
    paginas_vistas = set()

    while True:

        print()
        print("-" * 80)
        print(f"Descargando página desde startIndex = {start_index}")

        response = client.get_feature(
            type_name=TYPE_NAME,
            start_index=start_index,
            count=PAGE_SIZE,
        )

        xml = response.text

        features = parser.parse_named_places(xml)

        print(f"Entidades recibidas del WFS : {len(features)}")

        if not features:

            print()
            print("No quedan más registros.")
            break

        primer_id = features[0]["local_id"]
        ultimo_id = features[-1]["local_id"]

        print(f"Primer localId             : {primer_id}")
        print(f"Último localId             : {ultimo_id}")

        firma = (primer_id, ultimo_id)

        if firma in paginas_vistas:

            print()
            print("=" * 80)
            print("¡¡¡ PÁGINA REPETIDA DETECTADA !!!")
            print("=" * 80)
            print()
            print("El WFS ha devuelto exactamente el mismo rango de entidades.")
            print(f"Primer localId : {primer_id}")
            print(f"Último localId : {ultimo_id}")
            print()
            print("La descarga se detiene para evitar un bucle infinito.")
            break

        paginas_vistas.add(firma)

        inserted = database.insert_many(features)

        print(f"Entidades insertadas SQLite : {inserted}")

        if inserted != len(features):

            print()
            print("=" * 80)
            print("¡¡¡ DIFERENCIA DETECTADA !!!")
            print("=" * 80)
            print(f"Recibidas : {len(features)}")
            print(f"Insertadas: {inserted}")
            print()

        total_inserted += inserted

        start_index += inserted

        print(f"Siguiente startIndex        : {start_index}")

        elapsed = time.perf_counter() - started

        print(
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