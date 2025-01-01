import pytest

from project_utils.tests import flatten_form_errors

from project import _composer

# Skip tests if Request form app is not enabled from composer
if "request_form" in _composer.manifest.collection:
    from request_form.forms import RequestForm
    from request_form.models import RequestModel
else:
    pytestmark = pytest.mark.skipif(True, reason="Request form is not enabled")


def test_subject_empty(settings):
    """
    When there is no subject defined from setting the form should not includes the
    field 'subject'.
    """
    settings.REQUEST_SUBJECTS = {}

    f = RequestForm({})
    assert ("subject" in f.fields) is False


def test_subject_filled(settings):
    """
    When there is some subject defined from setting (as from the test environment
    settings do) the form should includes the field 'subject'.
    """
    f = RequestForm({})
    assert ("subject" in f.fields) is True


def test_empty(db, settings):
    """
    Empty form should not be valid because of required fields.
    """
    f = RequestForm({})

    validation = f.is_valid()
    assert validation is False
    assert flatten_form_errors(f) == {
        "first_name": ["This field is required."],
        "last_name": ["This field is required."],
        "email": ["This field is required."],
        "message": ["This field is required."],
        "data_confidentiality_policy": ["You must accept data confidentiality policy."],
        "captcha": ["This field is required."],
    }
    assert RequestModel.objects.count() == 0


def test_invalid(db, settings):
    """
    Invalid field values should raises specific errors.
    """
    f = RequestForm({
        "subject": "",
        "first_name": "Vladimir",
        "last_name": "Botchneko",
        "phone": "+1 604-401-1234",
        "email": "plop@mail.ru",
        "message": "Lorem Самовольная ipsum",
        "data_confidentiality_policy": False,
        "captcha_0": "foo",
        "captcha_1": "bar",
    })

    validation = f.is_valid()
    assert validation is False

    # import json
    # print(json.dumps(flatten_form_errors(f), indent=4))

    assert flatten_form_errors(f) == {
        "phone": ["The phone number entered is not valid."],
        "email": ["This email address isn't allowed."],
        "message": ["Cyrillic characters are not allowed."],
        "data_confidentiality_policy": ["You must accept data confidentiality policy."],
        "captcha": ["This field is required."],
    }


def test_valid(client, db, mailoutbox, settings):
    """
    Form should save request object and send email if enabled.
    """
    settings.REQUEST_FROM_EMAIL = "donald@localhost"
    settings.REQUEST_MAIL_DEFAULT_RECIPIENTS = ("default@localhost",)
    settings.REQUEST_EMAIL_SUBJECT = "Entreprise"

    f = RequestForm({
        "subject": "ENTREPRISE",
        "first_name": "Edward",
        "last_name": "Snowden",
        "phone": "+33 1 48 74 52 32",
        "email": "ed@snowden.com",
        "message": "Hello, world!",
        "data_confidentiality_policy": True,
        "g-recaptcha-response": "PASSED",
    }, request_ip_address="127.0.0.1")
    validation = f.is_valid()
    assert validation is True

    f.save()
    assert RequestModel.objects.count() == 1

    assert len(mailoutbox) == 1

    m = mailoutbox[0]
    assert m.subject == "Entreprise"
    assert m.from_email == "donald@localhost"
    assert list(m.to) == ["Entreprise@localhost"]
    assert m.body == "\n".join([
        "You have a new request from your site:",
        "",
        "Object: Entreprise",
        "First name: Edward",
        "Last name: Snowden",
        "E-mail: ed@snowden.com",
        "Phone: 01 48 74 52 32",
        "",
        "Message:",
        "Hello, world!",
        "",
    ])


def test_valid_no_email_sending(client, db, mailoutbox, settings):
    """
    Form should save request object without sending email if disabled.
    """
    # Empty recipient adress disable email sending.
    settings.REQUEST_MAIL_DEFAULT_RECIPIENTS = None

    f = RequestForm({
        "subject": "ENTREPRISE",
        "first_name": "Edward",
        "last_name": "Snowden",
        "phone": "+33 1 48 74 52 32",
        "email": "ed@snowden.com",
        "message": "Hello, world!",
        "data_confidentiality_policy": True,
        "g-recaptcha-response": "PASSED",
    }, request_ip_address="127.0.0.1")
    validation = f.is_valid()
    assert validation is True

    f.save()
    assert RequestModel.objects.count() == 1

    assert len(mailoutbox) == 0


def test_valid_no_db_save(client, db, mailoutbox, settings):
    """
    Form should not save request object but still send email if enabled.
    """
    settings.REQUEST_FROM_EMAIL = "donald@localhost"
    settings.REQUEST_MAIL_DEFAULT_RECIPIENTS = ("default@localhost",)
    settings.REQUEST_EMAIL_SUBJECT = "Entreprise"
    settings.REQUEST_SAVE_TO_DB = False

    f = RequestForm({
        "subject": "ENTREPRISE",
        "first_name": "Edward",
        "last_name": "Snowden",
        "phone": "+33 1 48 74 52 32",
        "email": "ed@snowden.com",
        "message": "Hello, world!",
        "data_confidentiality_policy": True,
        "g-recaptcha-response": "PASSED",
    }, request_ip_address="127.0.0.1")
    validation = f.is_valid()
    assert validation is True

    f.save()
    assert RequestModel.objects.count() == 0

    assert len(mailoutbox) == 1

    m = mailoutbox[0]
    assert m.subject == "Entreprise"
    assert m.from_email == "donald@localhost"
    assert list(m.to) == ["Entreprise@localhost"]
    assert m.body == "\n".join([
        "You have a new request from your site:",
        "",
        "Object: Entreprise",
        "First name: Edward",
        "Last name: Snowden",
        "E-mail: ed@snowden.com",
        "Phone: 01 48 74 52 32",
        "",
        "Message:",
        "Hello, world!",
        "",
    ])
