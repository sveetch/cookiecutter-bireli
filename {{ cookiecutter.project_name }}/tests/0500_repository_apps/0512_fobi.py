import pytest

from django.urls import reverse


try:
    import fobi
except ImportError:
    fobi_is_available = False
else:
    fobi_is_available = True

# Skip marker decorator for tests depending on a Fobi installation
fobi_skip = pytest.mark.skipif(
    fobi_is_available is False,
    reason="Fobi is not installed"
)


@fobi_skip
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
