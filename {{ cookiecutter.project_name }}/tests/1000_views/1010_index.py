from django.urls import reverse


def test_static_index(db, client):
    """
    Default dummy index view should respond with success.
    """
    response = client.get(reverse("index"), follow=True)

    assert response.redirect_chain == []
    assert response.status_code == 200


def test_styleguide(db, client):
    """
    Styleguide should respond with success.
    """
    response = client.get(reverse("styleguide:index"), follow=True)

    assert response.redirect_chain == []
    assert response.status_code == 200
