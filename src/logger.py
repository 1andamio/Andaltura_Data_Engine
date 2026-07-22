"""
=========================================================
Andaltura Data Engine
logger.py

Sistema de registro de eventos
=========================================================
"""

import logging

from config import LOG_FILE


def get_logger(nombre="Andaltura"):

    logger = logging.getLogger(nombre)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formato = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    archivo = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )

    archivo.setFormatter(formato)

    consola = logging.StreamHandler()

    consola.setFormatter(formato)

    logger.addHandler(archivo)
    logger.addHandler(consola)

    return logger