from channels.routing import route, include
from chat_app import consumers

channel_routing = [
    route("websocket.connect", consumers.ws_connect, path=r'^/(?P<room>[a-zA-Z0-9]+)/$'),
    route("websocket.receive", consumers.ws_message, path=r'^/(?P<room>[a-zA-Z0-9]+)/$'),
    route("websocket.disconnect", consumers.ws_disconnect, path=r'^/(?P<room>[a-zA-Z0-9]+)/$'),
]


# channel_routing = [
#     include(websocket_routing, path="^/chat_page")
# ]
