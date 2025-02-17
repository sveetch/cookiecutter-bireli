"""
A script to perform a health checking about Project composer configuration.

It will try to collect every processor from every enabled application, search for
possible misconfiguration and output some debug informations.

This should only involves Project composer since commonly processors should not include
any import of Django or related Django applications.

There is no available argument to launch this script, it only stands on configuration
from ``pyproject.toml``.
"""
import logging

from diskette.contrib.composer.processors import DisketteDefinitionsProcessor

from project_composer.logger import init_logger
from project_composer.helpers import check_project
from project_composer.processors import TextContentProcessor
from project_composer.contrib.django.processors import (
    DjangoSettingsProcessor, DjangoUrlsProcessor
)


if __name__ == "__main__":
    # Only critical error logs are allowed to no pollute debug output
    init_logger("project-composer", logging.ERROR)
    # Check and outputs debug informations from project
    check_project(
        "./pyproject.toml",
        processors=[
            DjangoSettingsProcessor,
            DjangoUrlsProcessor,
            TextContentProcessor,
            DisketteDefinitionsProcessor,
        ],
        lazy=False
    )
