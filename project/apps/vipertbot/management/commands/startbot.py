from django.core.management.base import BaseCommand, CommandError
from project.apps.vipertbot import twitch_bot

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
            self.stdout.write(self.style.SUCCESS('Successfully'))