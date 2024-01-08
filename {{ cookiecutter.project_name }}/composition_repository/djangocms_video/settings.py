from project_composer.marker import EnabledApplicationMarker


class DJANGOCMSVIDEOSettings(EnabledApplicationMarker):
    DJANGOCMS_VIDEO_ALLOWED_EXTENSIONS = ["mp4", "webm", "ogv"]

    @classmethod
    def setup(cls):
        super().setup()

        cls.INSTALLED_APPS.extend(
            [
                "djangocms_video",
            ]
        )
