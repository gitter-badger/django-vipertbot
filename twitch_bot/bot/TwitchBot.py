import sys, string, datetime, Queue, threading, dateutil.parser
from tools.termcolor import cprint
from Database import database
from IRC import ircClass

irc = ircClass()

que = Queue.Queue()
signal_shutdown = False
db = database()

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
    db = database()
    uid = db.getUserIdByUsername(owner)
    channel = owner
    commandID = 0
    commandText = ''
    commandActive = 0
    commandCooldown = 0

    if not uid == "":
        command = getCommand(message)
        user_commands = db.getUserCommands(uid)

        for item in user_commands:
            if command == item[1]:
                commandID = item[0]
                commandText = item[2]
                commandCooldown = item[3]
                commandActive = item[4]
                break
        cooldown = db.getCooldown(command, channel)


        if checkCooldown(cooldown, commandCooldown):
            if not commandText == '':
                permissions = db.getCommandPermissions(commandID)
                isAllowed = False

                for item in permissions:
                    if doesUserHavePermission(line, item[0]):
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
                        db.deleteCooldown(command, channel)

                    start_time = datetime.datetime.now()
                    db.insertCooldown(command, channel, start_time)
        else:
            cprint('Cooldown: ' + cooldown)

    return True

def checkCooldown(start_time, command_cooldown):
    if start_time == 0:
        return True

    end = datetime.datetime.now()
    diff = end - dateutil.parser.parse(start_time)
    minutes = diff.days * 86400 + diff.seconds / 60
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

def doesUserHavePermission(line, permission_id):

    if getUser(line) == getOwner(line):
        return True

    if permission_id is 1:
        if userIsModerator(line): return True

    if permission_id is 2:
        return True

    if permission_id is 3:
        if not db.getRegular(getUser(line)) == 0:
            return True

    if permission_id is 4:
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
    db = database()

    try:
        while not signal_shutdown:
            job = db.getJob()

            if job:
                cprint("Added Job to Queue: " + job, 'magenta')
                q.put(job)

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
                    cmd = arr[1]
                    chan = arr[2]

                    if cmd == 'join':
                        irc.joinChannel(chan)
                    if cmd == 'part':
                        irc.partChannel(chan)
                    if cmd == 'rejoin':
                        irc.rejoinChannel(chan)

                    if db.deleteJob(job):
                        cprint('Process Finished Successfully!', 'green')
                        q.task_done()
                    else:
                        cprint('Error: Process Job Failed!', 'red')
    except KeyboardInterrupt:
        sys.exit(0)