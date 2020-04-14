from django.core.management.base import BaseCommand

from indonesia import load as load_indo
from world import load as load_world


class Command(BaseCommand):
    help = 'Import data spasial kedalam basis data'

    def handle(self, *args, **options):
        load_indo.run()
        load_world.run()

