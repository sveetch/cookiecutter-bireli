import pytest

from django.urls import reverse


@pytest.mark.parametrize("urlname", [
    "admin:index",
])
def test_ping_admin_views(admin_client, urlname):
    """
    GET request on django admin views should succeed without login redirect response.

    Purpose is to check that critical admin parts are alive and ready to use.
    """
    response = admin_client.get(reverse(urlname), follow=True)
    assert response.redirect_chain == []
    assert response.status_code == 200
