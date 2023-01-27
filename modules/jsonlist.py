import interactions

class JsonList(interactions.Extension):
    def __init__(self, client):
        self.client = client

    @interactions.extension_message_command()
    async def on_command():
        pass

def setup(client):
    JsonList(client)