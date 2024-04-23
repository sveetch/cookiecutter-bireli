from django.urls import reverse

from project_utils.tests import html_pyquery
from project_utils.context_processors import project_globals


def test_project_globals_non_staff(db, client):
    """
    Project globals view should respond an error to non staff users.
    """
    response = client.get(reverse("project_utils:project-globals"), follow=True)
    assert response.redirect_chain == []
    assert response.status_code == 403


def test_project_globals_staff(db, admin_client):
    """
    Project globals view should respond properly to staff users.
    """
    response = admin_client.get(reverse("project_utils:project-globals"), follow=True)
    assert response.redirect_chain == []
    assert response.status_code == 200


def test_project_globals_content(db, admin_client):
    """
    Project globals should list some variables for SITE or PROJECT scope.
    """
    response = admin_client.get(reverse("project_utils:project-globals"), follow=True)
    assert response.redirect_chain == []
    assert response.status_code == 200

    dom = html_pyquery(response)

    variable_list = dom.find("#project-globals-variables tbody tr")

    # We vaguely check that there is more than two items with SITE and PROJECT items
    names = [
        item.cssselect("kbd")[0].text.replace(" ", "").replace("{{", "").replace(
            "}}", ""
        )
        for item in variable_list
        if (
            item.cssselect("kbd")[0].text.startswith("{{ SITE.") or
            item.cssselect("kbd")[0].text.startswith("{{ PROJECT.")
        )
    ]
    assert len(names) > 2


def test_project_globals_extra(db, rf, settings):
    """
    Context processor should include extra data if set from settings.
    """
    dummy_request = rf.get("/")

    data = project_globals(dummy_request)
    assert "EXTRA" not in data

    settings.EXTRA_PROJECT_GLOBALS = "foo"
    data = project_globals(dummy_request)
    assert "EXTRA" in data
    assert data["EXTRA"] == "foo"

    settings.EXTRA_PROJECT_GLOBALS = [1, 2, 3]
    data = project_globals(dummy_request)
    assert "EXTRA" in data
    assert data["EXTRA"] == [1, 2, 3]
