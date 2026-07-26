from pathlib import Path

from primer.services.wfs import WFSClient


OUTPUT = Path("data/debug")
OUTPUT.mkdir(parents=True, exist_ok=True)


def main():

    client = WFSClient(
        "https://www.ideandalucia.es/wfs-nga-inspire/services"
    )

    print("Descargando primera página...")

    response = client.request(
        request="GetFeature",
        typeNames="gn:NamedPlace",
        startIndex=0,
        count=1,
        outputFormat="application/json",
    )

    print()
    print("STATUS :", response.status_code)
    print("CONTENT-TYPE :", response.headers.get("Content-Type"))
    print()

    texto = response.text

    print(texto[:3000])

    with open(
        OUTPUT / "respuesta.txt",
        "w",
        encoding="utf-8",
    ) as f:
        f.write(texto)

    print()
    print("Guardado en data/debug/respuesta.txt")

    client.close()


if __name__ == "__main__":
    main()