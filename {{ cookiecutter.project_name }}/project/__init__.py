from pathlib import Path

from setuptools.config.pyprojecttoml import read_configuration

import pkg_resources

from project_composer.compose import Composer
from project_composer.contrib.django.processors import (
    DjangoSettingsProcessor, DjangoUrlsProcessor
)


def _extract_version(package_name):
    """
    Get package version from installed distribution or configuration file if not
    installed
    """
    try:
        return pkg_resources.get_distribution(package_name).version
    except pkg_resources.DistributionNotFound:
        _project_dir = Path(__file__).parents[1].resolve()
        _conf = read_configuration(str(_project_dir / "pyproject.toml"))

    return _conf["project"]["version"]


__version__ = _extract_version("{{ cookiecutter.project_name }}")

__generator__ = "cookiecutter-bireli=={{ cookiecutter._bireli_version }}"


# Initialize composer with the manifest and the message processor
print("🚀 Initialize composer")
_composer = Composer(
    Path("./pyproject.toml").resolve(),
    processors=[
        DjangoSettingsProcessor,
        DjangoUrlsProcessor,
    ],
)

# Resolve dependency order
_composer.resolve_collection(lazy=False)
