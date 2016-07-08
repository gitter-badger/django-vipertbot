import socket, string, time
from Settings import HOST, PORT, PASS, IDENT, CHANNELS
from tools.termcolor import cprint
from Database import database

class ircClass:

    bufferSize = 2048
    Loading = False

    def __init__(self):
        self.socket = socket.socket()
        self.db = database()

    def connect(self):
        self.socket.connect((HOST, PORT))
        self.socket.send("PASS " + PASS + "\r\n")
        self.socket.send("NICK " + IDENT + "\r\n")
        self.socket.send("CAP REQ :twitch.tv/membership\r\n")
        self.socket.send("CAP REQ :twitch.tv/commands\r\n")
        self.socket.send("CAP REQ :twitch.tv/tags\r\n")
        return True

    def sendPong(self, line):
        pong = line.replace("PING", "PONG")
        cprint(pong, 'green')
        self.sendToServer(pong + "\n")

    def sendToServer(self, msg):
        self.socket.send(msg)

    def readBuffer(self, buf=""):
        b = buf + self.socket.recv(self.bufferSize)
        stemp = string.split(b, "\n")
        b = stemp.pop()
        return stemp

    def sendMessage(self, channel, message):
        messageTemp = "PRIVMSG #" + channel + " :" + message
        self.socket.send(messageTemp + "\r\n")
        cprint("-- Sent Message -- " + str(channel) + " :message: " + str(message), 'green')
        return True

    def joinChannel(self, channel):
        self.Loading = True

        self.socket.send("JOIN #" + channel + "\r\n")

        while self.Loading:
            time.sleep(0)

        self.sendMessage(channel, "I\'m Here!")
        return True

    def partChannel(self, channel):
        self.sendMessage(channel, 'I\'m leaving ... Goodbye!')
        time.sleep(2)
        self.socket.send("PART #" + channel + "\r\n")
        return True

    def rejoinChannel(self, channel):
        self.sendMessage(channel, "BRB!")
        time.sleep(2)
        self.partChannel(channel)
        self.joinChannel(channel)
        return True
