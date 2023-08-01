
def test_cookiecutter_settings(settings):
    """
    Ensure cookiecutter settings point to the right stuff.
    """
    # JSON config has been properly loaded
    assert isinstance(settings.cookiecutter_config, dict) is True

    # Template directory path is correct
    assert settings.cookiecutter_template.exists() is True
    assert settings.cookiecutter_template.is_dir() is True
