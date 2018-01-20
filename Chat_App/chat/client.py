from channels.auth import channel_session_user_from_http, channel_session_user
from channels import Channel
from .models import Room
import json

"""This decorator copies the user from the HTTP session (only available in
 websocket.connect or http.request messages) to the channel session (available
 i n all consumers with the same reply_channel, so all three here)"""
# todo: @ ??
@channel_session_user_from_http
def ws_connect(message):
    message.reply_channel.send({"accept": True})
    message.channel_session['rooms'] = []


""" Unsubscribes from the server """
#TODO: Make the disconnection compatible with unijive databases.
@channel_session_user
def ws_disconnect(message):
    for room_id in message.channel_session.get("rooms"):
        try:
            room = Room.objects.get(pk=room_id)
            # Removes us from the room's send group.
            room.websocket_group.discard(message.reply_channel)
        except Room.DoesNotExist:
            pass


# Receives any message from JSON in text format.
def ws_receive(message):
    payload = json.loads(message['text'])
    payload['reply_channel'] = message.content['reply_channel']
    Channel("chat.recieve").send(payload)


@channel_session_user
@catch_client_error
def chat_join(message):
    # Find the room they requested (by ID) and add ourselves to the send group
    # Note that, because of channel_session_user, we have a message.user
    # object that works just like request.user would. Security!
    room = get_room_or_error(message["room"], message.user)

    # Send a "enter message" to the room if available
    if NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS:
        room.send_message(None, message.user, MSG_TYPE_ENTER)

    # OK, add them in. The websocket_group is what we'll send messages
    # to so that everyone in the chat room gets them.
    room.websocket_group.add(message.reply_channel)
    message.channel_session['rooms'] = list(set(message.channel_session['rooms']).union([room.id]))
    # Send a message back that will prompt them to open the room
    # Done server-side so that we could, for example, make people
    # join rooms automatically.
    message.reply_channel.send({
        "text": json.dumps({
            "join": str(room.id),
            "title": room.title,
        }),
    })


@channel_session_user
@catch_client_error
def chat_leave(message):
    # Reverse of join - remove them from everything.
    room = get_room_or_error(message["room"], message.user)

    # Send a "leave message" to the room if available
    if NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS:
        room.send_message(None, message.user, MSG_TYPE_LEAVE)

    room.websocket_group.discard(message.reply_channel)
    message.channel_session['rooms'] = list(set(message.channel_session['rooms']).difference([room.id]))
    # Send a message back that will prompt them to close the room
    message.reply_channel.send({
        "text": json.dumps({
            "leave": str(room.id),
        }),
    })


@channel_session_user
@catch_client_error
def chat_send(message):
    if int(message['room']) not in message.channel_session['rooms']:
        raise ClientError("ROOM_ACCESS_DENIED")
    room = get_room_or_error(message["room"], message.user)
    room.send_message(message["message"], message.user)