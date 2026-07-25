from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import requests
from bs4 import BeautifulSoup

URL = "https://www.ideandalucia.es/nomenclator/buscador.jsp?lang=esp"

print("Descargando formulario...")

response = requests.get(URL, timeout=60)
response.raise_for_status()

print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

print("\nFORMULARIOS\n")

forms = soup.find_all("form")

print(f"Encontrados {len(forms)} formularios\n")

for i, form in enumerate(forms, start=1):

    print("=" * 80)
    print(f"FORMULARIO {i}")
    print("=" * 80)

    print("Action :", form.get("action"))
    print("Method :", form.get("method"))

    print("\nCampos:\n")

    for field in form.find_all(["input", "select", "textarea"]):

        print(
            field.name,
            field.get("name"),
            field.get("type"),
            field.get("value"),
        )

    print()