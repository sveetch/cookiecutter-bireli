import json

from diskette.contrib.django_configuration import DisketteDefaultSettings

from project_composer.marker import EnabledApplicationMarker


class DisketteSettings(DisketteDefaultSettings, EnabledApplicationMarker):
    """
    Diskette settings
    """

    # A list of *Unix shell-style wildcards* patterns to filter out some storages files
    DISKETTE_STORAGES_EXCLUDES = ["cache/*"]

    # Filename for dump tarball file.
    DISKETTE_DUMP_FILENAME = "diskette{features}.tar.gz"

    @classmethod
    def setup(cls):
        super(DisketteSettings, cls).setup()

        cls.INSTALLED_APPS.extend([
            "diskette",
        ])

        # Application definition to dump data loaded from built JSON
        diskette_conf = cls.VAR_PATH / "diskette.json"
        cls.DISKETTE_APPS = (
            json.loads(diskette_conf.read_text())
            if diskette_conf.exists() else []
        )

        # A list of Path objects for storage to collect and dump
        cls.DISKETTE_STORAGES = [cls.MEDIA_ROOT]

        # For where are stored created dump
        cls.DISKETTE_DUMP_PATH = cls.VAR_PATH

        # For where to extract archive storages contents
        cls.DISKETTE_LOAD_STORAGES_PATH = cls.BASE_DIR
