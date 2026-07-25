"""
Estados posibles de un Dataset.
"""

from enum import Enum


class DatasetStatus(str, Enum):
    """
    Estado de un Dataset durante su ciclo de vida.
    """

    DEFINED = "defined"

    DOWNLOADING = "downloading"

    DOWNLOADED = "downloaded"

    PARSING = "parsing"

    PARSED = "parsed"

    NORMALIZING = "normalizing"

    NORMALIZED = "normalized"

    TRANSFORMING = "transforming"

    TRANSFORMED = "transformed"

    VALIDATING = "validating"

    VALIDATED = "validated"

    EXPORTING = "exporting"

    EXPORTED = "exported"

    FAILED = "failed"

    ARCHIVED = "archived"