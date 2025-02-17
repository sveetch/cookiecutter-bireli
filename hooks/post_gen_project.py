import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

from rich import print as rprint


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

    def execute_commandline(self, *args):
        """
        Execute given commandline and returns its output once finished.

        Command will be executed in current working directory as defined in
        ``PostGenerationHookManager.basepath``.

        Arguments:
            *args: Arguments (strings) as expected from ``subprocess.Popen`` so the
                first item is always the command name then its command arguments.

        Raise:
            SystemExit: Raised if command did not finished with a success signal.

        Returns:
            string: Captured output from command
        """
        popen = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=self.basepath
        )

        # Wait for process to terminate
        out, err = popen.communicate()

        # If command finish with a non success signal, display informations and errors
        # then raise exception so cookiecutter will cancel project creation
        if popen.returncode != 0:
            print()
            print(args)
            print()
            print("Exit {}".format(popen.returncode))
            print()
            print(err.decode())
            sys.exit(popen.returncode)

        return out

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
        print()
        rprint("[bold blue]Applying symbolic links[/]")
        rprint("[bold blue]│[/]")

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

            rprint("[bold blue]├──[/] Pointed '{source}' to '{destination}'".format(
                source=relative_target,
                destination=str(destination_path.relative_to(self.basepath)),
            ))

            # Store representation
            created.append((
                str(destination_path.relative_to(self.basepath)), relative_target
            ))

        rprint("[bold blue]└──[/] :white_check_mark: Finished")

        return created

    def repository_init(self, sources):
        """
        Initialize repository and make initial commit with project files.

        Arguments:
            sources (list): List of paths to add to initial commit.
        """
        print()
        rprint("[bold blue]GIT repository post task[/]")
        rprint("[bold blue]│[/]")

        rprint("[bold blue]├──[/] Initializing GIT repository")
        self.execute_commandline("git", "init", ".")

        rprint("[bold blue]├──[/] Adding files to repository")
        self.execute_commandline("git", "add", *sources)

        rprint("[bold blue]├──[/] Adding initial commit")
        self.execute_commandline("git", "commit", "-m", "Initial commit")

        rprint("[bold blue]└──[/] :white_check_mark: Finished")

    def cleaning_files(self, title, items):
        """
        Clean given directories and files.

        If a given path does not exists in project structure a warning is printed but
        won't block process. Developer should maintain properly given path list and
        avoid to forget unexisting files.

        .. Note::
            Given path must be relative to currently building project directory,
            meaning inside ``{{ cookiecutter.project_name }}``.

        Arguments:
            title (string): A title to announce task.
            items (list): List of path string for all files and directories to remove.
        """
        print()
        rprint("[bold blue]{title}[/]".format(title=title))
        rprint("[bold blue]│[/]")

        for item in items:
            path = self.basepath / Path(item)

            if path.exists():
                if path.is_dir():
                    shutil.rmtree(path)
                else:
                    path.unlink()
            else:
                rprint("[bold blue]├──[/] [yellow]Path does not exist: {}[/]".format(
                    path,
                ))

        rprint("[bold blue]└──[/] :white_check_mark: Finished")


if __name__ == "__main__":
    # Capture cookiecutter context and deserialize it using Json since naturally this
    # is an OrderedDict we can't evaluate as a Python object
    context = json.loads("""{{ cookiecutter|tojson }}""")

    # Note that cookiecutter set current working directory as the temporary created
    # project root, so we just use '.' (resolved to absolute path for sanity)
    manager = PostGenerationHookManager(Path(".").resolve())

    # Apply possible symbolic links
    manager.symlink_sources(context["_apply_symlink_to"])

    # Remove files related to API, the composer app is still keeped
    if not context["api_enabled"]:
        manager.cleaning_files(
            "Removing API files",
            [
                "django-apps/project_api/",
            ]
        )

    # Initialize GIT repository, usually the last task to use
    if context["init_git_repository"]:
        manager.repository_init([".gitignore", ".flake8", "*"])
