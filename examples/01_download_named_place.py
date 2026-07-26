"""
Descarga una única entidad del Nomenclátor Geográfico de Andalucía.

No analiza el XML.
No inserta en SQLite.

Únicamente descarga la respuesta original del WFS y la guarda
para poder realizar ingeniería inversa del modelo.
"""

from pathlib import Path
import sys

# Añade la raíz del proyecto al PYTHONPATH
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from primer.services.wfs import WFSClient


WFS_URL = "https://www.ideandalucia.es/wfs-nga-inspire/services"

TYPE_NAME = "gn:NamedPlace"

OUTPUT = Path("data/debug/named_place.xml")


def main():

    OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    client = WFSClient(WFS_URL)

    print("Descargando una entidad...")

    response = client.get_feature(
        type_name=TYPE_NAME,
        count=1,
        start_index=0,
    )

    OUTPUT.write_bytes(response.content)

    print()
    print("Archivo guardado correctamente:")
    print(OUTPUT.resolve())

    client.close()


if __name__ == "__main__":
    main()