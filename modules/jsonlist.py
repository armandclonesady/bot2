import interactions
import json
from functions import accessJsonFile

class JsonList(interactions.Extension):
    def __init__(self, client):
        self.client = client

    @interactions.extension_command(
        name="add_to_json",
        description="add your id to the json file",
    )
    async def add_to_json(self, ctx: interactions.CommandContext):
        file = accessJsonFile()
        for i in file[ids]:
            await ctx.send(f'here: {i}')
        

def setup(client):
    JsonList(client)