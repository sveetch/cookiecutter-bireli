from configurations import Configuration
from project_composer.contrib.django.helpers import project_settings

from project import _composer


# Build base settings class from composed applications settings
ComposedProjectSettings = project_settings(_composer, base_classes=[Configuration])
