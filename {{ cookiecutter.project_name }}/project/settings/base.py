"""
.. Note::
    You are probably searching for settings that are instead enabled from
    ``pyproject.toml:collection`` and composed ``settings.py`` files from modules in
    ``composition_repository/``.

    See the Bireli documentation for more details.
"""
from configurations import Configuration
from project_composer.contrib.django.helpers import project_settings

from project import _composer


# Build base settings class from composed applications settings
ComposedProjectSettings = project_settings(_composer, base_classes=[Configuration])
