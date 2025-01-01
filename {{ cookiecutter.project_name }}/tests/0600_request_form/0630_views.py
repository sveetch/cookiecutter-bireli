import pytest

from django.urls import reverse

from project_utils.tests import html_pyquery

from project import _composer

# Skip tests if Request form app is not enabled from composer
if "request_form" in _composer.manifest.collection:
    from request_form.models import RequestModel
else:
    pytestmark = pytest.mark.skipif(True, reason="Request form is not enabled")


def test_initial_form_view(client, db, settings):
    """
    View should respond with success and contain the form.
    """
    url = reverse("request_form:request-form")

    response = client.get(url, follow=True)
    assert response.redirect_chain == []
    assert response.status_code == 200

    # from project_utils.tests import decode_response_or_string
    # print(decode_response_or_string(response))
    dom = html_pyquery(response)
    assert len(dom.find("#request-form")) == 1


def test_initial_success_view(client, db, settings):
    """
    Just ensure the static view is responding with success.
    """
    url = reverse("request_form:request-success")

    response = client.get(url, follow=True)
    assert response.redirect_chain == []
    assert response.status_code == 200


def test_post_valid(client, db, mailoutbox, settings):
    """
    View should respond to POST request and save form request when it is valid.

    Also check the ip_address field is correctly filled.
    """
    request_form = {
        "subject": "ENTREPRISE",
        "first_name": "Edward",
        "last_name": "Snowden",
        "phone": "+33 1 48 74 52 32",
        "email": "ed@snowden.com",
        "message": "Hello, world!",
        "data_confidentiality_policy": True,
        "g-recaptcha-response": "PASSED",
    }

    response = client.post(
        reverse("request_form:request-form"),
        request_form,
        follow=True
    )
    assert response.redirect_chain == [
        (reverse("request_form:request-success"), 302)
    ]
    assert response.status_code == 200
    assert RequestModel.objects.count() == 1

    request = RequestModel.objects.all()[0]
    assert request.ip_address == "127.0.0.1"

    assert len(mailoutbox) == 1

    m = mailoutbox[0]
    assert m.subject == "Website request form"


def test_post_invalid(client, db, settings):
    """
    View should respond to POST request and raise field errors when form request is
    invalid.
    """
    response = client.post(reverse("request_form:request-form"), {}, follow=True)
    assert response.redirect_chain == []
    assert response.status_code == 200
    assert RequestModel.objects.count() == 0

    dom = html_pyquery(response)
    # print(response.content.decode("utf-8"))
    assert len(dom.find("#request-form .form-control.is-invalid")) > 1


def test_post_valid_no_db_save(client, db, mailoutbox, settings):
    """
    View should respond to POST request, ignore object save form but still sending
    email.
    """
    settings.REQUEST_SAVE_TO_DB = False

    request_form = {
        "subject": "ENTREPRISE",
        "first_name": "Edward",
        "last_name": "Snowden",
        "phone": "+33 1 48 74 52 32",
        "email": "ed@snowden.com",
        "message": "Hello, world!",
        "data_confidentiality_policy": True,
        "g-recaptcha-response": "PASSED",
    }

    response = client.post(
        reverse("request_form:request-form"),
        request_form,
        follow=True
    )
    assert response.redirect_chain == [
        (reverse("request_form:request-success"), 302)
    ]
    assert response.status_code == 200
    assert RequestModel.objects.count() == 0

    assert len(mailoutbox) == 1

    m = mailoutbox[0]
    assert m.subject == "Website request form"
