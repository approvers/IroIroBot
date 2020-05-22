import discord

from IroIroBot.Command.CommandParameters import CommandParameters
from IroIroBot.Command.Meigen.MeigenSubcommandBase import MeigenSubcommandBase
from IroIroBot.Command.Meigen.MeigenHolder import MeigenHolder



class DelSubcommand(MeigenSubcommandBase):
    COMMAND = "del"
    TEMPLATE = f"{{prefix}}{{command}} {COMMAND} [添字]"
    HELP =  f"{TEMPLATE}\n" +\
            "   MEIGENを削除するよ！\n" +\
            "   添字が指定されていない場合は最新のものを削除するよ\n"


    async def run(self, params: CommandParameters):
        holder = MeigenHolder()
        
        words = params.args.split()
        if len(words) < 1:
            # 引数の指定がない場合、新しいものを削除
            await params.send(
                await holder.delete(len(holder.meigen_list))
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
            await holder.delete(int(words[0]))
        )