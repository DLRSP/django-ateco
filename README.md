# django-ateco

Django helpers for the Italian **ATECO** classification, wrapping the pure-Python [`ateco`](https://pypi.org/project/ateco/) library.

[![CI](https://github.com/DLRSP/django-ateco/actions/workflows/ci.yaml/badge.svg)](https://github.com/DLRSP/django-ateco/actions/workflows/ci.yaml)

## Requirements

- Python 3.10+
- Django 3.2+
- [`ateco`](https://pypi.org/project/ateco/)

## Install

```shell
pip install django-ateco
```

```python
INSTALLED_APPS = [
    # ...
    "django_ateco",
]
```

## Usage

```python
from django_ateco import services

node = services.lookup("01.11.00")
assert services.validate("55.20.42")
```

## License

MIT
