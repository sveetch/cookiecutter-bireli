import pytest

from django.urls import reverse

@pytest.mark.skip
def test_static_index(db, client):
    """
    Pinging the root url whatever it is, should respond with success.

    NOTE:

        Currently skipped since test site is empty and so the CMS ask to login to
        create the root page which is not relevant for a ping test, at least not in
        this form.
    """
    response = client.get("/", follow=True)

    assert response.redirect_chain == []
    assert response.status_code == 200


@pytest.mark.skip
def test_ping_cms_home(db, client):
    """
    GET request on cms page root index should succeed

    NOTE:

        Dedicated test to the CMS root page, efficient but strictly related to CMS.
        However it won't work correctly without any inital datas (it will succeed but
        don't see it has been redirected to login).
    """
    response = client.get(reverse("pages-root"))
    assert response.status_code == 200


def test_styleguide(db, client):
    """
    Styleguide should respond with success.
    """
    response = client.get(reverse("styleguide:index"), follow=True)

    assert response.redirect_chain == []
    assert response.status_code == 200


def test_prototypes(db, client):
    """
    Staticpage prototypes index should respond with success.
    """
    response = client.get(reverse("prototypes-index"), follow=True)

    assert response.redirect_chain == []
    assert response.status_code == 200
