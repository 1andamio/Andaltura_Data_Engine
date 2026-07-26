"""
Punto de entrada de Primer.
"""

from __future__ import annotations

import sys

from primer.commands.inspect import inspect_command


def main() -> None:

    if len(sys.argv) < 2:
        print("Uso:")
        print("    python -m primer inspect <archivo.xml>")
        raise SystemExit(1)

    command = sys.argv[1]

    if command == "inspect":

        if len(sys.argv) != 3:
            print("Falta el archivo XML.")
            raise SystemExit(1)

        inspect_command(sys.argv[2])
        return

    print(f"Comando desconocido: {command}")
    raise SystemExit(1)


if __name__ == "__main__":
    main()