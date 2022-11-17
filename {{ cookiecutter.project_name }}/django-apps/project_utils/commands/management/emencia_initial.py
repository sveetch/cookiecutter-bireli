import argparse
import json

from django.conf import settings
from django.core.management.base import CommandError, BaseCommand

from cms.api import Page


class Command(BaseCommand):
    """
    Demo data loader.
    """
    help = (
        "Populate site with demo data. It will populate CMS pages from required JSON "
        "tree file. You MUST use Django command 'flush' before using this command. "
        "Pages are only created for the default language."
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.created_pages = {}

    def add_arguments(self, parser):
        parser.add_argument(
            "dump",
            metavar="FILEPATH",
            type=argparse.FileType("r", encoding="UTF-8"),
            help="Filepath to the JSON tree file to load."
        )

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS("=== Starting demo maker ===")
        )

        raise NotImplementedError("TODO")

        # Validate available demo page templates
        available_cms_templates = [item[0] for item in settings.CMS_TEMPLATES]
        for k, v in settings.DEMO_PAGE_TEMPLATES.items():
            if v not in available_cms_templates:
                raise CommandError((
                    "Page template '{}' must be enabled in 'settings.CMS_TEMPLATES'."
                ).format(v))

        if (
            "homepage" not in settings.DEMO_PAGE_TEMPLATES.keys() or
            "page" not in settings.DEMO_PAGE_TEMPLATES.keys()
        ):
            raise CommandError(
                "Page template 'homepage' and 'page' must be defined in "
                "'settings.DEMO_PAGE_TEMPLATES'."
            )

        # Validate database is empty
        existing = Page.objects.all()
        if existing.count():
            raise CommandError(
                "Demo maker will only work if there is not any existing CMS "
                "page. Did you forgot to use Django command 'flush' before ?"
            )

        self.stdout.write("* Opened JSON tree: {}".format(options["dump"].name))
        tree = json.load(options["dump"])

        self.create_cms_pages(tree)
