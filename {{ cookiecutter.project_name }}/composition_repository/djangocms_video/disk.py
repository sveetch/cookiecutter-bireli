from project_composer.marker import EnabledApplicationMarker


class DjangoCmsVideoDefinitions(EnabledApplicationMarker):
    def define(self):
        return super().define() + [
            [
                "djangocms_video",
                {
                    "comments": "Djangocms_Video",
                    "natural_foreign": True,
                    "models": [
                        "djangocms_video.VideoPlayer",
                        "djangocms_video.VideoSource",
                        "djangocms_video.VideoTrack"
                    ]
                }
            ],
        ]
