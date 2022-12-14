"""
======================
Production environment
======================

"""
from configurations import values

from .base import ComposedProjectSettings


class Production(ComposedProjectSettings):
    """
    Settings for kubernetes environment.
    """
    # Labelize the deployed production environment name
    ENVIRONMENT = values.Value("Production", environ_name="DEPLOYED_ENVIRONMENT")

    @classmethod
    def post_setup(cls):
        super().post_setup()
        # Expected path for optional Dotenv file
        cls.DOTENV = cls.BASE_DIR / ".env"
