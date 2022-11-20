from django.urls import reverse


def test_fobi_dashboard(db, client, admin_client):
    """
    Fobi dashboard should respond with success to admin users only.
    """
    url = reverse("fobi.dashboard")

    response = client.get(url, follow=True)

    assert response.redirect_chain == []
    assert response.status_code == 403

    response = admin_client.get(url, follow=True)

    assert response.redirect_chain == []
    assert response.status_code == 200
