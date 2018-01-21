from django.db import models
import json
import channels

from .attributes import MSG_TYPE_MESSAGE


class Room(models.Model):
    title = models.CharField(max_length=200)
    staff_only = models.BooleanField(default=False)

    def websocket_group(self):
        """ Returns the Channels Group that sockets should subscribe to to get sent
        messages as they are generated. """
        return channels.Group("room-%s" % self.title)

    # TODO: Need to make it compatible with important, muted and saved messages
    def send_message(self, message, user, msg_type=MSG_TYPE_MESSAGE):
        """
        Sends the message to the room for the user.
        :param message: The message to be sent
        :param user: The person on behalf of whom the message is being sent.
        :param msg_type: What type of message is being sent
        """

        msg = {'room': str(self.title),
               'message': message,
               'username': user.username,
               'msg_type': msg_type}

        self.websocket_group.send({'text': json.dumps(msg)})

    def __str__(self):
        return str(self.title)