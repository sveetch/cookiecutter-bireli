from pathlib import Path

import tomli

from project_composer.compose import Composer
from project_composer.contrib.django.processors import (
    DjangoSettingsProcessor, DjangoUrlsProcessor
)


BASE_DIR = Path(__file__).parents[1].resolve()


def _extract_version():
    """
    Get package version from project TOML file
    """
    _conf = tomli.loads((BASE_DIR / "pyproject.toml").read_text())

    return _conf["project"]["version"]


__version__ = _extract_version()

__generator__ = "cookiecutter-bireli=={{ cookiecutter._bireli_version }}"


# Initialize composer with the manifest and processors needed for Django
_composer = Composer(
    Path("./pyproject.toml").resolve(),
    processors=[
        DjangoSettingsProcessor,
        DjangoUrlsProcessor,
    ],
)

# Resolve dependency order
_composer.resolve_collection(lazy=False)
