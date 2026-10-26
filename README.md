<p align="center"><img src="assets/banner.png" alt="RD ID Check" width="100%"></p>

<h1 align="center">RD ID Check</h1>

<p align="center">
  <a href="https://github.com/luisbuilds-dev/rd-id-check/actions/workflows/ci.yml"><img src="https://github.com/luisbuilds-dev/rd-id-check/actions/workflows/ci.yml/badge.svg" alt="Tests"></a>
  <a href="https://pypi.org/project/rd-id-check/"><img src="https://img.shields.io/pypi/v/rd-id-check" alt="PyPI"></a>
  <img src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-informational" alt="Platforms">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT"></a>
</p>

<p align="center"><b>Validate and format Dominican cédulas and RNCs offline.</b></p>

<p align="center"><a href="README.es.md">🇪🇸 Leer en español</a> · <a href="https://luisbuilds.com/h/rd-id-check">Step-by-step guide</a></p>

---

RD ID Check validates and formats Dominican identity numbers (cédula, 11 digits) and tax IDs (RNC, 9 digits) without a network connection. It is a command-line tool and a Python library for developers, data entry staff, and anyone who checks lists of clients or suppliers.


## Features

- Offline validation using python-stdnum, including the official exceptions
- Accepts numbers with spaces, dashes or dots
- Formats cédulas and RNCs the way the DGII writes them
- Batch validation from a UTF-8 text file
- JSON output for scripts
- Spanish messages that explain why a number is invalid


## Install


```bash
pipx install rd-id-check
```

No `pipx`? `pip install rd-id-check` works too. Requires Python 3.10+ on Windows, macOS or Linux.

## Usage

Check a cédula and an RNC at once:

```console
$ rd-id-check 00113918205 401506254
```

Get JSON for your scripts:

```console
$ rd-id-check --json 401-50625-4
```

Validate a whole list (exit code 1 if any is invalid):

```console
$ rd-id-check --file clientes.txt
```

Run `rd-id-check --help` to see every option.


## FAQ

**Does it need internet or send my numbers anywhere?**
No. It works offline, without a network connection.

**How do I know if a number is a cédula or an RNC?**
By its length: 11 digits is a cédula, 9 digits is an RNC. Spaces, dashes and dots are ignored.

**What does it not check?**
It does not confirm that a person or company exists or is active, which requires the DGII or JCE online services. It also does not handle passports, foreign IDs or NCF/e-CF receipts.



## Support

This project is provided **as-is**, free and open source, without guaranteed support. If you find a security issue, please report it privately (see [SECURITY.md](SECURITY.md)).

If it saved you time, you can [sponsor my work](https://github.com/sponsors/luisbuilds-dev) ❤️

---

<p align="center">Made by <a href="https://luisbuilds.com">Luis Cabrera</a> · <a href="LICENSE">MIT License</a></p>
