"""
MDTA - Esquema de Núcleos de Población

Tabla oficial de núcleos de población del MDTA.
"""

from models import Table

from profiles.population_center import PopulationCenterProfile

from dictionary.population_center import PopulationCenter


class NucleosPoblacionSchema:
    """
    Definición de la tabla de núcleos de población.
    """

    @staticmethod
    def table() -> Table:

        table = Table(
            name="nucleos_poblacion",
            description="Catálogo oficial de núcleos de población.",
            fields=PopulationCenterProfile.fields(),
        )

        # =====================================================
        # Campos específicos del Nomenclátor
        # =====================================================

        table.add_fields([

            PopulationCenter.CODIGO_NOMENCLATOR.clone(),

            PopulationCenter.CODIGO_ENTIDAD.clone(),

            PopulationCenter.CODIGO_NUCLEO.clone(),

            PopulationCenter.TIPO_NUCLEO.clone(),

            PopulationCenter.CATEGORIA.clone(),

            PopulationCenter.ES_CAPITAL_MUNICIPAL.clone(),

            PopulationCenter.ES_DISSEMINADO.clone(),

            PopulationCenter.POBLACION_RESIDENTE.clone(),

            PopulationCenter.POBLACION_ESTACIONAL.clone(),

            PopulationCenter.NUMERO_VIVIENDAS.clone(),

            PopulationCenter.CODIGO_POSTAL.clone(),

            PopulationCenter.ALTITUD.clone(),

            PopulationCenter.DISTANCIA_CAPITAL.clone(),

            PopulationCenter.HABITADO.clone(),

            PopulationCenter.FECHA_REFERENCIA.clone(),

            PopulationCenter.FUENTE.clone(),

        ])

        return table