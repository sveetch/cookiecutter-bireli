from django.urls import reverse


def test_prototypes(db, client):
    """
    Staticpage prototypes index should respond with success.
    """
    response = client.get(reverse("prototypes-index"), follow=True)

    assert response.redirect_chain == []
    assert response.status_code == 200
