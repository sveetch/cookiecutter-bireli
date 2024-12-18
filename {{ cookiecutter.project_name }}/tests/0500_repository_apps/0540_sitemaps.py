import lxml.etree

from django.contrib.sites.models import Site
from django.urls import reverse

from lotus.choices import STATUS_DRAFT
from lotus.factories import ArticleFactory

from project_utils.factories import UserFactory
from project_utils.cms_tests import cms_page_create_helper


def test_sitemap_index(db, settings, client):
    """
    Sitemap index should list all enabled sitemap sections, no matter there is
    content or not.
    """
    current_site = Site.objects.get_current()
    base_url = "http://{}".format(current_site.domain)

    # Just add a single CMS page but no Lotus object
    picsou = UserFactory(flag_is_admin=True)
    page, content, version = cms_page_create_helper(
        "Foo",
        settings.TEST_PAGE_TEMPLATES["test-basic"],
        picsou,
        publish=True
    )

    url = reverse("project_sitemaps:sitemap-index")
    response = client.get(url)
    assert response.status_code == 200

    # Parse XML to get url items
    tree = lxml.etree.fromstring(response.content)
    found_urls = [
        url
        for url in tree.xpath("//urlset:loc/text()", namespaces={
            "urlset": "http://www.sitemaps.org/schemas/sitemap/0.9",
        })
    ]

    assert found_urls == [
        base_url + reverse("project_sitemaps:sitemap-section", kwargs={
            "section": "cms",
        }),
        base_url + reverse("project_sitemaps:sitemap-section", kwargs={
            "section": "lotus-article",
        }),
    ]


def test_sitemap_cms(db, settings, client):
    """
    CMS sitemap should return all published pages.
    """
    current_site = Site.objects.get_current()
    base_url = "http://{}".format(current_site.domain)

    picsou = UserFactory(flag_is_admin=True)
    foo_page, foo_content, foo_version = cms_page_create_helper(
        "Foo",
        settings.TEST_PAGE_TEMPLATES["test-basic"],
        picsou,
        publish=True
    )
    bar_page, bar_content, bar_version = cms_page_create_helper(
        "Bar",
        settings.TEST_PAGE_TEMPLATES["test-basic"],
        picsou,
        publish=True
    )
    cms_page_create_helper(
        "Nope",
        settings.TEST_PAGE_TEMPLATES["test-basic"],
        picsou,
    )

    url = reverse("project_sitemaps:sitemap-section", kwargs={
        "section": "cms",
    })
    response = client.get(url)
    assert response.status_code == 200

    # Parse XML to get url items
    tree = lxml.etree.fromstring(response.content)
    found_urls = [
        url
        for url in tree.xpath("//urlset:loc/text()", namespaces={
            "urlset": "http://www.sitemaps.org/schemas/sitemap/0.9",
        })
    ]

    assert found_urls == [
        base_url + foo_page.get_absolute_url(settings.LANGUAGE_CODE),
        base_url + bar_page.get_absolute_url(settings.LANGUAGE_CODE),
    ]


def test_sitemap_lotus(db, client):
    """
    Lotus article sitemap should return all published articles.
    """
    current_site = Site.objects.get_current()
    base_url = "http://{}".format(current_site.domain)

    ArticleFactory(
        title="Draft",
        slug="draft",
        status=STATUS_DRAFT,
    )
    published = ArticleFactory(
        title="Simply published",
        slug="simply-published",
    )
    published_bis = ArticleFactory(
        title="Published bis",
        slug="published-bis",
    )

    url = reverse("project_sitemaps:sitemap-section", kwargs={
        "section": "lotus-article",
    })
    response = client.get(url)
    assert response.status_code == 200

    # Parse XML to get url items
    tree = lxml.etree.fromstring(response.content)
    found_urls = [
        url
        for url in tree.xpath("//urlset:loc/text()", namespaces={
            "urlset": "http://www.sitemaps.org/schemas/sitemap/0.9",
        })
    ]

    assert found_urls == [
        base_url + published_bis.get_absolute_url(),
        base_url + published.get_absolute_url(),
    ]
