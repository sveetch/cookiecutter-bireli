from django.urls import reverse


def test_styleguide(db, client):
    """
    Styleguide should respond with success.
    """
    response = client.get(reverse("styleguide:index"), follow=True)

    assert response.redirect_chain == []
    assert response.status_code == 200
