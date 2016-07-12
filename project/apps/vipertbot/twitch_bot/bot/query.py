from tools.termcolor import cprint
from django.contrib.auth import get_user_model
from project.apps.vipertbot.models import Command
from project.apps.vipertbot.models import Job
from project.apps.vipertbot.models import Regular
from project.apps.vipertbot.models import Role
from project.apps.vipertbot.models import Cooldown

User = get_user_model()

def get_uid_by_username(owner):
    try:
        model = User.objects.get(username=owner)
        return model.id
    except (User.DoesNotExist,
            User.MultipleObjectsReturned):
        return False

def get_user_commands(uid):
    model = Command.objects.filter(user__id=uid)
    return model

def get_regulars(uid):
    model = Regular.objects.filter(user__id=uid)
    return model

def get_next_job():
    return Job.objects.all()[:1][0]

def remove_job(job_id):
    cprint('Job ID' + job_id, 'red')
    model = Job.objects.get(id=job_id)
    model.delete()
    return True

def get_cooldown(uid, command):
    try:
        model = Cooldown.objects.get(user__id=uid, name=command)
        return model.start_time
    except (Cooldown.DoesNotExist,
            Cooldown.MultipleObjectsReturned):
        return 0

def add_cooldown(uid, command, start_time):
    model = Cooldown(
        user=User.objects.get(id=uid),
        name=command,
        start_time=start_time
    )
    model.save()
    return True

def remove_cooldown(command, uid):
    model = Cooldown.objects.get(name=command, user__id=uid)
    model.delete()
    return True

