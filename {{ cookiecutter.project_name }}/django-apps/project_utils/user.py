from django.apps import apps
from django.conf import settings


def safe_get_user_model():
    """
    Shortcut to get the User model class enabled from settings.

    Returns:
        class: The model class for the enabled User model.
    """
    user_app, user_model = settings.AUTH_USER_MODEL.split(".")
    return apps.get_registered_model(user_app, user_model)
