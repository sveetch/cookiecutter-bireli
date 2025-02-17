import json
from pathlib import Path

from docutils import nodes
from docutils.parsers.rst import Directive, directives


BASE = Path(__file__).parents[2]
COMPOSE_REPOSITORY = BASE / Path(
    "{{ cookiecutter.project_name }}/composition_repository"
)


class ComposerAppRequirements(Directive):
    """
    A ReStructuredText directive to list requirements from a Composer application as
    defined in its ``requirements.txt``.

    Usage in a ReStructuredText document is: ::

        A first line

        .. composer-app-requirements:: appname1[,appname2]*
           :title: Optional title

        Another line

    """
    required_arguments = 1
    option_spec = {
        "title": directives.unchanged,
    }

    def _get_requirements(self, name):
        """
        Parse requirements file from given module name and return list of
        specifiers (every non empty or non comment lines).
        """
        module_path = COMPOSE_REPOSITORY / name
        requirements_file = module_path / "requirements.txt"

        if not module_path.exists() or not module_path.is_dir():
            raise self.error((
                "There is no application named '{}' in composer repository or it is "
                "not a directory."
            ).format(name))

        if not requirements_file.exists():
            raise self.error((
                "There is no requirements for application '{}' in composer repository "
                "or it is not a file."
            ).format(name))

        return [
            line.strip()
            for line in requirements_file.read_text().splitlines()
            if not line.strip().startswith("#")
        ]

    def _build_requirement_list(self, requirements):
        """
        Build RST nodes for a list of requirement items.
        """
        # Open new bullet list node
        container = nodes.bullet_list()

        # Add item to bullet list
        for value in requirements:
            item = nodes.list_item()
            item.append(nodes.paragraph(text=value))
            container += item

        return container

    def run(self):
        """
        Render content
        """
        elements = []
        names = self.arguments[0]

        # Get requirements lines
        requirements = []
        for item in names.split(","):
            if item:
                requirements.extend(self._get_requirements(item.strip()))
        requirement_list = self._build_requirement_list(requirements)

        if self.options.get("title"):
            title = nodes.paragraph()
            title.append(nodes.strong("", self.options["title"].strip()))
            elements.append(title)

        elements.append(requirement_list)
        return elements


def setup(app):
    app.add_directive("composer-app-requirements", ComposerAppRequirements)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
