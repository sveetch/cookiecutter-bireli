from configurations import values

from .base import ComposedProjectSettings


class Production(ComposedProjectSettings):
    """
    Settings for production environment.
    """
    # Labelize the deployed production environment name
    ENVIRONMENT = values.Value("Production", environ_name="DEPLOYED_ENVIRONMENT")
