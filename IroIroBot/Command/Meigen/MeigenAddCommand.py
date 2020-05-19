import discord

from IroIroBot.Command.Meigen.MeigenHolder import MeigenHolder



class MeigenAddCommand:
    ID_OPTION = "id"
    

    def __init__(self, channel: discord.TextChannel, args: str):
        self.send = channel.send
        self.fetch_message = channel.fetch_message
        self.args = args
        self.words = args.split()

    async def _send_not_decimal_err(self):
        await self.send(
                "```\n" +\
                "†キレた†\n" +\
                "   IDを指定しろカス\n" +\
                "```"
            )
        return

    async def _send_not_found_err(self):
        await self.send(
            "```\n" +\
            "†キレた†\n" +\
            "   指定したIDが貧弱だカス\n" +\
            "```"
        )
        return

    async def _send_exception(self, caught_exception: Exception):
        await self.send(
            "```\n" +\
            "†キレた†\n" +\
            "   内容だカス\n" +\
            "   {}\n".format(caught_exception) +\
            "```"
        )
        return
        

    async def run(self):
        if len(self.words) < 2:
            return

        if self.words[0] == MeigenAddCommand.ID_OPTION:
            if not self.words[1].isdecimal():
                self._send_not_decimal_err()
                return

            try:
                meigen_message = await self.fetch_message(int(self.words[1]))

            except discord.errors.NotFound:
                await self._send_not_found_err()
                return

            except Exception as caught_exception:
                await self._send_exception(caught_exception)
                return

            name = meigen_message.author.name
            text = meigen_message.content
            await self.send(
                await MeigenHolder().append(name, text)
            )
            return

        name = self.words[0]
        text = self.args[len(name):].lstrip()
        await self.send(
            await MeigenHolder().append(name, text)
        )
        return