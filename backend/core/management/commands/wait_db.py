import time

from django.core.management import BaseCommand
from django.db import connection, OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Waiting for the database..."))
        con_db = False

        while not con_db:
            try:
                connection.ensure_connection()
                con_db = True
            except OperationalError:
                self.stdout.write(self.style.ERROR("Database unavailable"))
                time.sleep(3)
        self.stdout.write(self.style.SUCCESS("Database connected"))
