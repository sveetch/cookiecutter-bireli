import copy

from project_composer.marker import EnabledApplicationMarker

from lotus.contrib.django_configuration import LotusDefaultSettings


class LotusSettings(LotusDefaultSettings, EnabledApplicationMarker):
    """
    Lotus settings
    """
    LOTUS_SITEMAP_ARTICLE_OPTIONS = {
        "changefreq": "monthly",
        "priority": 0.51,
        "pinned_priority": 0.80,
        "featured_priority": 0.64,
    }
    LOTUS_ADMIN_ARTICLE_ASSETS = {
        "css": {"all": ("css/components/lotus/admin.css",)},
        "js": None,
    }
    LOTUS_ADMIN_CATEGORY_ASSETS = {
        "css": {"all": ("css/components/lotus/admin.css",)},
        "js": None,
    }
    LOTUS_ADMIN_ALBUM_ASSETS = {
        "css": {"all": ("css/components/lotus/admin.css",)},
        "js": None,
    }

    @classmethod
    def setup(cls):
        super(LotusSettings, cls).setup()

        cls.INSTALLED_APPS.extend([
            "view_breadcrumbs",
            "lotus",
        ])

        cls.CKEDITOR_CONFIGS["lotus"] = copy.deepcopy(cls.CKEDITOR_SHARED_CONF)
        cls.CKEDITOR_CONFIGS["lotus"].update({
            "width": "100%",
            "height": 400,
            "extraPlugins": "image2,youtube,vimeo,codemirror",
            "removePlugins": "exportpdf,image,flash,stylesheetparser",
            "toolbar": "Lotus",
            "toolbar_Lotus": [
                ["Undo", "Redo"],
                ["ShowBlocks"],
                ["Format", "Styles"],
                ["RemoveFormat"],
                ["Maximize"],
                "/",
                ["Bold", "Italic", "Underline", "-", "Subscript", "Superscript"],
                ["JustifyLeft", "JustifyCenter", "JustifyRight"],
                ["TextColor"],
                ["Link", "Unlink"],
                [
                    "Image", "Youtube", "Vimeo", "-", "NumberedList", "BulletedList",
                    "-", "Table", "-", "CreateDiv", "HorizontalRule",
                ],
                # ["Iframe"],
                # ["Templates"],
                ["Source"],
            ],
        })
