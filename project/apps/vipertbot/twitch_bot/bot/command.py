import datetime
from django.utils.timezone import utc
from . import query, cooldown, chatter
from .tools.termcolor import cprint
from .read import (
    get_user,
    get_chan,
    get_cmd,
    get_msg,
    get_owner
)
def public_variables(line):
    return {
        '{{username}}': get_user(line),
        '{{owner}}': get_owner(line),
        '{{channel}}': get_chan(line)
    }

def process_trigger(line):
    message = get_msg(line)
    owner = get_owner(line)
    user = get_user(line)
    uid = query.get_uid_by_username(owner)
    channel = owner
    cmd_id = 0
    cmd_text = ''
    cmd_active = 0
    cmd_cooldown = 0
    cmd_roles = None

    try:
        if uid:
            command = get_cmd(message)
            user_commands = query.get_user_commands(uid)

            for item in user_commands:
                if command == item.name:
                    cmd_id = item.id
                    cmd_text = item.text
                    cmd_cooldown = item.cooldown_min
                    cmd_roles = item.roles
                    cmd_active = item.active
                    break

            _cooldown = query.get_cooldown(uid, command)

            if cooldown.check(_cooldown, cmd_cooldown):
                if not cmd_text == '':
                    isAllowed = False

                    for item in cmd_roles.all():
                        if chatter.has_role(line, uid, item.name):
                            isAllowed = True
                            break

                    if cmd_active and isAllowed:
                        for var in public_variables(line):
                            if var in cmd_text:
                                cmd_text = cmd_text.replace(var, public_variables(line)[var])
                                break

                        cprint("-- CMD Recieved -- Requested By: "+user+": On #"+channel, 'cyan')

                        if not cooldown == 0:
                            query.remove_cooldown(command, uid)

                        start_time = datetime.datetime.utcnow().replace(tzinfo=utc)
                        query.add_cooldown(uid, command, start_time)

                        return cmd_text
            else:
                cprint('Cooldown: ' + str(cooldown), 'red')
    except Exception, e:
        cprint(e.message, 'red')

    return False