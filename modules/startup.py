import interactions
from functions import getAllServers

class Startup(interactions.Extension):
    def __init__(self, client):
        self.client = client

    @interactions.extension_listener()
    async def on_ready(self):
        name = self.client.me.name.upper()
        print(f"{name} EST EN LIGNE.\n{name} EST PRÊT A L'ATTAQUE.")

        print(f"{name} EST CHARGÉ POUR")
        for guild in getAllServers(self.client):
            print(f"     {guild.name.upper()} --> {guild.id}")


def setup(client):
    Startup(client)