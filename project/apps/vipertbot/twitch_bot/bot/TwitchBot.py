import sys, string, datetime, Queue, threading
from django.utils.timezone import utc
from tools.termcolor import cprint
from IRC import ircClass
import model

irc = ircClass()

que = Queue.Queue()
signal_shutdown = False

#todo: Extract more methods, create new Read Module

def run():
    global signal_shutdown

    queWorkerThread = threading.Thread(target=queueWorker, args=(que,))
    queWorkerThread.daemon = True

    queProcessWorkerThread = threading.Thread(target=queueProcessWorker, args=(que,irc))
    queProcessWorkerThread.daemon = True

    try:
        irc.connect()

        while True:
            irc_buffer = irc.readBuffer()

            for line in irc_buffer:
                cprint(line, 'blue')
                message = getMessage(line)

                if ":End of /NAMES list" in line:
                    cprint('JOINED ...', 'yellow')
                    irc.Loading = False
                    break

                if ":twitch.tv/membership" in line:
                    cprint("Connection Complete!", 'green')
                    queWorkerThread.start()
                    queProcessWorkerThread.start()
                    break

                if "PING" in line:
                    irc.sendPong(line)
                    break

                if message.startswith("!"):
                    owner = getOwner(line)
                    user = getUser(line)
                    processUserCommand(owner, user, message, line)
                    break

    except KeyboardInterrupt:
        cprint("\r\nShutting down ViperTbot ..", 'red')
        signal_shutdown = True
        sys.exit(0)

def processUserCommand(owner, user, message, line):
    uid = model.get_uid_by_username(owner)
    channel = owner
    commandID = 0
    commandText = ''
    commandActive = 0
    commandCooldown = 0
    commandRoles = None

    if uid:
        command = getCommand(message)
        user_commands = model.get_user_commands(uid)

        for item in user_commands:
            if command == item.name:
                commandID = item.id
                commandText = item.text
                commandCooldown = item.cooldown_min
                commandRoles = item.roles
                commandActive = item.active
                break

        cooldown = model.get_cooldown(uid, command)


        if checkCooldown(cooldown, commandCooldown):
            if not commandText == '':
                isAllowed = False

                for item in commandRoles.all():
                    if doesUserHavePermission(line, uid, item.name):
                        isAllowed = True
                        break

                if commandActive and isAllowed:
                    for var in getVars(line):
                        if var in commandText:
                            commandText = commandText.replace(var, getVars(line)[var])
                            break

                    cprint("-- CMD Recieved -- Requested By: "+user+": On #"+channel, 'cyan')

                    irc.sendMessage(channel, commandText)

                    if not cooldown == 0:
                        model.remove_cooldown(command, uid)

                    start_time = datetime.datetime.utcnow().replace(tzinfo=utc)
                    model.add_cooldown(uid, command, start_time)
        else:
            cprint('Cooldown: ' + str(cooldown), 'red')

    return True

def checkCooldown(start_time, command_cooldown):
    if start_time == 0:
        return True

    end = datetime.datetime.utcnow().replace(tzinfo=utc)
    duration = end - start_time
    days, seconds = duration.days, duration.seconds
    minutes = (seconds % 3600) // 60

    if minutes >= command_cooldown:
        return True

    return False

def getOwner(line):
    owner = line.split(':')[1].split('#')[1].strip(' ')
    # cprint('Owner: ' + repr(owner), 'red')
    return owner

def getUser(line):
    user = line.split(':')[1].split('!')[0].strip(' ')
    # cprint('User: ' + repr(user), 'red')
    return user

def getMessage(line):
    if 'PRIVMSG #' in line:
        message = line.split(':')[2]
        # cprint('Message: ' + repr(message), 'red')
        return message

    return str('')

def getChannel(line):
    channel = line.split(':')[1].split(' ')[2]
    # cprint('Channel: ' + repr(channel), 'red')
    return channel

def getCommand(line):
    command = line.split(' ')[0]
    # cprint('Command: ' + repr(command), 'red')
    return command.strip('\r')

def userIsModerator(line):
    v = line.split(';')[5].split('=')[1]

    if v is 1:
        return True

    return False

def userIsSubscriber(line):
    v = line.split(';')[7].split('=')[1]

    if v is 1:
        return True

    return False

def userIsTurbo(line):
    v = line.split(';')[8].split('=')[1]

    if v is 1:
        return True

    return False

def getOptions(line):
    arr = line.split(' ')[1:]
    return arr

def doesUserHavePermission(line, uid, role_name):

    if getUser(line) == getOwner(line):
        return True

    if role_name == 'Moderators':
        if userIsModerator(line): return True

    if role_name == 'Normal Users':
        return True

    if role_name == 'Regulars':
        data = model.get_regulars(uid)
        for item in data:
            if getUser(line) in item.name:
                return True

    if role_name == 'Subscribers':
        if userIsSubscriber(line): return True

    return False

def getVars(line):
    return {
        '{{username}}': getUser(line),
        '{{owner}}': getOwner(line),
        '{{channel}}': getChannel(line)
    }

def queueWorker(q):
    global signal_shutdown

    try:
        while not signal_shutdown:
            try:
                job = model.get_next_job()

                if job:
                    cprint("Added Job to Queue: " + job.name, 'magenta')
                    q.put(str(job.id)+'::'+job.name+'::'+job.user.username)
            except IndexError:
                continue

            q.join()

    except KeyboardInterrupt:
        sys.exit(0)

def queueProcessWorker(q, irc):
    global signal_shutdown

    try:
        while not signal_shutdown:
                job = q.get()

                if job:
                    arr = string.split(job, '::')
                    id = arr[0]
                    cmd = arr[1]
                    chan = arr[2]

                    if cmd == 'join':
                        irc.joinChannel(chan)
                    if cmd == 'part':
                        irc.partChannel(chan)
                    if cmd == 'rejoin':
                        irc.rejoinChannel(chan)

                    if model.remove_job(id):
                        cprint('Process Finished Successfully!', 'green')
                        q.task_done()
                    else:
                        cprint('Error: Process Job Failed!', 'red')
    except KeyboardInterrupt:
        sys.exit(0)