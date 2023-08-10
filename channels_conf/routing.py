from channels.routing import route

from channels_conf.consumers import ws_add, ws_disconnect, test_channel

channel_routing = [
    route('websocket.connect', ws_add),
    route('websocket.disconnect', ws_disconnect),
    route('testing', test_channel),
]
