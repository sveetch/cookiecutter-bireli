from project_composer.marker import EnabledApplicationMarker

from import_export.formats.base_formats import CSV, JSON, XLSX


class DisketteSettings(EnabledApplicationMarker):
    """
    Django import export settings
    """

    IMPORT_EXPORT_FORMATS = [CSV, JSON, XLSX]

    @classmethod
    def setup(cls):
        super().setup()

        cls.INSTALLED_APPS.append("import_export")
