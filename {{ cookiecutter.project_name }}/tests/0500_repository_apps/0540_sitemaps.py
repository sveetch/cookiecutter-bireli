import lxml.etree

from django.contrib.sites.models import Site
from django.urls import reverse

from lotus.choices import STATUS_DRAFT
from lotus.factories import ArticleFactory

from project_utils.factories import PageFactory


def test_sitemap_index(db, settings, client):
    """
    Sitemap index should list all enabled sitemap sections, no matter there is
    content or not.
    """
    current_site = Site.objects.get_current()
    base_url = "http://{}".format(current_site.domain)

    # Just add a single CMS page but no Lotus object
    PageFactory(
        template=settings.TEST_PAGE_TEMPLATES["test-basic"],
        title__title="Foo",
        should_publish=True,
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

    foo = PageFactory(
        template=settings.TEST_PAGE_TEMPLATES["test-basic"],
        title__title="Foo",
        should_publish=True,
    )
    bar = PageFactory(
        template=settings.TEST_PAGE_TEMPLATES["test-basic"],
        title__title="Bar",
        should_publish=True,
    )
    PageFactory(
        template=settings.TEST_PAGE_TEMPLATES["test-basic"],
        title__title="Nope",
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
        base_url + foo.get_absolute_url(settings.LANGUAGE_CODE),
        base_url + bar.get_absolute_url(settings.LANGUAGE_CODE),
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
