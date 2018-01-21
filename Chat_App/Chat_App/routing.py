# todo: install channels into unijiveEnv.
from channels import route

def message_handler(message):
    print(message['text'])

channel_routing = [
    route("websocket.receive", message_handler)  # todo: Find out what this means
]
