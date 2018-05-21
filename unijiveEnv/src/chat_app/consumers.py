"""
Where all the incoming data from the websockets is handled.
Similar to the views.py file.
"""
import json
from channels import Group
from channels.sessions import channel_session
from urllib.parse import parse_qs


# Connected to websocket.connect
@channel_session
def ws_connect(message):
    # Accept connection
    message.reply_channel.send({"accept": True})
    # Parse the query string
    params = parse_qs(message.content["query_string"])
    # print(room_name)
    print(params)
    if (b"username" in params) and (b'room' in params):
        # Set the username in the session
        message.channel_session["username"] = params[b"username"][0].decode("utf8")
        message.channel_session["room"] = params[b"room"][0].decode("utf8")
        # Add the user to the room_name group
        Group("chat-%s" % params[b'room'][0].decode("utf8")).add(message.reply_channel)
    else:
        # Close the connection.
        message.reply_channel.send({"close": True})


# Connected to websocket.receive
@channel_session
def ws_message(message):
    Group("chat-%s" % message.channel_session["room"]).send({
        "text": json.dumps({
            "text": message["text"],
            "username": message.channel_session["username"],
        }),
    })


# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message):
    Group("chat-%s" % message.channel_session["room"]).discard(message.reply_channel)