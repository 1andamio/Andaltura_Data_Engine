"""
Diagnóstico de estabilidad de la paginación WFS.

Muestra las primeras entidades completas de dos peticiones
idénticas para comprobar si el servidor devuelve realmente
resultados diferentes.
"""

from __future__ import annotations

from primer.services.wfs import WFSClient
from primer.services.wfs.parser import GMLParser


WFS_URL = "https://www.ideandalucia.es/wfs-nga-inspire/services"

TYPE_NAME = "gn:NamedPlace"

START_INDEX = 232855
COUNT = 20


def descargar(client, parser, titulo):

    print()
    print("=" * 80)
    print(titulo)
    print("=" * 80)

    response = client.get_feature(
        type_name=TYPE_NAME,
        start_index=START_INDEX,
        count=COUNT,
    )

    print()
    print(response.url)
    print()

    features = parser.parse_named_places(response.text)

    print(f"Entidades recibidas: {len(features)}")
    print()

    for i, feature in enumerate(features[:10], start=1):

        print(f"[{i}]")
        print(f"gml:id    : {feature.get('gml_id')}")
        print(f"local_id  : {feature.get('local_id')}")
        print(f"namespace : {feature.get('namespace')}")
        print(f"name      : {feature.get('name')}")
        print("-" * 60)

    return features


def main():

    client = WFSClient(WFS_URL)
    parser = GMLParser()

    f1 = descargar(client, parser, "PRIMERA PETICIÓN")

    f2 = descargar(client, parser, "SEGUNDA PETICIÓN")

    client.close()


if __name__ == "__main__":
    main()