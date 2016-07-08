#!/usr/bin/python
from tools.termcolor import cprint
from Database import database
import TwitchBot, sys

db = database()

def Main():
    cprint('Starting ViperTbot ...', 'green')
    try:
        TwitchBot.run()
    except KeyboardInterrupt:
        sys.exit(0)

if __name__=='__main__':
    Main()
