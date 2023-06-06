from django.conf import settings
from django.urls import reverse

from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool


class EmenciaToolbar(CMSToolbar):
    """
    Include useful admin tool urls in CMS toolbar.

    Add shortcut links to some application admin list into the CMS toolbar.
    """
    supported_apps = []

    def populate(self):

        menu = self.toolbar.get_or_create_menu(
            "emencia_cms_utilities",
            "Applications"
        )

        if "fobi" in settings.INSTALLED_APPS:
            menu.add_sideframe_item(
                name="Fobi forms management",
                url=reverse("fobi.dashboard"),
            )

        if "lotus" in settings.INSTALLED_APPS:
            menu.add_sideframe_item(
                name="Lotus articles",
                url=reverse("admin:lotus_article_changelist"),
            )
            menu.add_sideframe_item(
                name="Lotus categories",
                url=reverse("admin:lotus_category_changelist"),
            )

        if "taggit" in settings.INSTALLED_APPS:
            menu.add_sideframe_item(
                name="Tags management",
                url=reverse("admin:taggit_tag_changelist"),
            )

        if "djangocms_snippet" in settings.INSTALLED_APPS:
            menu.add_sideframe_item(
                name="Snippet management",
                url=reverse("admin:djangocms_snippet_snippet_changelist"),
            )


if "cms" in settings.INSTALLED_APPS:
    toolbar_pool.register(EmenciaToolbar)
