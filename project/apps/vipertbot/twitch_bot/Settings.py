from project.env import env_settings

HOST = "irc.twitch.tv"
PORT = 6667
PASS = env_settings.OAUTHKEY
IDENT = "vipertbot"
CHANNELS = []
#CHANNELS = db.getChannels()