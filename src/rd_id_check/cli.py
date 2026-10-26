"""Command line interface for rd-id-check."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .core import detectar, formatear, motivo


def _leer_archivo(ruta: str) -> list[str]:
    lineas = Path(ruta).read_text(encoding="utf-8-sig").splitlines()
    out = []
    for linea in lineas:
        linea = linea.strip()
        if linea and not linea.startswith("#"):
            out.append(linea)
    return out


def _evaluar(texto: str) -> dict:
    razon = motivo(texto)
    return {
        "input": texto,
        "tipo": detectar(texto),
        "valido": razon == "",
        "formato": formatear(texto) if razon == "" else None,
        "motivo": razon,
    }


def _linea(r: dict) -> str:
    if not r["valido"]:
        return f"{r['input']}  ✗ inválido: {r['motivo']}"
    etiqueta = "cédula válida" if r["tipo"] == "cedula" else "RNC válido"
    return f"{r['formato']}  ✓ {etiqueta}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="rd-id-check",
        description="Validate and format Dominican cédulas (11 digits) and RNCs (9 digits) offline.",
    )
    parser.add_argument("numbers", nargs="*", metavar="NUMBER", help="cédula or RNC to check")
    parser.add_argument("--json", action="store_true", help="print results as a JSON list")
    parser.add_argument("--file", metavar="PATH", help="read one number per line (UTF-8; blank lines and # comments ignored)")
    args = parser.parse_args(argv)

    numeros = list(args.numbers)
    if args.file:
        try:
            numeros += _leer_archivo(args.file)
        except OSError as exc:
            parser.error(f"cannot read {args.file}: {exc.strerror or exc}")
    if not numeros:
        parser.error("provide at least one NUMBER or --file")

    resultados = [_evaluar(n) for n in numeros]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if args.json:
        print(json.dumps(resultados, ensure_ascii=False, indent=2))
    else:
        for r in resultados:
            print(_linea(r))
    return 0 if all(r["valido"] for r in resultados) else 1
