import interactions

class Spotify(interactions.Extension):
    def __init__(self, client):
        self.client = client

    @interactions.extension_command(
        name="spotify",
        description="get the song you are listening to",
    )
    async def spotify(self, ctx: interactions.CommandContext):
        activity = None
        if activity is not None:
            await ctx.send(f"{activity.name}")
        else:
            await ctx.send(f"You are not listening to anything, also does this work? {ctx.user.email}")




def setup(client):
    Spotify(client)