"""Validate and format Dominican cédulas and RNCs offline, including the official exceptions."""

from .core import detectar, formatear, motivo, validar_cedula, validar_rnc

__version__ = "0.1.0"
__all__ = ["detectar", "formatear", "motivo", "validar_cedula", "validar_rnc"]
