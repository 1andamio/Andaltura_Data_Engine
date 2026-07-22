"""
=========================================================
Andaltura Data Engine

Grupos reutilizables de campos
=========================================================
"""

from fields import identity
from fields import administrative
from fields import audit
from fields import lifecycle


def identity_group():
    return [
        identity.id(),
        identity.nombre(),
        identity.slug(),
    ]


def administrative_group():
    return [
        administrative.codigo_ine(),
        administrative.codigo_iso(),
    ]


def audit_group():
    return [
        audit.created_at(),
        audit.updated_at(),
    ]


def lifecycle_group():
    return [
        lifecycle.activo(),
        lifecycle.version(),
        lifecycle.fuente(),
    ]