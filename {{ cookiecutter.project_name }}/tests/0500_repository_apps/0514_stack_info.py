from django.urls import reverse

from project_utils.factories import UserFactory


def test_stack_info_anonymous_redirected(admin_client, client, db):
    """
    Stack info view should redirect anonymous and non staff users to login and finally
    respond properly to authenticated staff users.
    """
    # For anonymous
    url = reverse("project_utils:stack-info")
    response = client.get(url)
    assert response.status_code == 302
    assert "/admin/login/" in response.url

    # For authenticated but non staff users
    user = UserFactory()
    client.force_login(user)
    url = reverse("project_utils:stack-info")
    response = client.get(url)
    assert response.status_code == 302

    # For staff users
    url = reverse("project_utils:stack-info")
    response = admin_client.get(url)
    assert response.status_code == 200


def test_stack_info_python_version_in_context(db, admin_client):
    """
    Stack info view should include python_version in context.
    """
    url = reverse("project_utils:stack-info")
    response = admin_client.get(url)
    assert "python_version" in response.context
    assert response.context["python_version"] is not None


def test_stack_info_python_packages_in_context(db, admin_client):
    """
    Stack info view should include python_packages in context.
    """
    url = reverse("project_utils:stack-info")
    response = admin_client.get(url)
    assert "python_packages" in response.context
    packages = response.context["python_packages"]
    assert isinstance(packages, list)
    assert len(packages) > 0
    assert "name" in packages[0]
    assert "version" in packages[0]


def test_stack_info_django_version_in_context(db, admin_client):
    """
    Stack info is not involved here since Django version is a builtin in any Django
    context.
    """
    url = reverse("project_utils:stack-info")
    response = admin_client.get(url)
    assert "django_version" in response.context
    assert response.context["django_version"] is not None


def test_stack_info_node_info_in_context(db, admin_client):
    """
    Stack info view should include node_info in context.
    """
    url = reverse("project_utils:stack-info")
    response = admin_client.get(url)
    assert "node_info" in response.context
    node_info = response.context["node_info"]
    assert "node_version" in node_info
    assert "npm_version" in node_info
    assert "packages" in node_info


def test_stack_info_node_packages_from_package_json(db, admin_client):
    """
    Stack info view should include Node packages from package.json.
    """
    url = reverse("project_utils:stack-info")
    response = admin_client.get(url)
    node_info = response.context["node_info"]
    # Should have packages from package.json
    assert isinstance(node_info["packages"], list)
    if node_info["packages"]:
        pkg = node_info["packages"][0]
        assert "name" in pkg
        assert "version" in pkg
        assert "dev" in pkg
