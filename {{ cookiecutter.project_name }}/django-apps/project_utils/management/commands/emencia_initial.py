from django.core.management.base import CommandError, BaseCommand

from cms.api import Page

from ...initial_loader import InitialDataLoader


class Command(BaseCommand):
    """
    Initial data loader.
    """
    help = (
        "Populate site with initial data loaded from a JSON file."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "dump",
            metavar="FILEPATH",
            help="Filepath to the JSON file with structure to load."
        )

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS("=== Loading initial data ===")
        )

        # Validate database is empty
        existing = Page.objects.all()
        if existing.count():
            raise CommandError(
                "Initial data can only be loaded when the database is empty from any "
                "objects. You should (carefuly) use Django command 'flush' before."
            )

        self.stdout.write("* Opened JSON source: {}".format(options["dump"]))

        maker = InitialDataLoader()
        maker.load(options["dump"])
