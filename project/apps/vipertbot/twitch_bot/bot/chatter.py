from . import query
from .read import (
    get_user,
    get_owner
)

def is_mod(line):
    v = line.split(';')[5].split('=')[1]

    if v is 1:
        return True

    return False

def is_sub(line):
    v = line.split(';')[7].split('=')[1]

    if v is 1:
        return True

    return False

def is_turbo(line):
    v = line.split(';')[8].split('=')[1]

    if v is 1:
        return True

    return False

def has_role(line, uid, role_name):

    if get_user(line) == get_owner(line):
        return True

    if role_name == 'Moderators':
        if is_mod(line): return True

    if role_name == 'Normal Users':
        return True

    if role_name == 'Regulars':
        data = query.get_regulars(uid)
        for item in data:
            if get_user(line) in item.name:
                return True

    if role_name == 'Subscribers':
        if is_sub(line): return True

    return False