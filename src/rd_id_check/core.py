"""Validation and formatting of Dominican cédulas and RNCs."""

from __future__ import annotations

import re

from stdnum.do import cedula, rnc


def _normalizar(texto: str) -> str:
    return re.sub(r"[\s.\-]", "", texto or "")


def detectar(texto: str) -> str | None:
    limpio = _normalizar(texto)
    if not limpio.isdigit():
        return None
    if len(limpio) == 11:
        return "cedula"
    if len(limpio) == 9:
        return "rnc"
    return None


def validar_cedula(texto: str) -> bool:
    limpio = _normalizar(texto)
    return len(limpio) == 11 and cedula.is_valid(limpio)


def validar_rnc(texto: str) -> bool:
    limpio = _normalizar(texto)
    return len(limpio) == 9 and rnc.is_valid(limpio)


def motivo(texto: str) -> str:
    limpio = _normalizar(texto)
    if not limpio.isdigit():
        return "solo puede contener dígitos"
    if len(limpio) not in (9, 11):
        return "debe tener 11 dígitos (cédula) o 9 (RNC)"
    if validar_cedula(limpio) or validar_rnc(limpio):
        return ""
    return "el dígito verificador no coincide"


def formatear(texto: str) -> str:
    if motivo(texto):
        raise ValueError(f"invalid number: {texto!r}")
    limpio = _normalizar(texto)
    if len(limpio) == 11:
        return f"{limpio[:3]}-{limpio[3:10]}-{limpio[10]}"
    return f"{limpio[:3]}-{limpio[3:8]}-{limpio[8]}"
