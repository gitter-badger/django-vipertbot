import datetime
from django.utils.timezone import utc

def check(start_time, command_cooldown):
    if start_time == 0:
        return True

    end = datetime.datetime.utcnow().replace(tzinfo=utc)
    duration = end - start_time
    days, seconds = duration.days, duration.seconds
    minutes = (seconds % 3600) // 60

    if minutes >= command_cooldown:
        return True

    return False