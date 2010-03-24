import readline
import introbot.actions

def say(msg):
    print "<< " + msg
introbot.actions.say = say

def run():
    try:
        while 1:
            line = raw_input("textbot> ")
            line.strip()
            if line.startswith("/me "):
                action = line[4:]
                introbot.actions.action('console', action)
            elif line.startswith("textbot: "):
                msg = line[9:]
                introbot.actions.talkto('console', msg)
            else:
                introbot.actions.pubmsg('console', line)
    except EOFError:
        print "BYE!"
