from twisted.internet import reactor
from lalita import Plugin
import introbot.actions

class Introbot(Plugin):
    def init(self, config):
        self.register(self.events.ACTION, self.do_action)
        self.register(self.events.PUBLIC_MESSAGE, self.do_pubmsg)
        self.register(self.events.TALKED_TO_ME, self.do_talkto)
        self.register(self.events.COMMAND, self.do_quit, ('quit',))

        introbot.actions.say = self.do_say
        self.last_channel = None

    def do_say(self, msg):
        self.say(self.last_channel, msg)

    def do_quit(self, user, channel, command):
        self.say(channel, "sorry, bye")
        reactor.stop()

    def do_talkto(self, user, channel, msg):
        self.last_channel = channel
        introbot.actions.talkto(user, msg)

    def do_action(self, user, channel, action):
        self.last_channel = channel
        introbot.actions.action(user, action)

    def do_pubmsg(self, user, channel, msg):
        self.last_channel = channel
        introbot.actions.pubmsg(user, msg)
