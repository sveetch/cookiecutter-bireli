"""
=============
Base settings
=============

"""
from pathlib import Path

from configurations import Configuration

from project_composer.compose import Composer
from project_composer.processors import DjangoSettingsProcessor


# Initialize composer with the manifest and the message processor
_composer = Composer(Path("./pyproject.toml").resolve(),
    processors=[DjangoSettingsProcessor],
)

# Resolve dependency order
_composer.resolve_collection(lazy=False)

# Search for all enabled message classes
_classes = _composer.call_processor("DjangoSettingsProcessor", "export")

# Reverse the list since Python class order is from the last to the first
_classes.reverse()

# Add the base messager as the base inheritance
_COMPOSED_CLASSES = _classes + [Configuration]

# Build base settings class from composed settings
ComposedProjectSettings = type(
    "ComposedProjectSettings",
    tuple(_COMPOSED_CLASSES),
    {}
)
