from project_composer.marker import EnabledApplicationMarker


class DjangoCMSFileSettings(EnabledApplicationMarker):
    """
    DjangoCMS File settings
    """

    @classmethod
    def setup(cls):
        """
        Note on DJANGOCMS_FILE_TEMPLATES setting:

        Provided templates are very minimal by design
        you can add some by creating a folder at project/templates/djangocms_file/
        folder name should be 1st element of tuple.

        Example:

        At project root `mkdir project/templates/djangocms_file/`

        Then add following setting in `DjangoCMSFileSettings.setup`:
        ```python
        cls.DJANGOCMS_FILE_TEMPLATES = [
            ('usageX', _('usageX Version')),
        ]
        ```
        (Dont forget to import `django.utils.translation.gettext_lazy` as _)
        """
        super().setup()

        cls.INSTALLED_APPS.extend([
            "djangocms_file",
        ])
