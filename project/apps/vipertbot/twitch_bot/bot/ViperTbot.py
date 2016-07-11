#!/usr/bin/python

import ircbot, Settings, sys
from tools.termcolor import cprint

def Main():
    cprint('Starting ViperTbot ...', 'green')
    try:
        bot = ircbot.SingleServerIRCBot([
            (Settings.HOST,Settings.PORT, Settings.PASS)
        ], Settings.IDENT, 'ViperTbot')

        bot.start()

    except KeyboardInterrupt:
        sys.exit(0)

if __name__=='__main__':
    Main()