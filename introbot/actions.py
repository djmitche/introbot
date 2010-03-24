def talkto(user, message):
    # someone is talking to us; talk back
    say("nice to hear from you: " + message)

def action(user, action):
    # someone did something in the channel
    pass

def pubmsg(user, msg):
    # someone posted a regular, public message
    say("cool!")
