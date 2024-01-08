from project_composer.marker import EnabledApplicationMarker


class DjangoCMSAudioSettings(EnabledApplicationMarker):
    DJANGOCMS_AUDIO_ALLOWED_EXTENSIONS = ["mp3", "ogg", "wav"]

    @classmethod
    def setup(cls):
        super().setup()

        cls.INSTALLED_APPS.extend(
            [
                "djangocms_audio",
            ]
        )
