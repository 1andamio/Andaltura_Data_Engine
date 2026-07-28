"""
Prueba de estabilidad del parámetro sortBy utilizando un atributo simple.

Compara dos peticiones idénticas usando:
    sortBy=beginLifespanVersion
"""

from __future__ import annotations

from primer.services.wfs import WFSClient
from primer.services.wfs.parser import GMLParser

WFS_URL = "https://www.ideandalucia.es/wfs-nga-inspire/services"

TYPE_NAME = "gn:NamedPlace"

START_INDEX = 0
COUNT = 20

SORT_BY = "beginLifespanVersion"


def descargar(client, parser, titulo):

    print()
    print("=" * 80)
    print(titulo)
    print("=" * 80)

    response = client.get_feature(
        type_name=TYPE_NAME,
        start_index=START_INDEX,
        count=COUNT,
        sortBy=SORT_BY,
    )

    print()
    print("URL:")
    print(response.url)
    print()

    print("STATUS:", response.status_code)
    print()

    features = parser.parse_named_places(response.text)

    print(f"Entidades recibidas : {len(features)}")

    ids = []

    for feature in features:

        ids.append(feature["local_id"])

        print(
            f"{feature['local_id']:>7} | "
            f"{feature['name']}"
        )

    return ids


def main():

    client = WFSClient(WFS_URL)
    parser = GMLParser()

    ids1 = descargar(
        client,
        parser,
        "PRIMERA PETICIÓN",
    )

    ids2 = descargar(
        client,
        parser,
        "SEGUNDA PETICIÓN",
    )

    print()
    print("=" * 80)

    if ids1 == ids2:
        print("✅ RESULTADO: SORTBY ES ESTABLE")
    else:
        print("❌ RESULTADO: SORTBY NO ES ESTABLE")

        comunes = set(ids1) & set(ids2)

        print()
        print(f"IDs comunes     : {len(comunes)}")
        print(f"Solo petición 1 : {len(set(ids1)-comunes)}")
        print(f"Solo petición 2 : {len(set(ids2)-comunes)}")

    client.close()


if __name__ == "__main__":
    main()