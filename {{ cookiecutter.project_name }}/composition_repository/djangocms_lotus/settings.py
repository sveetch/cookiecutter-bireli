from project_composer.marker import EnabledApplicationMarker


class DjangocmsLotusSettings(EnabledApplicationMarker):
    """
    djangocms-lotus settings
    """
    CMSLOTUS_ARTICLE_FLUX_TEMPLATES = (
        ("djangocms_lotus/article-flux/default.html", "Default"),
    )

    CMSLOTUS_ARTICLE_FLUX_LIMIT_DEFAULT = 5

    CMSLOTUS_ADMIN_ARTICLE_FLUX_ASSETS = {
        "css": {
            "all": ("css/cmslotus-admin/article-flux.css",)
        },
        "js": None,
    }

    @classmethod
    def post_setup(cls):
        super(DjangocmsLotusSettings, cls).post_setup()

        cls.LOTUS_ADMIN_ALBUM_ASSETS["css"]["all"] = (
            "css/cmslotus-admin/lotus-admin.css",
        )
        cls.LOTUS_ADMIN_ARTICLE_ASSETS["css"]["all"] = (
            "css/cmslotus-admin/lotus-admin.css",
        )
        cls.LOTUS_ADMIN_CATEGORY_ASSETS["css"]["all"] = (
            "css/cmslotus-admin/lotus-admin.css",
        )

        cls.INSTALLED_APPS.extend([
            "djangocms_lotus",
        ])
