from configurations import values

from .base import ComposedProjectSettings


class Production(ComposedProjectSettings):
    """
    Settings for production environment.
    """
    # Labelize the deployed production environment name
    ENVIRONMENT = values.Value("Production", environ_name="DEPLOYED_ENVIRONMENT")

    @classmethod
    def pre_setup(cls):
        # Expected path for optional Dotenv file
        cls.DOTENV = cls.BASE_DIR / ".env"

        super(Production, cls).pre_setup()
