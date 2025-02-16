from project_composer.marker import EnabledApplicationMarker

from import_export.formats.base_formats import CSV, XLSX


class ImportExportSettings(EnabledApplicationMarker):
    """
    Django import export settings
    """

    IMPORT_EXPORT_FORMATS = [CSV, XLSX]

    @classmethod
    def setup(cls):
        super().setup()

        cls.INSTALLED_APPS.append("import_export")
