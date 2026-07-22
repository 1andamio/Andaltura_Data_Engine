"""
Utilidades para la normalización de texto.
"""

from __future__ import annotations

import html
import re

from ftfy import fix_encoding


_MOJIBAKE_HINTS = ("Ã", "Â", "â", "ï»¿")


def _fix_mojibake(text: str) -> str:
    """
    Repara automáticamente texto con problemas de codificación
    (mojibake), por ejemplo 'NÃ­jar' -> 'Níjar'.
    """

    if not any(hint in text for hint in _MOJIBAKE_HINTS):
        return text

    return fix_encoding(text)


def normalize_text(text: str | None) -> str:
    """
    Normaliza una cadena de texto procedente del SIMA.

    - Elimina BOM.
    - Decodifica entidades HTML.
    - Repara posibles problemas de codificación.
    - Sustituye espacios no separables.
    - Compacta espacios consecutivos.
    """

    if text is None:
        return ""

    text = str(text)

    # Eliminar BOM UTF-8
    text = text.replace("\ufeff", "")
    text = text.replace("ï»¿", "")

    # Decodificar entidades HTML
    text = html.unescape(text)

    # Reparar mojibake si existe
    text = _fix_mojibake(text)

    # Algunas entidades pueden aparecer tras la reparación
    text = html.unescape(text)

    # Espacios no separables
    text = text.replace("\xa0", " ")

    # Compactar espacios
    text = re.sub(r"\s+", " ", text)

    return text.strip()