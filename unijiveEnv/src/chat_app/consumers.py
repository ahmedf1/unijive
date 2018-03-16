"""
Where all the incoming data from the websockets is handled.
Similar to the views.py file.
"""
import json
from channels import Group
from channels.sessions import channel_session
from urllib.parse import parse_qs
from channels.security.websockets import allowed_hosts_only

# Connects to the websocket.
@allowed_hosts_only
@channel_session
def ws_connect(message, room):
    message.reply_channel.send({"accept": True})
    params = parse_qs(message.content["query_string"])
    if b"username" in params:
        print(params[b"username"])
        message.channel_session["username"] = params[b"username"][0].decode("utf8")
        Group("chat-%s" % room).add(message.reply_channel)
    else:
        message.reply_channel.send({"close": True})


# Handles a received message by sending it to the entire group
@channel_session
def ws_message(message, room):
    print(message.content['text'])
    Group("chat-%s" % room).send({
        "text": json.dumps({
            "text": message.content["text"],
            "username": message.channel_session["username"],
        }),
    })


# Handles a person leaving the chat.
def ws_disconnect(message, room):
    Group("chat-%s" % room).discard(message.reply_channel)
