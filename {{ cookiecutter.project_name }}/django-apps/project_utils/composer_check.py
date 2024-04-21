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
