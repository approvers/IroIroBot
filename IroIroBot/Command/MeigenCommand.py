import discord

from IroIroBot.Command.CommandParameters import CommandParameters
from IroIroBot.Command.CommandBase import CommandBase
from IroIroBot.Command.Meigen.MeigenAddCommand import MeigenAddCommand
from IroIroBot.Command.Meigen.PrintSubcommand import PrintSubcommand
from IroIroBot.Command.Meigen.DelSubcommand import DelSubcommand
from IroIroBot.Command.Meigen.RandomSubcommand import RandomSubcommand
from IroIroBot.Command.Meigen.MeigenHolder import MeigenHolder



class MeigenCommand(CommandBase):
    COMMAND = "meigen"
    TEMPLATE = f"{{prefix}}{COMMAND} [Subcommand] ..."
    HELP = f"{TEMPLATE}\n\
        ***†MEIGEN†***を管理するよ"


    def __init__(self):
        self.subcommands = [PrintSubcommand(), DelSubcommand(), RandomSubcommand()]

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
        text =  f"{prefix}{MeigenCommand.COMMAND} [発言者] [内容]\n" +\
                f"{prefix}{MeigenCommand.COMMAND} id [メッセージID]\n" +\
                "   MEIGENを追加するよ！かわいいね！！\n"

        for subcommand in self.subcommands:
            text += "\n" + subcommand.HELP.format(
                prefix=prefix, 
                command=MeigenCommand.COMMAND
            )

        await channel.send(
            "```" + text + "```"
        )