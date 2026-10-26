"""Acceptance tests with real public examples:
- 401-50625-4: RNC printed by the DGII on its own official notice 16-24 (2024).
- 1-01-85004-3 and 001-1391820-5 / 001-1391820-4: examples from the python-stdnum documentation.
- 000-0002124-9 and 1-01-58160-1: officially issued numbers whose check digit does NOT follow the formula
  (exceptions listed by python-stdnum); a correct validator must accept them.
"""
import json

import pytest

from rd_id_check import detectar, formatear, motivo, validar_cedula, validar_rnc
from rd_id_check.cli import main


def test_rnc_real_de_la_dgii():
    assert validar_rnc("401506254")
    assert validar_rnc("401-50625-4")
    assert formatear("401506254") == "401-50625-4"


def test_ejemplos_de_referencia():
    assert validar_rnc("1-01-85004-3")
    assert validar_cedula("00113918205")
    assert validar_cedula("001-1391820-5")
    assert not validar_cedula("00113918204")
    assert formatear("00113918205") == "001-1391820-5"


def test_excepciones_oficiales():
    assert validar_cedula("00000021249")
    assert validar_rnc("101581601")


def test_detectar_y_motivos():
    assert detectar("001 1391820 5") == "cedula"
    assert detectar("401.50625.4") == "rnc"
    assert detectar("12345") is None
    assert motivo("00113918205") == ""
    assert "dígito verificador" in motivo("00113918204")
    assert "11 dígitos" in motivo("12345")
    with pytest.raises(ValueError):
        formatear("00113918204")


def test_cli_codigos_de_salida(capsys):
    assert main(["00113918205", "401506254"]) == 0
    salida = capsys.readouterr().out
    assert "001-1391820-5" in salida and "401-50625-4" in salida
    assert main(["00113918204"]) == 1
    assert "dígito verificador" in capsys.readouterr().out


def test_cli_json(capsys):
    assert main(["--json", "401506254", "123"]) == 1
    datos = json.loads(capsys.readouterr().out)
    assert datos[0] == {"input": "401506254", "tipo": "rnc", "valido": True, "formato": "401-50625-4", "motivo": ""}
    assert datos[1]["valido"] is False and datos[1]["formato"] is None and datos[1]["tipo"] is None


def test_cli_archivo(tmp_path, capsys):
    f = tmp_path / "lista.txt"
    f.write_text("# clientes\n00113918205\n\n00113918204\n", encoding="utf-8")
    assert main(["--file", str(f)]) == 1
    salida = capsys.readouterr().out
    assert "001-1391820-5" in salida and "inválido" in salida
