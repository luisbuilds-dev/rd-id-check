import json

from rd_id_check import detectar, formatear, motivo, validar_cedula, validar_rnc
from rd_id_check.cli import main


def test_non_digits():
    assert motivo("abc12345678") == "solo puede contener dígitos"
    assert detectar("abc") is None


def test_length_not_mixed():
    assert not validar_cedula("401506254")
    assert not validar_rnc("00113918205")


def test_format_rnc_and_cedula():
    assert formatear("1-01-85004-3") == "101-85004-3"
    assert formatear("001.1391820.5") == "001-1391820-5"


def test_cli_usage_error():
    import pytest

    with pytest.raises(SystemExit) as e:
        main([])
    assert e.value.code == 2


def test_cli_json_invalid_file(tmp_path, capsys):
    f = tmp_path / "x.txt"
    f.write_text("00113918204\n", encoding="utf-8")
    assert main(["--json", "--file", str(f)]) == 1
    assert json.loads(capsys.readouterr().out)[0]["tipo"] == "cedula"
