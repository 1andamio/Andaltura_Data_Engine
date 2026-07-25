from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import requests

SEARCH_URL = "https://www.ideandalucia.es/nomenclator/enlace.jsp?lang=esp"
ENTITY_URL = "https://www.ideandalucia.es/nomenclator/entidadConcreta.jsp?lang=esp"

payload = {
    "textB": "granada",
    "provMuni": "on",
    "seleccioProv": "0",
    "seleccioMuni": "0",
    "envioEntidades": "-1",
    "result": "",
    "inicial": "1",
    "final": "10",
    "coordenada": "0",
    "cercanos": "no",
    "elementoSeleccionado": "3",
    "campProvMuni": "1",
    "campMapa": "0",
    "suma": "0",
    "redonda": "3",
    "cuadradoProvMuni": "1",
    "cuadradoMapa": "0",
    "muniSeleccionado": "0",
    "provSeleccionado": "0",
    "entidadesSelec": "",
    "nombreProv": "",
    "nombreMuni": "",
    "c1": "",
    "c2": "",
    "c3": "",
    "c4": "",
    "proviene": "1",
    "coord1": "0",
    "coord2": "0",
    "coord3": "0",
    "coord4": "0",
}

ENTITY_ID = "ES.ES61.NGA.1151"

session = requests.Session()

print("1. Realizando búsqueda...")
response = session.post(
    SEARCH_URL,
    data=payload,
    timeout=60,
)

print("   Status:", response.status_code)

print("2. Solicitando ficha de la entidad...")

response = session.post(
    ENTITY_URL,
    data={
        "entidad": ENTITY_ID
    },
    timeout=60,
)

print("   Status:", response.status_code)
print("   URL:", response.url)

with open("entidad.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print()
print("✓ Archivo guardado como entidad.html")
print(f"✓ Tamaño: {len(response.text):,} caracteres")

if ENTITY_ID in response.text:
    print("✓ El identificador NGA aparece en la respuesta.")

if "Nombre" in response.text:
    print("✓ Parece contener datos de la entidad.")