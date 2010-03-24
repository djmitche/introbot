import os, pwd, sys
import logging
import lalita.ircbot
import introbot.actions

def introbot():
    if len(sys.argv) < 2:
        print "specify a channel name with no hash: introbot mychannel"
        return

    # Servers Configuration Settings
    servers = {
            'freenode': dict (
                encoding='utf8',
                host='irc.freenode.net', port=6667,
                nickname=pwd.getpwuid(os.getuid())[0] + "bot",
                lang='en',
                channels= {
                    '#' + sys.argv[1]: {},
                },
                plugins= {
                    'lalita.plugins.misc.Ping': { },
                    'introbot.plugin.Introbot': { },
                },
            ),
        }

    lalita.ircbot.plugins_loglvl = {}
    lalita.ircbot.main(servers.values(), {}, None)

def textbot():
    import introbot.textbot
    introbot.textbot.run()
