import json
from pathlib import Path

import pytest

# Coming from "hooks/"
import post_gen_project


class FixturesSettingsTestMixin(object):
    """
    A mixin containing settings about project. This is almost about useful
    paths which may be used in tests.

    Attributes:
        root_path (pathlib.Path): Absolute path to the project repository root.
        project_dir (pathlib.Path): Django project directory name.
        tests_dir (pathlib.Path): Directory name which include tests.
        tests_path (pathlib.Path): Absolute path to the tests directory.
        fixtures_dir (pathlib.Path): Directory name which include tests datas.
        fixtures_path (pathlib.Path): Absolute path to the tests datas.
    """
    def __init__(self):
        self.root_path = Path(__file__).parent.parent.resolve()

        self.tests_dir = "tests"
        self.tests_path = self.root_path / self.tests_dir

        self.fixtures_dir = "data_fixtures"
        self.fixtures_path = self.tests_path / self.fixtures_dir

        self.cookiecutter_config = json.loads(
            (self.root_path / "cookiecutter.json").read_text()
        )

        self.cookiecutter_template = self.root_path / "{{ cookiecutter.project_name }}"

    def format(self, content):
        """
        Format given string to include some values related to this application.

        Arguments:
            content (str): Content string to format with possible values.

        Returns:
            str: Given string formatted with possible values.
        """
        return content.format(
            HOMEDIR=Path.home(),
            ROOT=str(self.root_path),
            TESTS=str(self.tests_path),
            FIXTURES=str(self.fixtures_path),
            VERSION=self.cookiecutter_config["_bireli_version"],
        )


@pytest.fixture(scope="function")
def temp_builds_dir(tmp_path):
    """
    Prepare a temporary build directory.

    NOTE: You should use directly the "tmp_path" fixture in your tests.
    """
    return tmp_path


@pytest.fixture(scope="module")
def settings():
    """
    Initialize and return settings for tests.

    Example:
        You may use it in tests like this: ::

            def test_foo(tests_settings):
                print(tests_settings.root_path)
                print(tests_settings.format("Root: {ROOT}"))
    """
    return FixturesSettingsTestMixin()


@pytest.fixture(scope="function")
def postgen_manager():
    """
    Return a function to initialize manager
    """
    return post_gen_project.PostGenerationHookManager
