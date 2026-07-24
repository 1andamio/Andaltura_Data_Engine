"""
Modelos de datos para el importador del SIMA.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


# ----------------------------------------------------------------------
# Tipos de entidades de población
# ----------------------------------------------------------------------


class PopulationEntityType(str, Enum):
    """
    Tipos de entidades de población.
    """

    MUNICIPALITY_TOTAL = "municipality_total"

    NUCLEI_TOTAL = "nuclei_total"

    DISSEMINATED = "disseminated"

    NUCLEUS = "nucleus"


# ----------------------------------------------------------------------
# Indicadores
# ----------------------------------------------------------------------


@dataclass(slots=True)
class Indicator:
    """
    Representa un indicador individual del SIMA.
    """

    section: str

    name: str

    value: object

    year: str | None = None

    unit: str | None = None


# ----------------------------------------------------------------------
# Secciones
# ----------------------------------------------------------------------


@dataclass(slots=True)
class Section:
    """
    Agrupa los indicadores pertenecientes a una sección del SIMA.
    """

    name: str

    indicators: list[Indicator] = field(default_factory=list)

    # --------------------------------------------------------------

    def add_indicator(
        self,
        indicator: Indicator,
    ) -> None:
        """
        Añade un indicador a la sección.
        """

        self.indicators.append(indicator)


# ----------------------------------------------------------------------
# Entidades de población
# ----------------------------------------------------------------------


@dataclass(slots=True)
class PopulationEntity:
    """
    Representa una entidad de población.

    Puede representar:

    - Total municipal
    - Población en núcleos
    - Población diseminada
    - Un núcleo de población
    """

    official_code: str = ""

    parent_code: str = ""

    name: str = ""

    entity_type: PopulationEntityType = (
        PopulationEntityType.NUCLEUS
    )

    population_total: int = 0

    population_male: int = 0

    population_female: int = 0

    year: int | None = None

    source: str = "SIMA"

    is_main_entity: bool = False

    notes: str | None = None


# ----------------------------------------------------------------------
# Municipio
# ----------------------------------------------------------------------


@dataclass(slots=True)
class MunicipalityData:
    """
    Información completa de un municipio obtenida desde el SIMA.
    """

    code: str

    name: str

    sections: list[Section] = field(default_factory=list)

    population_entities: list[PopulationEntity] = (
        field(default_factory=list)
    )

    # --------------------------------------------------------------

    def add_section(
        self,
        section: Section,
    ) -> None:
        """
        Añade una sección.
        """

        self.sections.append(section)

    # --------------------------------------------------------------

    def add_population_entity(
        self,
        entity: PopulationEntity,
    ) -> None:
        """
        Añade una entidad de población.
        """

        self.population_entities.append(entity)

    # --------------------------------------------------------------

    def get_section(
        self,
        name: str,
    ) -> Section | None:
        """
        Devuelve una sección por nombre.
        """

        for section in self.sections:

            if section.name == name:
                return section

        return None

    # --------------------------------------------------------------

    def get_population_entity(
        self,
        official_code: str,
    ) -> PopulationEntity | None:
        """
        Devuelve una entidad por su código oficial.
        """

        for entity in self.population_entities:

            if entity.official_code == official_code:
                return entity

        return None

    # --------------------------------------------------------------

    def get_population_entities(
        self,
        entity_type: PopulationEntityType,
    ) -> list[PopulationEntity]:
        """
        Devuelve todas las entidades de un tipo.
        """

        return [
            entity
            for entity in self.population_entities
            if entity.entity_type == entity_type
        ]

    # --------------------------------------------------------------

    @property
    def nuclei(self) -> list[PopulationEntity]:
        """
        Devuelve únicamente los núcleos de población.
        """

        return self.get_population_entities(
            PopulationEntityType.NUCLEUS
        )

    # --------------------------------------------------------------

    @property
    def municipality_total(
        self,
    ) -> PopulationEntity | None:
        """
        Devuelve el registro de población total del municipio.
        """

        entities = self.get_population_entities(
            PopulationEntityType.MUNICIPALITY_TOTAL
        )

        return entities[0] if entities else None

    # --------------------------------------------------------------

    @property
    def nuclei_total(
        self,
    ) -> PopulationEntity | None:
        """
        Devuelve el registro de población en núcleos.
        """

        entities = self.get_population_entities(
            PopulationEntityType.NUCLEI_TOTAL
        )

        return entities[0] if entities else None

    # --------------------------------------------------------------

    @property
    def disseminated(
        self,
    ) -> PopulationEntity | None:
        """
        Devuelve el registro de población diseminada.
        """

        entities = self.get_population_entities(
            PopulationEntityType.DISSEMINATED
        )

        return entities[0] if entities else None