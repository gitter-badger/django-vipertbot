def get_owner(line):
    owner = line.split(':')[1].split('#')[1].strip(' ')
    # cprint('Owner: ' + repr(owner), 'red')
    return owner

def get_user(line):
    user = line.split(':')[1].split('!')[0].strip(' ')
    # cprint('User: ' + repr(user), 'red')
    return user

def get_msg(line):
    if 'PRIVMSG #' in line:
        message = line.split(':')[2]
        # cprint('Message: ' + repr(message), 'red')
        return message

    return str('')

def get_chan(line):
    channel = line.split(':')[1].split(' ')[2]
    # cprint('Channel: ' + repr(channel), 'red')
    return channel

def get_cmd(line):
    command = line.split(' ')[0]
    # cprint('Command: ' + repr(command), 'red')
    return command.strip('\r')

def get_options(line):
    arr = line.split(' ')[1:]
    return arr