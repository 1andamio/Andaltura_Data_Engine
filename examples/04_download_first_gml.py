"""
Descarga la primera entidad del Nomenclátor Geográfico de Andalucía
en formato GML (INSPIRE).

No interpreta nada.
Simplemente descarga el XML real y lo guarda en disco.
"""

from pathlib import Path

from primer.services.wfs import WFSClient


OUTPUT = Path("data/debug")
OUTPUT.mkdir(parents=True, exist_ok=True)


def main():

    client = WFSClient(
        "https://www.ideandalucia.es/wfs-nga-inspire/services"
    )

    print()
    print("=" * 80)
    print("DESCARGANDO PRIMERA ENTIDAD GML")
    print("=" * 80)
    print()

    response = client.request(
        request="GetFeature",
        typeNames="gn:NamedPlace",
        startIndex=0,
        count=1,
    )

    print("Status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print()

    xml = response.text

    fichero = OUTPUT / "first_entity.gml"

    fichero.write_text(
        xml,
        encoding="utf-8",
    )

    print(f"GML guardado en: {fichero}")
    print()

    print("=" * 80)
    print("PRIMEROS 4000 CARACTERES")
    print("=" * 80)
    print()

    print(xml[:4000])

    client.close()


if __name__ == "__main__":
    main()