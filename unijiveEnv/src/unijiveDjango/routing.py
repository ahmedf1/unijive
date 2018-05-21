from channels.routing import route
from chat_app import consumers

channel_routing = [
    route("websocket.receive", consumers.ws_message),
    route("websocket.connect", consumers.ws_connect),
    route("websocket.disconnect", consumers.ws_disconnect),
]

# path=r"^/(?P<room_name>[a-zA-Z0-9_]+)/$"