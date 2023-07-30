"""
TODO:

- [x] Finish symlink_sources()
- [ ] Install test structure to test hook_toolbox
- [ ] Add cookiecutter option to initialize created project as a Git repository with
      initial commit, will need a private cookiecutter var for the "git add" command
      value
- [ ] Docs

"""
import json
import os
import shutil
from pathlib import Path


class PostGenerationHookManager:
    """
    Post generation hook manager contains all the methods to use from hook script to
    perform operations on a post generated project.

    Arguments:
        basepath (pathlib.Path): A path which every relative paths are prefixed
            with. This would commonly be the generated project path.
    """
    def __init__(self, basepath):
        self.basepath = basepath.resolve()

    def symlink_sources(self, items):
        """
        Process given symlink item to achieve.

        All created symlinks will be relative to ensure portability.

        Arguments:
            items (list): A list of tuple with two items, the source path to
                symlink and the destination path of the symlink. All path have to be
                relative from the root of project template structure. If destination
                already exists it will be removed to be replaced with the symlink.

        Returns:
            list: A list of tuple, each tuple is for created symlink where first item
            is the created symlink and second item is the symlink target.
        """

        created = []

        for source, destination in items:
            # Ensure we have clear absolute paths else assume it is relative to
            # basepath and enforce it
            if not Path(source).is_absolute():
                source_path = self.basepath / source
            else:
                source_path = source

            if not Path(destination).is_absolute():
                destination_path = self.basepath / destination
            else:
                destination_path = destination

            # Source and destination can not resolve to the same path
            if source_path.resolve() == destination_path.resolve():
                raise ValueError((
                    "Source and destination can not resolve to the same path: "
                    "{}".format(source_path)
                ))

            # Check source path does exist
            if not source_path.exists():
                raise ValueError(
                    "Given source path does not exists: {}".format(source_path)
                )

            # Ensure destination tree already exists
            if not destination_path.parent.exists():
                raise ValueError((
                    "Given destination path belong to a parent directory that "
                    "does not exists: {}".format(destination_path)
                ))

            # Check if destination exists and remove it
            if destination_path.exists():
                # We manage removing either it is a file (or a link) or a directory
                if destination_path.is_dir():
                    shutil.rmtree(destination_path)
                else:
                    destination_path.unlink()

            # We use lower level 'os.path' module instead of 'Path.relative_to()'
            # since the latter only create absolute symlink.
            relative_target = os.path.relpath(source_path, destination_path.parent)
            os.symlink(relative_target, destination_path)

            # Store representation
            created.append((
                str(destination_path.relative_to(self.basepath)), relative_target
            ))

        return created


if __name__ == "__main__":
    print()
    print("🍻 Post generation hook")

    # Capture cookiecutter context and deserialize it using Json since naturally this
    # is an OrderedDict we can't evaluate as a Python object
    COOKIE_CONTEXT = json.loads("""{{ cookiecutter|tojson }}""")

    manager = PostGenerationHookManager(Path(".").resolve())

    manager.symlink_sources(COOKIE_CONTEXT["_apply_symlink_to"])
