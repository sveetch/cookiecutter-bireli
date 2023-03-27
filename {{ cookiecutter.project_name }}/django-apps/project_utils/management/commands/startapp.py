from pathlib import Path
import shutil
import tempfile

from django.conf import settings
from django.core.management.base import CommandError, BaseCommand

import tomli

SUCCESS_MESSAGE = """
🎉 Created a new application: {title}

- Application composer parts have been created to: {dest_module}
- Application code directory has been created to: {dest_compose}

1. Now you need to edit Project configuration: {conf}

   Open it and edit the composer 'collection' to add a new line for your application:

     [tool.project_composer]
     collection = [
         ...
         \"{module}\",
     ]

2. Go into your application code and start development
3. You may not need everything that was generated, please clean what you don't need
4. Since generated model is a sample, no migrations have been created for it yet. Once
   you are done with your models, you can start their initial migration:

     make migrations

♥ Happy coding ♥

"""


try:
    from cookiecutter.main import cookiecutter
    from slugify import slugify
except ImportError:
    class Command(BaseCommand):
        def handle(self, *args, **options):
            self.stdout.write(
                self.style.ERROR((
                    "This command requires 'cookiecutter' to be installed to work."
                ))
            )
            raise CommandError("Aborted.")
else:

    class Command(BaseCommand):
        """
        Use a cookiecutter template progammatically to create and deploy a new
        application into project.
        """
        help = (
            "Create everything for a new application properly structured for a Bireli "
            "project."
        )

        def add_arguments(self, parser):
            parser.add_argument(
                "--title",
                metavar="TITLE",
                help=(
                    "Application full title. It will be used to build application "
                    "name, Python class name and Python module name. Think about to "
                    "quote it if there is some spaces or special characters."
                )
            )

        def get_apps_destination(self, module):
            return self.apps_dir / module

        def get_composer_destination(self, module):
            return self.composer_repo / module

        def get_title_value(self, options):
            """
            Get title value from argument or from interactive input if argument is
            empty.
            """
            if not options["title"]:
                value = input("Input the full title: ")
                self.stdout.write("")
            else:
                value = options["title"]

            return value.strip()

        def validate_names(self, title, name, module, klass):
            """
            Validate than built names won't overwrite anything from existing
            applications.
            """
            errors = []

            if module in settings.INSTALLED_APPS:
                msg = "Module name already exists in 'settings.INSTALLED_APPS'"
                errors.append(msg)

            if module in self.project_conf["tool"]["project_composer"]["collection"]:
                msg = "Module name already exists in composer collection from: {}"
                errors.append(msg.format(self.project_conf_path))

            if self.get_composer_destination(module).exists():
                msg = "Module name already exists in: {}"
                errors.append(msg.format(self.composer_repo))

            if self.get_apps_destination(module).exists():
                msg = "Module name already exists in: {}"
                errors.append(msg.format(self.apps_dir))

            if errors:
                self.stdout.write()

                for msg in errors:
                    self.stdout.write(
                        self.style.ERROR("- " + msg)
                    )

                self.stdout.write()
                raise CommandError("Aborted due to errors.")

            return True

        def deploy_app(self, title, name, module, klass):
            composer_conf = self.project_conf["tool"].get("bireli", {})
            template_repository = composer_conf.get("app_template")

            # Get the template repository with possible tag (after the #)
            if not template_repository:
                msg = (
                    "No template repository could be found from "
                    "'tool.bireli.app_template' in: {}"
                )
                raise CommandError(msg.format(self.project_conf_path))
            else:
                try:
                    template_repository, repo_tag = template_repository.split("#")
                except ValueError:
                    repo_tag = None

            self.stdout.write("- Using repository: {}".format(template_repository))
            self.stdout.write("- Using tag: {}".format(repo_tag))

            # Build tmp directory to receive generated new app
            tmpdir = Path(
                tempfile.mkdtemp(prefix="bireli_newapp_{}_".format(module))
            )

            # Build paths
            destination_dirname = name + "_newapp"
            apps_source = tmpdir / destination_dirname / "django-apps" / module
            composer_source = (
                tmpdir / destination_dirname / "composition_repository" / module
            )
            apps_destination = self.get_apps_destination(module)
            composer_destination = self.get_composer_destination(module)

            # Generated stuff from template
            cookiecutter(
                template_repository,
                no_input=True,
                extra_context={
                    "application_title": title,
                    "application_name": name,
                    "application_module": module,
                    "application_class": klass,
                },
                output_dir=tmpdir,
                checkout=repo_tag,
            )

            # Move generated dir to apps
            shutil.copytree(apps_source, apps_destination)
            # Move generated dir to compose repo
            shutil.copytree(composer_source, composer_destination)
            # Finally remove the temporary generated stuff
            shutil.rmtree(tmpdir)

        def handle(self, *args, **options):
            self.project_conf_path = settings.BASE_DIR / "pyproject.toml"
            self.project_conf = tomli.loads(self.project_conf_path.read_text())

            self.composer_repo = settings.BASE_DIR / "composition_repository"
            self.apps_dir = settings.BASE_DIR / "django-apps"

            # Exactly use the same "name building" than the cookie template
            application_title = self.get_title_value(options)
            application_name = slugify(application_title.lower())
            application_module = application_name.replace('-', '_')
            application_class = application_name.replace('-', ' ').title()
            application_class = application_class.replace(' ', '')

            self.stdout.write("- Application title: {}".format(application_title))
            self.stdout.write("- Built name: {}".format(application_name))
            self.stdout.write("- Built module: {}".format(application_module))
            self.stdout.write("- Built classes prefix: {}".format(
                application_class
            ))
            self.stdout.write("")

            self.validate_names(
                application_title,
                application_name,
                application_module,
                application_class,
            )

            self.deploy_app(
                application_title,
                application_name,
                application_module,
                application_class,
            )

            self.stdout.write(SUCCESS_MESSAGE.format(
                conf=self.project_conf_path,
                title=application_title,
                name=application_name,
                module=application_module,
                klass=application_class,
                dest_module=self.get_apps_destination(application_module),
                dest_compose=self.get_composer_destination(application_module),
            ))
