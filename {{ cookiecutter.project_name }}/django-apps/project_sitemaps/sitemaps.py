from django.conf import settings

from cms.sitemaps import CMSSitemap
from lotus.sitemaps import ArticleSitemap


class CustomizedCMSSitemap(CMSSitemap):
    """
    Publish CMS sitemap with some configurable options from settings.

    Also implement a variance for item ``priority`` depending it is a homepage or not.
    """
    default_priority = settings.CMS_SITEMAP_DEFAULT_PRIORITY
    homepage_priority = settings.CMS_SITEMAP_HOMEPAGE_PRIORITY
    changefred = settings.CMS_SITEMAP_CHANGEFREQ

    def priority(self, obj):
        return self.homepage_priority if obj.page.is_home else self.default_priority


class CustomizedArticleSitemap(ArticleSitemap):
    """
    Publish Article sitemap with item priority depending from item state.

    Additionaly to the default Lotus article sitemap settings, this class supports
    option ``pinned_priority``and ``featured_priority`` that allow to define a specific
    priority depending the article is pinned, featured or not.
    """
    def priority(self, obj):
        if (
            settings.LOTUS_SITEMAP_ARTICLE_OPTIONS.get("pinned_priority") and
            obj.pinned is True
        ):
            return settings.LOTUS_SITEMAP_ARTICLE_OPTIONS.get("pinned_priority")

        if (
            settings.LOTUS_SITEMAP_ARTICLE_OPTIONS.get("featured_priority") and
            obj.featured is True
        ):
            return settings.LOTUS_SITEMAP_ARTICLE_OPTIONS.get("featured_priority")

        return settings.LOTUS_SITEMAP_ARTICLE_OPTIONS.get("priority")
