#!/usr/bin/env python
"""
A simple parser to collect all task help description from a Makefile.

It is hardly base on a basic Makefile format and may not be usable for some other
formats.

Task name are not allowed to contains "--" since it is used as a separator between
task name and task help text.
"""

EXPECTED_TASK_HELP_LINE_START = "	@echo \"  "
EXPECTED_TASK_HELP_SEPARATOR = "--"
EXPECTED_TASK_HELP_LINE_END = "\""


def is_task_help_line(line):
    """
    Validate given line if it is a proper task help line or not.

    To be valid a line should starts exactly with string from
    ``EXPECTED_TASK_HELP_LINE_START`` and then contains string from
    ``EXPECTED_TASK_HELP_SEPARATOR``.

    Arguments:
        line (string): A string to validate as a task help line.

    Returns
        boolean: True if line match criteria, else False.
    """
    if (
        line and
        line.startswith(EXPECTED_TASK_HELP_LINE_START) and
        EXPECTED_TASK_HELP_SEPARATOR in line and
        line.endswith(EXPECTED_TASK_HELP_LINE_END)
    ):
        return True

    return False


def parse_task_help(line, titelize=True):
    """
    Parse a task help line to return proper data to collect.

    Arguments:
        line (string): A string to parse.

    Keyword Arguments:
        titelize (boolean): If True, the first letter of help text is uppercased.
            Default to True.

    Returns:
        tuple: A tuple where first item is the task name and second one is the task
        help text.
    """
    # Remove expected starting and ending
    content = line[len(EXPECTED_TASK_HELP_LINE_START):]
    content = content[:-len(EXPECTED_TASK_HELP_LINE_END)]

    content = content.split(EXPECTED_TASK_HELP_SEPARATOR)
    name = content[0].strip()
    description = "".join(content[1:]).strip()

    if titelize:
        description = description[0:1].upper() + description[1:]

    return name, description


def output_rst_definitions(tasks):
    """
    Output a RestructuredText definition list element from given items.

    Arguments:
        tasks (dictionnary): Items to format as RST definition list.

    Returns:
        string: A RST definition list.
    """
    output = ""

    for task_name, task_text in tasks.items():
        output += task_name + "\n"
        output += "    " + task_text + "\n"

    return output


def get_task_helps(content):
    """
    Iterate on Makefile content lines to collect task help lines

    Arguments:
        content (string): A Makefile file content to parse.

    Returns
        dict: Found task help items.
    """
    collected = {}
    # State flag for when in the help section
    in_help_section = False

    for line in content.splitlines():
        # Trigger help section state
        if line.startswith("help:"):
            in_help_section = True
            continue
        # Once in help section and encounter en empty line, assume help section is
        # finished and we stop to parse
        elif not line:
            if in_help_section:
                in_help_section = False
                break

        # During help section, collect task helps
        if in_help_section and is_task_help_line(line):
            name, description = parse_task_help(line)
            collected[name] = description

    return collected


if __name__ == "__main__":
    import argparse
    import sys
    import json

    from pathlib import Path

    parser = argparse.ArgumentParser(
        description=(
            "Parse a Makefile to collect task help texts."
        ),
    )
    parser.add_argument(
        "sourcepath",
        default=None,
        help=(
            "Give a path to a Makefile file."
        )
    )
    parser.add_argument(
        "--format",
        choices=["json", "rst"],
        default="json",
        help=(
            "Output format, either 'json' or 'rst'. Default to 'rst'."
        )
    )
    parser.add_argument(
        "--destination",
        default=None,
        help=(
            "Give a file path where to write output."
        )
    )
    args = parser.parse_args()

    SOURCE_PATH = Path(args.sourcepath)

    if not SOURCE_PATH.exists():
        print("Given Makefile path does not exists: {}".format(SOURCE_PATH))
        sys.exit(1)

    # Open file and collect task helps
    tasks = get_task_helps(SOURCE_PATH.read_text())

    # Serialize to format
    if args.format == "json":
        output = json.dumps(tasks, indent=4)
    else:
        output = output_rst_definitions(tasks)

    if not args.destination:
        print(output)
    else:
        DESTINATION_PATH = Path(args.destination)
        DESTINATION_PATH.write_text(output)
        print("Output has been written to: {}".format(DESTINATION_PATH))
