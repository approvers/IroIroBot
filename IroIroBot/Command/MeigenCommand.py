import discord

from IroIroBot.Command.CommandBase import CommandBase
from IroIroBot.Command.Meigen.PrintSubcommand import PrintSubcommand



class MeigenCommand(CommandBase):
    COMMAND = "meigen"
    TEMPLATE = f"{{prefix}}{COMMAND} [Subcommand] ..."
    HELP = f"{TEMPLATE}\n\
        ***†MEIGEN†***を管理するよ"


    async def run(self, message: discord.Message):
        pass
    
    async def send_help(self, channel: discord.TextChannel, prefix: str):
        pass