"""
NOTE: Since the initials datas may change from a project to another, those tests try
to make the less assumptions possible on initial datas.
"""
import logging

import pytest

from cms.api import Page
from cms.utils import get_current_site

from project_utils.exceptions import InitialDataLoaderException
from project_utils.initial_loader import InitialDataLoader
from project_utils.user import safe_get_user_model


def test_cms_demomaker_blank(caplog, db):
    """
    Without pages involved there is no requirement.
    """
    caplog.set_level(logging.DEBUG, logger="project-utils")

    maker = InitialDataLoader()
    maker.create({})

    User = safe_get_user_model()

    assert User.objects.count() == 0
    assert Page.objects.count() == 0


@pytest.mark.parametrize("structure, expected", [
    # Empty default template
    (
        {
            "global_author": "guest",
            "users": {
                "guest": {},
            },
            "pages": [{
                "key": "homepage",
                "name": "Demo homepage",
                "is_homepage": True,
            }],
        },
        "A template path cannot be empty.",
    ),
    # Invalid default template
    (
        {
            "global_author": "guest",
            "default_template": "foo.html",
            "users": {
                "guest": {},
            },
            "pages": [{
                "key": "homepage",
                "name": "Demo homepage",
                "is_homepage": True,
            }],
        },
        (
            "Given template path is not registered from 'settings.CMS_TEMPLATES': "
            "foo.html"
        ),
    ),
    # Empty global author
    (
        {
            "default_template": "pages/single_column.html",
            "users": {
                "guest": {},
            },
            "pages": [{
                "key": "homepage",
                "name": "Demo homepage",
                "is_homepage": True,
            }],
        },
        "No 'global_author' have been given despite it is required."
    ),
    # Invalid global author username
    (
        {
            "global_author": "nope",
            "default_template": "pages/single_column.html",
            "users": {
                "guest": {},
            },
            "pages": [{
                "key": "homepage",
                "name": "Demo homepage",
                "is_homepage": True,
            }],
        },
        "Unable to find created user for global author username 'nope'."
    ),
    # Empty page key
    (
        {
            "global_author": "guest",
            "default_template": "pages/single_column.html",
            "users": {
                "guest": {},
            },
            "pages": [{
                "name": "Demo homepage",
                "is_homepage": True,
            }],
        },
        "A page must define a non empty 'key' item."
    ),
    # Invalid page key
    (
        {
            "global_author": "guest",
            "default_template": "pages/single_column.html",
            "users": {
                "guest": {},
            },
            "pages": [{
                "key": "L'été",
                "name": "Demo homepage",
                "is_homepage": True,
            }],
        },
        (
            "The 'key' item must be a valid identifier consisting of letters, "
            "numbers, underscores or hyphens. Given one is invalid: L'été"
        )
    ),
    # Empty page name
    (
        {
            "global_author": "guest",
            "default_template": "pages/single_column.html",
            "users": {
                "guest": {},
            },
            "pages": [{
                "key": "homepage",
                "is_homepage": True,
            }],
        },
        "A page must define a non empty 'name' item."
    ),
    # Invalid page template
    (
        {
            "global_author": "guest",
            "default_template": "pages/single_column.html",
            "users": {
                "guest": {},
            },
            "pages": [{
                "key": "homepage",
                "name": "Demo homepage",
                "template": "foo.html",
                "is_homepage": True,
            }],
        },
        (
            "Given template path is not registered from 'settings.CMS_TEMPLATES': "
            "foo.html"
        ),
    ),
    # Missing homepage declaration
    (
        {
            "global_author": "guest",
            "default_template": "pages/single_column.html",
            "users": {
                "guest": {},
            },
            "pages": [{
                "key": "homepage",
                "name": "Demo homepage",
            }],
        },
        (
            "At least one homepage is required, given structure got none."
        ),
    ),
    # Multiple homepage declarations
    (
        {
            "global_author": "guest",
            "default_template": "pages/single_column.html",
            "users": {
                "guest": {},
            },
            "pages": [
                {
                    "key": "homepage",
                    "name": "Demo homepage",
                    "is_homepage": True,
                    "children": [{
                        "key": "foo",
                        "name": "Foo",
                        "is_homepage": True,
                    }]
                }
            ],
        },
        (
            "Only a single page with 'is_homepage' is allowed but given structure "
            "got 2 pages with this option enabled."
        ),
    ),
])
def test_cms_demomaker_validatons(caplog, db, structure, expected):
    """
    DemoMake should raise an exception 'InitialDataLoaderException' for invalid
    structure values.
    """
    caplog.set_level(logging.DEBUG, logger="project-utils")

    maker = InitialDataLoader()

    with pytest.raises(InitialDataLoaderException) as exc_info:
        maker.create(structure)

    assert exc_info.value.args[0] == expected


def test_cms_demomaker_success(caplog, db):
    """
    InitialDataLoader should correctly create all objects from given structure.
    """
    caplog.set_level(logging.DEBUG, logger="project-utils")

    maker = InitialDataLoader()
    maker.create({
        "global_author": "admin",
        "default_template": "pages/single_column.html",
        "site": {
            "name": "Demo",
            "domain": "127.0.0.8001",
        },
        "users": {
            "guest": {},
            "superuser": {
                "status": "superuser",
            },
            "admin": {
                "status": "admin",
                "first_name": "Admin",
                "last_name": "Staff",
                "email": "support@mail.com",
                "password": "ok",
            },
        },
        "pages": [
            {
                "key": "homepage",
                "name": "Demo homepage",
                "is_homepage": True,
                "template": None,
                "children": [
                    {
                        "key": "foo",
                        "name": "Foo",
                        "children": [
                            {
                                "key": "bar",
                                "name": "Bar",
                                "children": []
                            },
                        ]
                    },
                ],
            },
            {
                "key": "plop_plop-plop",
                "name": "Plop",
            },
        ]
    })

    site = get_current_site()
    assert site.name == "Demo"
    assert site.domain == "127.0.0.8001"

    # All user have been created with their respected staff level
    User = safe_get_user_model()
    assert User.objects.count() == 3
    assert User.objects.filter(is_staff=True).count() == 2
    assert User.objects.filter(is_superuser=True).count() == 1

    # All pages have a published and draft version, homepage have been set correctly
    assert Page.objects.count() == 8
    assert Page.objects.public().count() == 4
    assert Page.objects.get_home().get_title() == "Demo homepage"


def test_cms_demomaker_fixture(caplog, db, load_initials):
    """
    The Pytest fixture should load the initial data.

    We just check some content have been created with success but without to check the
    contents themselves.

    This assumes there is at least a created user and page, nothing more so the
    initials data may be changed.

    NOTE: This won't be safe for project without CMS.
    """
    caplog.set_level(logging.DEBUG, logger="project-utils")

    User = safe_get_user_model()
    assert User.objects.count() > 0

    assert Page.objects.count() > 0
