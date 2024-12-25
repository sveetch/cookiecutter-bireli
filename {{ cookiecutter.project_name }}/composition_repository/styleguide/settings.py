from pathlib import Path

from configurations import values

from project_composer.marker import EnabledApplicationMarker


class StyleguideSettings(EnabledApplicationMarker):
    """
    Site layout styleguide
    """
    # Enable JSON dump auto save when CSS manifest has been successfully loaded
    STYLEGUIDE_SAVE_DUMP = values.BooleanValue(
        False,
        environ_name="STYLEGUIDE_SAVE_DUMP",
    )

    @classmethod
    def setup(cls):
        super(StyleguideSettings, cls).setup()

        cls.INSTALLED_APPS.extend([
            "styleguide",
        ])

        # Built CSS manifest relative path to static directory
        cls.STYLEGUIDE_MANIFEST_PATH = (
            Path("css") / "components" / "styleguide" / "manifest.css"
        )

        # JSON manifest dump destination as an absolute path
        cls.STYLEGUIDE_DUMP_PATH = (
            cls.PROJECT_PATH / "templates" / "styleguide" / "manifest.json"
        )
