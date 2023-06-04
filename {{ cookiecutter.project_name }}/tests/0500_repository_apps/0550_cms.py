import factory

from cms.api import Page

from project_utils.factories import PageFactory


def test_cms_factory_page_root(db, settings, client):
    """
    PageFactory should correctly create a root page as expected from given arguments.
    """
    with factory.debug():
        PageFactory(
            should_publish=True,
            template=settings.TEST_PAGE_TEMPLATES["test-basic"],
            set_homepage=True,
            in_navigation=True,
            reverse_id="foofoo",
            title__title="Foo",
            title__language=settings.LANGUAGE_CODE,
        )

    page = Page.objects.get_home()

    assert page.get_title() == "Foo"
    assert page.get_slug() == "foo"
    assert page.reverse_id == "foofoo"
    assert page.is_published(settings.LANGUAGE_CODE) is True

    # New root page is reachable
    response = client.get(page.get_absolute_url(settings.LANGUAGE_CODE), follow=True)
    assert response.redirect_chain == []
    assert response.status_code == 200


def test_cms_factory_page_basic(db, settings, client):
    """
    PageFactory should correctly create a basic page as expected from given arguments.
    """
    created = PageFactory(
        template=settings.TEST_PAGE_TEMPLATES["test-basic"],
        title__title="Foo",
    )

    page = Page.objects.get(pk=created.id)

    assert page.get_title() == "Foo"
    assert page.get_slug() == "foo"
    assert page.reverse_id is None
    assert page.is_published(settings.LANGUAGE_CODE) is False

    # New page is not reachable since it is not published by default from factory
    response = client.get(page.get_absolute_url(settings.LANGUAGE_CODE), follow=True)
    assert response.redirect_chain == []
    assert response.status_code == 404


def test_cms_factory_page_auto_reverseid(db, settings, client):
    """
    Giving "True" to reverse_id post generator will automatically adopt the slug value
    as the reverse id.
    """
    created = PageFactory(
        template=settings.TEST_PAGE_TEMPLATES["test-basic"],
        title__title="Foo",
        reverse_id=True,
    )

    page = Page.objects.get(pk=created.id)

    assert page.get_title() == "Foo"
    assert page.get_slug() == "foo"
    assert page.reverse_id == "foo"
