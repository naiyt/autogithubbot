def parser(message):
    if 'Hello Robot, you should reply to this comment' in message.body:
        return True
    else:
        return False
