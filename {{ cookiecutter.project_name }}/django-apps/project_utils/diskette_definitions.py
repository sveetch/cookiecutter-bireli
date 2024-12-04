import logging
import json
from pathlib import Path

from diskette.contrib.composer.collectors import DisketteDefinitionsCollector
from diskette.contrib.composer.processors import DisketteDefinitionsProcessor
from project_composer.logger import init_logger

from project_composer.compose import Composer


if __name__ == "__main__":
    # Only critical error logs are allowed to no pollute debug output
    init_logger("project-composer", logging.ERROR)

    _composer = Composer(
        Path("./pyproject.toml").resolve(),
        processors=[DisketteDefinitionsProcessor],
    )

    # Resolve dependency order
    _composer.resolve_collection(lazy=False)

    # Get all application Diskette classes
    _classes = _composer.call_processor("DisketteDefinitionsProcessor", "export")

    # Reverse the list since Python class order is from the last to the first
    _classes.reverse()

    # Add the base collector as the base inheritance
    _COMPOSED_CLASSES = _classes + [DisketteDefinitionsCollector]

    # Compose the final classe
    DisketteDefinitions = type("DisketteDefinitions", tuple(_COMPOSED_CLASSES), {})

    # Collect all definitions in the right order
    definitions = DisketteDefinitions()

    # Get the registry destination path
    destination = Path("./parts/diskette/diskette.json")
    if not destination.parent.exists():
        destination.parent.mkdir(parents=True)

    # And finally output all collected definitions
    destination.write_text(
        json.dumps(definitions.get_definitions(), indent=4)
    )
    print("Diskette definitions have been written to:", destination.resolve())
