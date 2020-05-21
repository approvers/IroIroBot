import discord
import random

from IroIroBot.Command.CommandParameters import CommandParameters
from IroIroBot.Command.Meigen.MeigenSubcommandBase import MeigenSubcommandBase
from IroIroBot.Command.Meigen.MeigenHolder import MeigenHolder



class RandomSubcommand(MeigenSubcommandBase):
    DEFAULT_NUM = 1
    
    COMMAND = "random"
    TEMPLATE = f"{{prefix}}{{command}} {COMMAND} [表示数={DEFAULT_NUM}]"
    HELP =  f"{TEMPLATE}\n" +\
            "   MEIGENをランダム表示するよ！\n"


    async def run(self, params: CommandParameters):
        words = params.args.split()
        if len(words) < 1:
            await params.send(
                MeigenHolder().random(RandomSubcommand.DEFAULT_NUM)
            )
            return

        if not words[0].isdecimal():
            await params.send(
                "```\n" +\
                "†キレた†\n" +\
                "   まともな数字入力しろよカス\n" +\
                "```"
            )
            return

        await params.send(
            MeigenHolder().random(int(words[0]))
        )