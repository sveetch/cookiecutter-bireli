"""
=============
Base settings
=============

"""
from pathlib import Path

from configurations import Configuration

from project import _composer


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
