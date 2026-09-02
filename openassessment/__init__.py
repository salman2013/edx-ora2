"""
Initialization Information for Open Assessment Module
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("ora2")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
