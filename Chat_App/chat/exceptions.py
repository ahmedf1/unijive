
class ClientError(Exception):
    """
    Custom exception class that is caught by the websocket receive()
    handler and translated into a send back to the client.
    """
    def __init__(self, code):
        super(ClientError, self).init(code)
        self.code = code

    # Send's data back to the sender.
    def backtrack(self,channel):
        channel.send({
            'text'
        })
