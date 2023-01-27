import interactions
from functions import reloadAllModules


if __name__ == '__main__':
    client = interactions.Client(open("token.txt", "r").readline())
    client.load("modules.startup")
    client.load("modules.spotify")
    client.load("modules.jsonlist")

    @client.command(
        name="reload",
        description="reloads all modules to update them if needed (only for the owner of the bot)",
    )
    async def reload(ctx: interactions.CommandContext):
        message = await ctx.send("Working on it!!")
        await reloadAllModules(client)
        await message.edit("Reloaded all modules")
    async def addToList(ctx: interactions.CommandContext):
        pass
        
    client.start()