"""
Comando inspect.

Analiza un documento XML y muestra un resumen del modelo generado.
"""

from __future__ import annotations

from pathlib import Path

from primer.readers.xml_reader import XMLReader


def inspect_command(filename: str | Path) -> None:
    """
    Inspecciona un documento XML.
    """

    reader = XMLReader()

    model = reader.read(filename)

    summary = model.stats()

    print()
    print("Primer XML Inspector")
    print("-" * 40)

    print(f"Documento     : {Path(filename).name}")
    print(f"Nodos         : {summary['nodes']}")
    print(f"Atributos     : {summary['attributes']}")
    print(f"Namespaces    : {summary['namespaces']}")
    print(f"Profundidad   : {summary['max_depth']}")

    if model.root:
        print(f"Nodo raíz     : {model.root.name}")

    print("-" * 40)