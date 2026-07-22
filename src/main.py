"""
MDTA

Punto de entrada del Motor de Datos Territorial de Andaltura.
"""

from pathlib import Path

from engine.database import Database
from engine.validator import Validator
from engine.sql.sqlite import SQLiteBuilder

from providers.csv_provider import CSVProvider

from importers.nucleos_importer import NucleosImporter

from schema.nucleos_poblacion import NucleosPoblacionSchema


def main():

    # -----------------------------------------------------
    # Base de datos
    # -----------------------------------------------------

    database = Database(
        Path("data/andalucia.db")
    )

    # -----------------------------------------------------
    # Esquema
    # -----------------------------------------------------

    table = NucleosPoblacionSchema.table()

    # -----------------------------------------------------
    # Validación
    # -----------------------------------------------------

    Validator().validate(table)

    # -----------------------------------------------------
    # Crear tabla
    # -----------------------------------------------------

    builder = SQLiteBuilder()

    sql = builder.create_table(table)

    database.executescript(sql)

    database.commit()

    # -----------------------------------------------------
    # Importar CSV
    # -----------------------------------------------------

    provider = CSVProvider(
        "datasets/nucleos.csv",
        delimiter=";",
        encoding="utf-8-sig",
    )

    importer = NucleosImporter(
        database,
        table,
    )

    total = importer.import_rows(provider)

    print()

    print("-" * 50)

    print(f"Importados: {total}")

    print("-" * 50)

    database.close()


if __name__ == "__main__":

    main()