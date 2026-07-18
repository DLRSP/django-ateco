"""
See PEP 386 (https://peps.python.org/pep-0386/)
"""

__version__ = "0.1.0"
__version_info__ = tuple(
    int(i) if i.isdigit() else i for i in __version__.split(".")
)
__license__ = "MIT"
__title__ = "django_ateco"

__author__ = "DLRSP"
__copyright__ = "Copyright 2010-present DLRSP"

VERSION = __version_info__
