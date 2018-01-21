from functools import wraps # what does this do??
from .exceptions import ClientError
from .models import Room

def catch_client_error(func):
    @wraps(func) # Courtesy of gearheart.io
    def inner(message, args, **kwargs):
        try:
            return func(message, args, **kwargs)
        except ClientError as e:
            # Sends error string back to client.
            e.backtrack(message.reply_channel)

    return inner

def get_room_or_error(room_id, user):
    """
    Tries to fetch a room for the user, checking permissions along the way.
    """
    # Check if the user is logged in
    # TODO: Has to be configured with unijive app.
    if not user.is_authenticated():
        raise ClientError("USER_HAS_TO_LOGIN")
    # Find the room they requested (by ID)
    # TODO: Has to be configured with unijive models.
    try:
        room = Room.objects.get(pk=room_id)
    except Room.DoesNotExist:
        raise ClientError("ROOM_INVALID")