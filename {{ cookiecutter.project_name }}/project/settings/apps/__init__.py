"""
============================
Application settings modules
============================

Commonly you won't never edit theses modules and will prefer to make your specific
changes in environment settings.

"""
from .icomoon import IcomoonSettings
from .staticpages import StaticpageSettings
from .styleguide import StyleguideSettings
from .webpack import WebpackSettings


__all__ = [
    "IcomoonSettings",
    "StaticpageSettings",
    "StyleguideSettings",
    "WebpackSettings",
]
