import sqlite3 as lite
from tools.termcolor import cprint

class database:

    def __init__(self):
        self.sqlite_database = '../database/vtb_database.sqlite'
        self.cur = False
        self.con = False

    def connect(self):
        self.con = lite.connect(self.sqlite_database, isolation_level=None, timeout=30000)
        self.cur = self.con.cursor()

    def close(self):
        if self.cur:
            self.cur.close()
        if self.con:
                self.con.close()

    def getJob(self):
        try:
            self.connect()
            self.cur.execute("""SELECT cmd FROM jobs""")
            data = self.cur.fetchone()
            self.close()

            try:
                return data[0]
            except Exception:
                return False

        except lite.OperationalError, e:
            self.printError(e.args[0])

    def getRegular(self, name):
        try:
            self.connect()
            self.cur.execute("""SELECT name FROM regulars WHERE name='%s'""" % (name,))
            data = self.cur.fetchone()
            self.close()

            try:
                return data[0]
            except Exception:
                return 0

        except lite.OperationalError, e:
            self.printError(e.args[0])

    def getCooldown(self, command, channel):
        try:
            self.connect()
            self.cur.execute("""SELECT start_time FROM cooldowns WHERE command='%s' AND channel='%s'""" % (command, channel))
            data = self.cur.fetchone()
            self.close()

            try:
                return data[0]
            except Exception:
                return 0

        except lite.OperationalError, e:
            self.printError(e.args[0])

    def insertCooldown(self, command, channel, start_time):
        try:
            self.connect()
            self.cur.execute("""INSERT INTO cooldowns('command', 'channel', 'start_time')
                                VALUES (?, ?, ?)""", (command, channel, start_time))

            result = self.cur.rowcount
            self.con.commit()
            self.close()

            if result > 0:
                return True

            cprint('Error: no rows affected : ' + repr(command+':'+channel+':'+start_time), 'red')
            return False

        except lite.OperationalError, e:
            self.printError(e.args[0])

    def deleteCooldown(self, command, channel):
        try:
            self.connect()
            self.cur.execute("""DELETE FROM cooldowns WHERE command='%s' AND channel='%s'""" % (command, channel))
            result = self.cur.rowcount
            self.con.commit()
            self.close()

            if result > 0:
                return True

            cprint('Error: no rows affected : ' + repr(command+':'+channel), 'red')
            return False

        except lite.OperationalError, e:
            self.printError(e.args[0])

    def deleteJob(self, cmd):
        try:
            self.connect()
            self.cur.execute("""DELETE FROM jobs WHERE cmd='%s'""" % (cmd,))
            result = self.cur.rowcount
            self.con.commit()
            self.close()

            if result > 0:
                return True

            cprint('Error: no rows affected : ' + repr(cmd), 'red')
            return False

        except lite.OperationalError, e:
            self.printError(e.args[0])

    def getChannels(self):
        try:
            self.connect()
            self.cur.execute("""SELECT username FROM users""")
            data = self.cur.fetchall()
            self.close()

            try:
                return data[0]
            except Exception:
                return []

        except lite.OperationalError, e:
            self.printError(e.args[0])

    def getUserIdByUsername(self, username):
        try:
            self.connect()
            self.cur.execute("""SELECT id FROM users WHERE username='%s'""" % (username,))
            data = self.cur.fetchone()
            self.close()

            try:
                return data[0]
            except Exception:
                return 0

        except lite.OperationalError, e:
            self.printError(e.args[0])

    def getUserCommands(self, uid):
        try:
            self.connect()
            self.cur.execute("""SELECT id, command, text, cooldown, active FROM commands WHERE user_id=%i""" % (uid,))
            data = self.cur.fetchall()
            self.close()

            try:
                return data
            except Exception:
                return ""

        except lite.OperationalError, e:
            self.printError(e.args[0])

    def getCommandState(self, uid, command):
        try:
            self.connect()
            self.cur.execute("""SELECT active FROM commands WHERE user_id=%i AND command='%s'""" % (uid, command))
            data = self.cur.fetchone()
            self.close()

            try:
                return data[0]
            except Exception:
                return ""

        except lite.OperationalError, e:
            self.printError(e.args[0])

    def getCommandPermissions(self, id):
        try:
            self.connect()
            self.cur.execute("""SELECT id FROM permissions p LEFT JOIN command_permission cp ON cp.permission_id = p.id WHERE cp.command_id = '%i'""" % (id,))
            data = self.cur.fetchall()
            self.close()

            try:
                return data
            except Exception:
                return []

        except lite.OperationalError, e:
            self.printError(e.args[0])

    def getCommandText(self, uid, command):
        try:
            self.connect()
            self.cur.execute("""SELECT text FROM commands WHERE user_id=%i AND command='%s'""" % (uid, command))
            data = self.cur.fetchone()
            self.close()

            try:
                return data[0]
            except Exception:
                return ""

        except lite.OperationalError, e:
            self.printError(e.args[0])

    def printError(self, error):
        cprint("Error %s:" % error, 'red')