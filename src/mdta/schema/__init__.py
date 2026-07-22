from models import Schema

from .provincias import PROVINCIAS

MDTA = Schema(
    name="MDTA",
    version="1.0",
    description="Modelo de Datos Territoriales de Andaltura",
    tables=[
        PROVINCIAS,
    ]
)