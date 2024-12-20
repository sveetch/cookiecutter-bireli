from cms.api import Page

from project_utils.factories import UserFactory
from project_utils.cms_tests import cms_page_create_helper

try:
    import two_factor  # noqa: F401,F403
except ImportError:
    IS_TWO_FACTOR_AVAILABLE = False
else:
    IS_TWO_FACTOR_AVAILABLE = True


def test_cms_create_page_root(db, settings, client):
    """
    This should correctly create a root page as expected from given arguments.
    """
    # Creating a page now require a valid user else it could be difficult to retrieve
    # it because of CMS queryset manager
    picsou = UserFactory(flag_is_admin=True)
    page, content, version = cms_page_create_helper(
        "Foo",
        settings.TEST_PAGE_TEMPLATES["test-basic"],
        picsou,
        reverse_id="foofoo",
        is_home=True
    )
    assert page.is_home is True
    assert page.reverse_id == "foofoo"
    assert page.get_slug(settings.LANGUAGE_CODE) == "foo"
    assert content.title == "Foo"
    assert version.state == "draft"

    # Get again the created page from db
    page = Page.objects.get_home()
    assert page.is_home is True
    assert page.reverse_id == "foofoo"
    assert page.get_slug(settings.LANGUAGE_CODE) == "foo"

    # New draft root page is only reachable from preview by admins
    response = client.get(
        page.get_absolute_url(settings.LANGUAGE_CODE),
        follow=True
    )

    expected_redirects = [
        ("/admin/cms/pagecontent/", 302),
        ("/admin/login/?next=/admin/cms/pagecontent/", 302),
    ]
    # Two factor append a third redirect to the front login
    if IS_TWO_FACTOR_AVAILABLE:
        expected_redirects.append(("/account/login/?next=/admin/cms/pagecontent/", 302))

    assert response.redirect_chain == expected_redirects
    assert response.status_code == 200

    # Publishing page is done through its last draft version and with a valid user
    version.publish(picsou)
    assert version.state == "published"

    # New draft root page is only reachable from preview by admins
    response = client.get(
        page.get_absolute_url(settings.LANGUAGE_CODE),
        follow=True
    )
    assert response.redirect_chain == []
    assert response.status_code == 200


def test_cms_factory_page_basic(db, settings, client):
    """
    This should correctly create a basic page as expected from given arguments.
    """
    picsou = UserFactory(flag_is_admin=True)
    page, content, version = cms_page_create_helper(
        "Foo",
        settings.TEST_PAGE_TEMPLATES["test-basic"],
        picsou,
    )
    assert page.is_home is False
    assert page.reverse_id is None
    assert page.get_slug(settings.LANGUAGE_CODE) == "foo"
    assert content.title == "Foo"
    assert version.state == "draft"

    response = client.get(
        page.get_absolute_url(settings.LANGUAGE_CODE),
        follow=True
    )
    assert response.redirect_chain == []
    assert response.status_code == 404

    # Publishing page is done through its last draft version and with a valid user
    version.publish(picsou)
    assert version.state == "published"

    # New draft root page is only reachable from preview by admins
    response = client.get(
        page.get_absolute_url(settings.LANGUAGE_CODE),
        follow=True
    )
    assert response.redirect_chain == []
    assert response.status_code == 200
