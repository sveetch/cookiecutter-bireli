from project_composer.marker import EnabledApplicationMarker


class DjangoCmsAudioDefinitions(EnabledApplicationMarker):
    def define(self):
        return super().define() + [
            [
                "djangocms_audio",
                {
                    "comments": "Djangocms_Audio",
                    "natural_foreign": True,
                    "models": [
                        "djangocms_audio.AudioPlayer",
                        "djangocms_audio.AudioFile",
                        "djangocms_audio.AudioFolder",
                        "djangocms_audio.AudioTrack"
                    ]
                }
            ],
        ]
