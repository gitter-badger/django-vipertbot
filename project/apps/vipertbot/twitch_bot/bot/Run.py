#!/usr/bin/python
from tools.termcolor import cprint
import TwitchBot, sys, os

def Main():

    cprint('Starting ViperTbot ...', 'green')
    try:
        TwitchBot.run()
    except KeyboardInterrupt:
        sys.exit(0)

if __name__=='__main__':
    Main()
