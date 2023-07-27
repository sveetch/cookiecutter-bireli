"""
This script just return a list of elligible directories as Django application modules.

Basically it is to reproduce behavior of: ::

    ls -I '__pycache__' -I '*.py' django-apps

This is because some 'ls' arguments are not compatible on all systems like BSD or
MacOS.
"""


def is_elligible_appdir(path):
    """
    Determine if given path is elligible as a Django application directory to consider.

    This is just about path to be a directory with a file ``__init__.py``. We don't
    enforce things like a file ``models.py``, etc..

    Arguments:
        path (pathlib.Path): A path to check.

    Returns:
        boolean: True if path is elligible else False.
    """
    if path.is_dir() and (path / "__init__.py").exists():
        return True

    return False


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description=(
            "Listing of elligible app directory names from a path."
        ),
    )
    parser.add_argument(
        "path",
        default=None,
        help=(
            "An existing path where to search for elligible directories."
        )
    )

    args = parser.parse_args()

    source = Path(args.path)

    if not source.exists():
        raise SystemExit("Given path is invalid")

    print(
        " ".join([
            str(v.name)
            for v in source.iterdir()
            if is_elligible_appdir(v)
        ])
    )
