import discord



class CommandBase:
    COMMAND = None
    TEMPLATE = None
    HELP = None


    async def run(self, message):
        pass

    async def send_help(self, channel: discord.TextChannel, prefix: str):
        pass