import discord
import random

from IroIroBot.Message.MessageAbstract import MessageAbstract



class ChinChinSamuraiGame(MessageAbstract):
    KEY_WORDS = ["ちんちん", "おちんちん", "侍", "ちんちん侍"]
    RESPONSES = {
        "おちんちん" : "びろーん",
        "侍" : "シャキーン",
        "ちんちん侍" : "ちんちん侍！",
    }


    async def _respond(self, key: str, send_func):
        response = self.RESPONSES.get(key, None)
        if(response is None):
            return

        await send_func(response)

    async def _request(self, send_func):
        request = random.choice(self.KEY_WORDS)
        await send_func(request)

        if(request == "ちんちん侍"):
            await send_func(self.RESPONSES["ちんちん侍"])


    async def run(self, message: discord.Message):
        for key in self.KEY_WORDS:
            if (message.content != key):
                continue

            send_func = message.channel.send

            await self._respond(key, send_func)
            await self._request(send_func)