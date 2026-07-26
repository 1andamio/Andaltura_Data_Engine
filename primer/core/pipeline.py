"""
Pipeline principal de Primer.
"""

from __future__ import annotations

from primer.core.model import Model


class Pipeline:
    """
    Ejecuta una secuencia de procesadores sobre un modelo.
    """

    def __init__(self):

        self._steps = []

    # -----------------------------------------------------

    def add(self, step):

        self._steps.append(step)

        return self

    # -----------------------------------------------------

    def run(
        self,
        model: Model,
    ) -> Model:

        for step in self._steps:

            step.process(model)

        return model