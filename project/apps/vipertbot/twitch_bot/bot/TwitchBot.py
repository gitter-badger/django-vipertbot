import sys, string, Queue, threading
from . import query, command
from .tools.termcolor import cprint
from .irc_twitch import IRC
from .read import (
    get_chan,
    get_msg
)

irc = IRC()

que = Queue.Queue()
signal_shutdown = False

def run():
    global signal_shutdown
    cprint('Starting ViperTbot ...', 'green')

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

                if get_msg(line).startswith("!"):
                    cmd_response = command.process_trigger(line)
                    if cmd_response:
                        irc.sendMessage(get_chan(line), cmd_response)
                    break

    except KeyboardInterrupt:
        cprint("\r\nShutting down ViperTbot ..", 'red')
        signal_shutdown = True
        sys.exit(0)

def queueWorker(q):
    global signal_shutdown

    try:
        while not signal_shutdown:
            try:
                job = query.get_next_job()

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

                    if query.remove_job(id):
                        cprint('Process Finished Successfully!', 'green')
                        q.task_done()
                    else:
                        cprint('Error: Process Job Failed!', 'red')
    except KeyboardInterrupt:
        sys.exit(0)