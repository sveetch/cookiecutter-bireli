from project_composer.marker import EnabledApplicationMarker

from cmsplugin_blocks.contrib.django_configuration import CmsBlocksDefaultSettings


class CmsPluginBlocksSettings(CmsBlocksDefaultSettings, EnabledApplicationMarker):
    """
    cmsplugin-blocks settings

    .. HINTS::

        * ``test.html`` in plugins templates is reserved to tests, never overwrite them;
        * All feature choices are list of tuple. First choice item is a valid CSS class
          name (not a selector, only alphanumeric, ``-`` and ``_``), second item is the
          label for select option.
    """
    # Enabled plugins to register. Unregistered plugin models are still created but
    # not available anymore in DjangoCMS
    BLOCKS_ENABLED_PLUGINS = [
        "AlbumPlugin",
        "CardPlugin",
        "ContainerPlugin",
        "HeroPlugin",
        "SliderPlugin",
        "AccordionPlugin"
    ]

    # Available feature classes for Album model
    BLOCKS_ALBUM_FEATURES = []

    # Available feature classes for AlbumItem model
    BLOCKS_ALBUMITEM_FEATURES = []

    # Available feature classes for Card model
    BLOCKS_CARD_FEATURES = []

    # Available feature classes for Container model
    BLOCKS_CONTAINER_FEATURES = []

    # Available feature classes for Hero model
    BLOCKS_HERO_FEATURES = [
        ("align-left", "align left"),
        ("align-right", "align right"),
        ("img-left", "Image à gauche"),
        ("img-right", "Image à droite"),
        ]

    # Available feature classes for Slider model
    BLOCKS_SLIDER_FEATURES = [
        ("align-left", "align left"),
        ("align-right", "align right"),
        ]

    # Available feature classes for Slider item model
    BLOCKS_SLIDERITEM_FEATURES = []

    # Available feature classes for Accordion model
    BLOCKS_ACCORDION_FEATURES = []

    # Available feature classes for Accordion item model
    BLOCKS_ACCORDIONITEM_FEATURES = []

    # Available template choices to render an Album object and its items
    BLOCKS_ALBUM_TEMPLATES = [
        ("cmsplugin_blocks/album/default.html", "Default"),
    ]

    # Available template choices to render an Card object
    BLOCKS_CARD_TEMPLATES = [
        ("cmsplugin_blocks/card/default.html", "Default"),
    ]

    # Available template choices to render an Container object
    BLOCKS_CONTAINER_TEMPLATES = [
        ("cmsplugin_blocks/container/default.html", "Default"),
    ]

    # Available template choices to render an Hero object
    BLOCKS_HERO_TEMPLATES = [
        ("cmsplugin_blocks/hero/default.html", "Default"),
    ]

    # Available template choices to render a Slider object and its items
    BLOCKS_SLIDER_TEMPLATES = [
        ("cmsplugin_blocks/slider/default.html", "Default"),
    ]

    # Available template choices to render a Accordion object and its items
    BLOCKS_ACCORDION_TEMPLATES = [
        ("cmsplugin_blocks/accordion/default.html", "Default"),
    ]

    # Allow to input multiple CSS class names divided with a whitespace in Feature
    # value
    BLOCKS_FEATURE_ALLOW_MULTIPLE_CLASSES = True

    @classmethod
    def setup(cls):
        super(CmsPluginBlocksSettings, cls).setup()

        cls.INSTALLED_APPS.extend([
            "cmsplugin_blocks",
        ])
