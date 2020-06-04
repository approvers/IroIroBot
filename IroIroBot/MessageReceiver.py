import discord

from IroIroBot.Message.ChinChinSamuraiGame import ChinChinSamuraiGame



class MessageReceiver:
    def __init__(self):
        self.instances = [ChinChinSamuraiGame()]

    async def receive(self, message: discord.Message):
        for instance in self.instances:
            await instance.run(message)