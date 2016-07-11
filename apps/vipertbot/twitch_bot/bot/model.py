from django.contrib.auth import get_user_model
from apps.vipertbot.models import Command
from apps.vipertbot.models import Job
from apps.vipertbot.models import Regular
from apps.vipertbot.models import Role
from apps.vipertbot.models import Cooldown

User = get_user_model()

def get_uid_by_username(owner):
    try:
        model = User.objects.get(username=owner)
        return model.id
    except (User.DoesNotExist,
            User.MultipleObjectsReturned):
        return False

def get_user_commands(uid):
    return Command.objects.filter(user__id=uid)

def get_cooldown(owner, command):
    try:
        model = Cooldown.objects.get(username=owner)
        return model.start_time
    except (Cooldown.DoesNotExist,
            Cooldown.MultipleObjectsReturned):
        return 0