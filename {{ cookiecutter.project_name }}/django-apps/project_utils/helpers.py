"""

Expected data structure
***********************

    {
        "global_author": "emencia",
        "default_template": "pages/single_column.html",
        "site": {
            "name": "Demo",
            "domain": "127.0.0.8001",
        },
        "users": {
            "emencia": {
                "first_name": "Anne",
                "last_name": "Nonymous",
                "email": "my@email.com",
                "password": "ok",
            },
        },
        "pages": {
            "key": "homepage",
            "name": "Homepage",
            "template": None,
            "children": [
                {
                    "key": "foo",
                    "name": "Foo",
                    "children": []
                },
            ],
        },
    }


Structure description
*********************

Site, users and pages parts are not required, but if you define some page items, at
least one user is required.

global_author
    The username to retrieve from created users and that will be assigned to every
    objects which depends from a User object. This is required.
default_template
    The default template path to use for created Page when they don't define a specific
    one. This is required.
site
    An optional dictionnary with items ``name`` and ``domain`` to update the current
    Site object. Both items are strings and optionals.
users
    A dictionnary of user items to create. Each item is an user, user keyname will be
    used for the username and user values ``first_name``, ``last_name``, ``email`` and
    ``password`` are all strings and optional to fill the User object. Empty user
    values are automatically filled with random content. Default password is
    ``secret``.

    Additionally, user item can have a ``status`` value that is either ``admin`` or
    ``superuser`` to set its status level, any other value assume the user is a basic
    user without any staff level.

    At least a single user is required and its username must match the
    ``global_author`` value, all pages will be assigned to this user object.
pages
    A dictionnary of page items to create. Each page item can define children page
    items to reproduce a proper page tree.

    A page item expected the following fields:

    * key: A valid page identifier used for the page slug and its reverse id (all page
      will have a reverse id). This is required;
    * name: The page title to set. This is required;
    * template: Optional specific template path to use instead of the default one from
      ``default_template``.

    All created pages are published and set to appear in navigation.

.. Note::
    Any page template path must be a registered template from
    ``settings.CMS_TEMPLATES``.


Flexbility note
***************

Currently this is hardly coupled to Django site, Django auth and CMS. This is not
really flexible and will be broken if CMS is not enabled.

This can be improved by splitting DemoMaker into application parts managed by
project-composer.

"""
from django.conf import settings
from django.core.validators import slug_re

from cms.utils import get_current_site

from .exceptions import DemoMakerException
from .factories import PageFactory, UserFactory
from .logging import BaseOutput


class DemoMaker:
    """
    Helper class that will create implemented objects from a given structure.

    All objects that need a language code are created using the default project
    language from ``settings.LANGUAGE_CODE``. No multilingual objects are supported.

    Keyword Arguments:
        output_interface (class): Class to manage logging output. It must implement
            an interface like ``project_utils.logging.BaseOutput``. Default is to use
            ``BaseOutput`` which use Python logging.

    Attributes:
        log (object): Logging output manager as defined from ``output_interface``.
    """
    def __init__(self, output_interface=None):
        self.log = output_interface or BaseOutput()

    def validate_global_author(self):
        """
        Validate global author value is valid.
        """
        if not self.global_author:
            msg = "No 'global_author' have been given despite it is required."
            raise DemoMakerException(msg)

        if isinstance(self.global_author, str):
            msg = "Unable to find created user for global author username '{}'."
            raise DemoMakerException(msg.format(self.global_author))

        return True

    def validate_page_data(self, data):
        """
        Validate page data is valid.

        Arguments:
            data (dict): Page item data.
        """
        if not data.get("key"):
            msg = "A page must define a non empty 'key' item."
            raise DemoMakerException(msg)

        if not slug_re.match(data["key"]):
            msg = (
                "The 'key' item must be a valid identifier consisting of letters, "
                "numbers, underscores or hyphens. Given one is invalid: {}"
            )
            raise DemoMakerException(msg.format(data["key"]))

        if not data.get("name"):
            msg = "A page must define a non empty 'name' item."
            raise DemoMakerException(msg)

        return True

    def validate_page_template(self, template, can_be_empty=False):
        """
        Validate page template is valid.

        Arguments:
            template (string): Template path.

        Keyword Arguments:
            can_be_empty (boolean): If True, the template path is allowed to be empty.
                Default to False, path must never be empty.
        """
        if not can_be_empty and not template:
            msg = "A template path cannot be empty."
            raise DemoMakerException(msg)

        if template not in [k for k, v in settings.CMS_TEMPLATES]:
            msg = (
                "Given template path is not registered from "
                "'settings.CMS_TEMPLATES': {}"
            )
            raise DemoMakerException(msg.format(template))

        return True

    def site_update(self, data):
        """
        Update current site fields

        Arguments:
            data (dict): Site data.
        """
        if data.get("domain") or data.get("name"):
            self.log.info("- Editing site object")
            site = get_current_site()
            site.name = data.get("name") or site.name
            site.domain = data.get("domain") or site.domain
            site.save()

        return site

    def user_creation(self, data):
        """
        Create all user items and assign an user as the global author if it match
        username from 'global_author'.

        Arguments:
            data (dict): User item data.
        """
        created = []

        for username, fields in data.items():
            self.log.info("- Creating user: {}".format(username))
            payload = {"username": username}

            status = fields.pop("status", "user")
            if status == "superuser":
                payload["flag_is_superuser"] = True
            elif status == "admin":
                payload["flag_is_admin"] = True

            payload.update(fields)
            user = UserFactory(**payload)
            created.append(user)

            if user.username == self.global_author:
                self.global_author = user

        return created

    def page_creation(self, data, parent=None, level=0, created=[]):
        """
        Recursively create the page tree

        Arguments:
            data (dict): Page item data.

        Keyword Arguments:
            parent (cms.models.Page): Parent page that current page will be related to.
            level (integer): Page level in the CMS tree. Zero is the level for the
                root page.
            created (list): List where to append all created page objects.
        """
        self.validate_page_data(data)

        key = data["key"]
        self.log.info("- Creating page: {name}".format(
            name=key,
        ))

        payload = {"title__title": data["name"]}

        # Compute field values
        payload.update({
            "user": self.global_author,
            "parent": parent,
            "reverse_id": key,
            "set_homepage": True if level == 0 else False,
            "should_publish": True,
            "in_navigation": True,
            "title__language": settings.LANGUAGE_CODE,
            "title__slug": key,
            "template": data.get("template") or self.default_template,
        })

        self.validate_page_template(payload["template"])

        page = PageFactory(**payload)
        created.append(page)

        level =+ 1
        for child in data.get("children", []):
            self.page_creation(child, parent=page, level=level)

        return created

    def create(self, structure):
        """
        Create all objects from given data structure.

        Arguments:
            structure (dict): Dictionnary of data structure. See *Expected data
                structure* and *Structure description* documentation for details.
        """
        self.global_author = structure.get("global_author")
        self.default_template = structure.get("default_template")

        if structure.get("site"):
            self.site_update(structure["site"])

        if structure.get("users"):
            users = self.user_creation(structure["users"])
            self.log.info("* Created {} user(s)".format(len(users)))

        # Validate global_author after users have been processed and before process
        # which use it. Currently only executed if there is some page to create.
        if structure.get("pages"):
            self.validate_global_author()

        if structure.get("pages"):
            self.validate_page_template(self.default_template)
            pages = self.page_creation(structure["pages"])
            self.log.info("* Created {} page(s)".format(len(pages)))

        return
