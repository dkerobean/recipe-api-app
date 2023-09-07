"""
Django commands to wait for the database to be available
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """ Django commands to wait for the database to be available """

    def handle(self, *args, **options):
        """ Entry point for command """
        self.stdout.write("Waiting for database to be available...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write("Database is not available, waiting...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database is available'))
