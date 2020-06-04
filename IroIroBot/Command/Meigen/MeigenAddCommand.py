import discord

from IroIroBot.Command.Meigen.MeigenHolder import MeigenHolder



class MeigenAddCommand:
    ID_OPTION = "id"
    MESSAGE_ID_MAX = 9223372036854775807
    

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

    async def _send_max_over_err(self):
        await self.send(
            "```\n" +\
            "†キレた†\n" +\
            "   指定したIDが不適切だカス\n" +\
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

    async def replace_and_send(self, name: str, text: str):
        new_name = name.replace('`', '\'')
        new_text = text.replace('`', '\'')

        await self.send(
            await MeigenHolder().append(new_name, new_text)
        )
        
    async def run(self):
        if len(self.words) < 2:
            return

        if self.words[0] == MeigenAddCommand.ID_OPTION:
            if not self.words[1].isdecimal():
                await self._send_not_decimal_err()
                return

            try:
                message_id = int(self.words[1])
                if (message_id > self.MESSAGE_ID_MAX):
                    await self._send_max_over_err()
                    return

                meigen_message = await self.fetch_message()

            except discord.errors.NotFound:
                await self._send_not_found_err()
                return

            except Exception as caught_exception:
                await self._send_exception(caught_exception)
                return

            name = meigen_message.author.name
            text = meigen_message.content
            await self.replace_and_send(
                name, text
            )
            return

        name = self.words[0]
        text = self.args[len(name):].lstrip()
        await self.replace_and_send(
            name, text
        )
        return