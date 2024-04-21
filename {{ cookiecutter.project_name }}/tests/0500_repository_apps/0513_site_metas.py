from django.urls import reverse

from project_utils.tests import html_pyquery


def test_site_metas_non_staff(db, client):
    """
    Site metas view should respond an error to non staff users.
    """
    response = client.get(reverse("project_utils:site-metas"), follow=True)
    assert response.redirect_chain == []
    assert response.status_code == 403


def test_site_metas_staff(db, admin_client):
    """
    Site metas view should respond properly to staff users.
    """
    response = admin_client.get(reverse("project_utils:site-metas"), follow=True)
    assert response.redirect_chain == []
    assert response.status_code == 200


def test_site_metas_content(db, admin_client):
    """
    Site metas should list some variables for SITE or PROJECT scope.
    """
    response = admin_client.get(reverse("project_utils:site-metas"), follow=True)
    assert response.redirect_chain == []
    assert response.status_code == 200

    dom = html_pyquery(response)

    variable_list = dom.find("#site-metas-variables tbody tr")

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
