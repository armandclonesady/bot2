import interactions
from functions import reloadAllModules


if __name__ == '__main__':
    client = interactions.Client(open("token.txt", "r").readline())
    client.load("modules.startup")
    client.load("modules.spotify")

    @client.command(
        name="reload",
        description="on test frr",
    )
    async def reload(ctx: interactions.CommandContext):
        message = await ctx.send("Working on it!!")
        await reloadAllModules(client)
        await message.edit("Reloaded all modules")
    
    @client.command(
        name="add-to-list",
        description="Adds your id to the json (only makes it so it'll read your Rich Presence)",

    )
    async def addToList(ctx: interactions.CommandContext):
        pass
        
    client.start()