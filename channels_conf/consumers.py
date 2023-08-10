from channels import Group


def ws_add(message):
    message.reply_channel.send({"accept": True})
    Group("chat").add(message.reply_channel)


def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)


def test_channel(message):
    print('recieved message')
    print(message)
