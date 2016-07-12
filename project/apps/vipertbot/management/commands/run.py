from django.core.management.base import NoArgsCommand, CommandError
from project.apps.vipertbot.twitch_bot import TwitchBot

class Command(NoArgsCommand):
    help = 'Runs the server with vipertbot'
    can_import_settings = True

    def handle_noargs(self, **options):
        self.stdout.write(self.style.SUCCESS('Successful'))
        TwitchBot.run()