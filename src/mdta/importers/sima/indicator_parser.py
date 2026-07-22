"""
Parser de indicadores del SIMA.
"""

from __future__ import annotations

import re

from mdta.importers.sima.models import Indicator
from mdta.importers.sima.normalizer import ValueNormalizer


YEAR_PATTERN = re.compile(
    r"\.\s*(\d{4}(?:-\d{4})?)$"
)

UNIT_PATTERN = re.compile(
    r"\(([^()]*)\)"
)


class IndicatorParser:

    def __init__(self):

        self.normalizer = ValueNormalizer()

    def parse(
        self,
        section: str,
        label: str,
        value: str,
    ) -> Indicator:

        year = None
        unit = None

        # Año

        match = YEAR_PATTERN.search(label)

        if match:

            year = match.group(1)

            label = label[:match.start()].strip()

        # Unidad

        match = UNIT_PATTERN.search(label)

        if match:

            unit = match.group(1)

            label = (
                label[:match.start()]
                + label[match.end():]
            ).strip()

        value = self.normalizer.normalize(value)

        return Indicator(
            section=section,
            name=label,
            value=value,
            year=year,
            unit=unit,
        )