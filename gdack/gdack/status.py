

def Status(Text, Channel, User):
    try:
        message = "this is the statys command"
    except Exception as e:
        print(e)
        message = "*Error:* There was a problem running that command:\n```" + str(e) + "```"
    return message
