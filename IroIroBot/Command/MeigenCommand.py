import discord

from IroIroBot.Command.CommandParameters import CommandParameters
from IroIroBot.Command.CommandBase import CommandBase
from IroIroBot.Command.Meigen.MeigenAddCommand import MeigenAddCommand
from IroIroBot.Command.Meigen.PrintSubcommand import PrintSubcommand
from IroIroBot.Command.Meigen.MeigenHolder import MeigenHolder



class MeigenCommand(CommandBase):
    COMMAND = "meigen"
    TEMPLATE = f"{{prefix}}{COMMAND} [Subcommand] ..."
    HELP = f"{TEMPLATE}\n\
        ***†MEIGEN†***を管理するよ"


    def __init__(self):
        self.subcommands = [PrintSubcommand()]

    async def run(self, params: CommandParameters):
        HEAD = params.args.split()[0]

        for subcommand in self.subcommands:
            if HEAD != subcommand.COMMAND:
                continue

            new_args = params.args[len(HEAD):].lstrip()
            await subcommand.run(
                params.new_param(new_args)
            )
            return

        await MeigenAddCommand(params.message.channel, params.args).run()
        
    async def send_help(self, channel: discord.TextChannel, prefix: str):
        pass