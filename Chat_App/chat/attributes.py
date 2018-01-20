#todo: Look into this settings configuration
from django.conf import settings

NOTIFY_ENTER_AND_LEAVE = getattr(settings, "NOTIFY_ENTER_AND_LEAVE", True)

MSG_TYPE_MESSAGE = 0 # STANDARD MESSAGE
MSG_TYPE_IMPORTANT = 1 # IMPORTANT MESSAGE
MSG_TYPE_MUTED = 2 # MUTED MESSAGES
MSG_TYPE_SAVED = 3 # MESSAGE SAVED

MESSAGE_TYPES_CHAT = getattr(settings, 'MESSAGE_TYPES_CHOICES', (
    (MSG_TYPE_MESSAGE, 'MESSAGE'),
    (MSG_TYPE_IMPORTANT, 'IMPORTANT'),
    (MSG_TYPE_MUTED, 'MUTED'),
    (MSG_TYPE_SAVED, 'SAVED')))

MESSAGE_TYPES_LIST = getattr(settings, 'MESSAGE_TYPES_LIST',
                             [MSG_TYPE_MESSAGE,
                              MSG_TYPE_IMPORTANT,
                              MSG_TYPE_MUTED,
                              MSG_TYPE_SAVED])
