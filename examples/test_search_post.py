from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import requests

URL = "https://www.ideandalucia.es/nomenclator/enlace.jsp?lang=esp"

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

print("Enviando búsqueda...")

session = requests.Session()

response = session.post(
    URL,
    data=payload,
    timeout=60
)

print("Status:", response.status_code)
print("URL final:", response.url)

with open("resultado.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Guardado como resultado.html")

if "Resultado de la búsqueda" in response.text:
    print("✓ Página de resultados detectada")

if "Encontradas" in response.text:
    inicio = response.text.find("Encontradas")
    print(response.text[inicio:inicio + 120])