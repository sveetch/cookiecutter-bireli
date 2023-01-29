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
    def _get_stack_content(self):
        """
        JSON source parser to retrieve elligible versions to collect and format.

        Returns:
            list: List of tuples for retrieved and formatted versions.
        """
        content = []

        cookie_options = json.loads(SOURCE.read_text())
        for name, value in cookie_options.items():
            if (
                not name.startswith("__") and
                name.startswith("_") and
                name.endswith("_version")
            ):
                label = name[1:-len("_version")].replace("_", "-").capitalize()
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


def setup(app):
    app.add_directive("bireli-stack", BireliStack)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
