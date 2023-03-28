import json
from pathlib import Path

from docutils import nodes
from docutils.parsers.rst import Directive


SOURCE = Path(__file__).parents[2] / Path("cookiecutter.json")


class BireliStack(Directive):
    """
    A directive to extend Sphinx builder.

    It will retrieve every available version variables from ``../../cookiecutter.json``
    file.

    Variable from JSON file is assumed as a version variable if variable name:

    * Does not starts with ``__``;
    * Does starts with ``_``;
    * Does ends with ``_version``;

    All these criteria must be true to succeed assumption.

    Usage in RestructuredText document is: ::

        Some text

        .. bireli-stack::

        Blah blah

    It will render versions in a bullet list where the variable name will be
    capitalized, modified to replace ``_`` with ``-``, leading ``_`` removed and ending
    ``_version`` removed.

    """
    __cookiecontext_cache = None

    def _get_cookiecutter_context(self):
        """
        Get or use cached loaded cookiecutter context
        """
        if not self.__cookiecontext_cache:
            self.__cookiecontext_cache = json.loads(SOURCE.read_text())

        return self.__cookiecontext_cache

    def _format_stack_title(self, value):
        return value.replace("_", "-").capitalize()

    def _get_stack_content(self):
        """
        JSON source parser to retrieve elligible versions to collect and format.

        Returns:
            list: List of tuples for retrieved and formatted versions.
        """
        content = []

        cookie_options = self._get_cookiecutter_context()

        for name, value in cookie_options.items():
            if (
                not name.startswith("__") and
                name.startswith("_") and
                name.endswith("_version")
            ):
                label = self._format_stack_title(name[1:-len("_version")])
                content.append((label, value))

        return content

    def run(self):
        # Get versions
        versions = self._get_stack_content()

        # Open new bullet list node
        version_list = nodes.bullet_list()

        # Add item to bullet list
        for label, value in versions:
            item = nodes.list_item()
            paragraph = nodes.paragraph()
            paragraph.append(nodes.strong(text="{}: ".format(label)))
            paragraph.append(nodes.literal('', value))
            item.append(paragraph)
            version_list += item

        return [version_list]


class BireliBackendStack(BireliStack):
    def _get_stack_content(self):
        """
        Filter out all stack item that are not listed from context variable
        ``_backend_stack``.

        Returns:
            list: List of tuples for retrieved and formatted versions.
        """
        content = super()._get_stack_content()

        cookie_options = self._get_cookiecutter_context()

        backend_names = [
            self._format_stack_title(item)
            for item in cookie_options.get("_backend_stack", [])
         ]

        return [
            (label, value)
            for label, value in content
            if label in backend_names
        ]


class BireliFrontendStack(BireliStack):
    def _get_stack_content(self):
        """
        Filter out all stack item that are not listed from context variable
        ``_frontend_stack``.

        Returns:
            list: List of tuples for retrieved and formatted versions.
        """
        content = super()._get_stack_content()

        cookie_options = self._get_cookiecutter_context()

        backend_names = [
            self._format_stack_title(item)
            for item in cookie_options.get("_frontend_stack", [])
         ]

        return [
            (label, value)
            for label, value in content
            if label in backend_names
        ]


def bireli_stackitem_role(name, rawtext, text, lineno, inliner, options={},
                          content=[]):
    """
    Return item value from Bireli stack from cookiecutter context.
    """
    cookiecontext = json.loads(SOURCE.read_text())

    label = text
    value = cookiecontext.get("_{}_version".format(text), "Undefined")
    rendered = nodes.Text(value)

    ref = nodes.reference(rawtext, rendered, refuri=None)
    return [nodes.literal('', '', rendered)], []


def setup(app):
    app.add_role("bireli-stack-item", bireli_stackitem_role)
    app.add_directive("bireli-full-stack", BireliStack)
    app.add_directive("bireli-backend-stack", BireliBackendStack)
    app.add_directive("bireli-frontend-stack", BireliFrontendStack)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
