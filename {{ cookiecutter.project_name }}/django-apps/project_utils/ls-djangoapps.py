"""
This script returns a list of elligible Python module directories.

Basically it is to reproduce behavior of ``ls``: ::

    ls -I '__pycache__' -I '*.py' django-apps

It is mostly used to feed application list to check with Django migration (to avoid
checking external application libraries).

This is because some 'ls' arguments are not compatible on all systems like BSD or
MacOS.

This is pure Python without any library usage.
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
