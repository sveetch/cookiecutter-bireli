import pytest

from cms.api import add_plugin
from cms.utils.urlutils import admin_reverse
from cms.models import Placeholder

from project_utils.tests import html_pyquery
from project_utils.factories import UserFactory
from project_utils.cms_tests import cms_page_create_helper

from project import _composer

# Skip tests if Request form app is not enabled from composer
if "request_form" in _composer.manifest.collection:
    from request_form.plugins.request import RequestPlugin
else:
    pytestmark = pytest.mark.skipif(True, reason="Request form is not enabled")


def test_form_view_add(db, client, settings):
    """
    Plugin creation form should return a success status code and every
    expected field should be present in HTML.
    """
    # Request to plugin form must be authenticated with a staff
    client.force_login(UserFactory(flag_is_superuser=True))

    # Get placeholder destination
    placeholder = Placeholder.objects.create(slot="content")

    # Get the edition plugin form url and open it
    url = admin_reverse("cms_placeholder_add_plugin")
    response = client.get(url, {
        "plugin_type": "RequestPlugin",
        "placeholder_id": placeholder.pk,
        "cms_path": "/{}/".format(settings.LANGUAGE_CODE),
        "plugin_language": settings.LANGUAGE_CODE,
        "plugin_position": 1,
    })

    # Expected http success status
    assert response.status_code == 200

    # Parse resulting plugin fields
    dom = html_pyquery(response)

    # There is currently no input except the internal ones from DjangoCMS
    assert sorted([
        item.get("name")
        for item in dom.find("#requestpluginmodel_form input")
    ]) == ["_popup", "_save", "csrfmiddlewaretoken"]


def test_render_in_page(db, client, settings):
    """
    Plugin should be properly rendered in a Page.
    """
    picsou = UserFactory(flag_is_superuser=True)
    client.force_login(picsou)

    # Create dummy page where to insert plugin
    page, content, version = cms_page_create_helper(
        "Foo",
        settings.TEST_PAGE_TEMPLATES["test-basic"],
        picsou,
        publish=True
    )

    # Get placeholder destination
    placeholder = page.get_placeholders(settings.LANGUAGE_CODE).get(slot="content")

    # Add plugin to page placeholder and publish
    add_plugin(
        placeholder,
        RequestPlugin,
        settings.LANGUAGE_CODE,
    )

    # Get the rendered page with expected plugin
    url = page.get_absolute_url(language=settings.LANGUAGE_CODE)
    response = client.get(url)
    # print()
    # print(response.content.decode())
    # print()

    # Request form should be here with its inputs
    dom = html_pyquery(response)
    assert len(dom.find(".request-form-plugin form")) == 1
    assert len(dom.find(".request-form-plugin form input")) > 1
