"""
=============
Base settings
=============

"""
from pathlib import Path

from configurations import Configuration

from project_composer.compose import ComposeDjangoSettings


# Compose settings from enabled applications
_composer = ComposeDjangoSettings(
    Path("./composition-manifest.json").resolve(),
    "composition.apps"
)


# Add the base django-configuration class as the base inheritance
_COMPOSED_CLASSES = _composer.export() + [Configuration]


# Build base settings class from composed settings
ComposedProjectSettings = type(
    "ComposedProjectSettings",
    tuple(_COMPOSED_CLASSES),
    {}
)
