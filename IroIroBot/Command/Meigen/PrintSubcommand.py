from IroIroBot.Command.Meigen.MeigenSubcommandBase import MeigenSubcommandBase



class PrintSubcommand(MeigenSubcommandBase):
    DEFAULT_NUM = 5

    COMMAND = "print"
    TEMPLATE = "{{prefix}}{{command}} {subcommand} [表示数={default_num}]" \
        .format(subcommand=COMMAND, default_num=DEFAULT_NUM)
    HELP = "{TEMPLATE}\n\
        MEIGENを表示するよ！"



    async def run(self, args: str):
        pass