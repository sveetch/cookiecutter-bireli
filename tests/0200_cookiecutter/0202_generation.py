import json

from cookiecutter.main import cookiecutter


def test_create_project(tmp_path, settings):
    """
    With default option, cookiecutter should generate a project without errors.
    """
    # Expected project directory name computed from slugified 'project_title'
    project_destination = tmp_path / "a-project-sample"
    # Expected built config
    baked_config = project_destination / "cookiebaked.json"

    # Minimal context, let config default value to be used
    context = {
        "project_title": "A project Sample",
    }

    # Use cookiecutter programatically to create project with context
    cookiecutter(
        str(settings.cookiecutter_template.parent),
        no_input=True,
        extra_context=context,
        output_dir=str(tmp_path),
    )

    # Check for some significant paths
    assert (project_destination / "requirements/base_template.txt").exists()
    assert (project_destination / "pyproject.toml").exists()
    assert (project_destination / "composition_repository").exists()
    assert (project_destination / "project").exists()

    # Ensure baked project config is valid
    assert baked_config.exists() is True
    assert baked_config.is_file() is True
    # Load JSON config
    baked_config = json.loads(baked_config.read_text())
    # Initial version with default versionning is correct
    assert baked_config["versioning"] == "natural"
    assert baked_config["__version"] == "0.1.0"
