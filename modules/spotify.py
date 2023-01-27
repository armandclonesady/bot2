import interactions

class Spotify(interactions.Extension):
    def __init__(self, client):
        self.client = client

    @interactions.extension_message_command()
    async def on_command():
        pass

def setup(client):
    Spotify(client)