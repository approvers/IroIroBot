import discord
from discord.ext import tasks
import os

from IroIroBot.ChannelHolder import ChannelHolder



class Client(discord.Client):
    __TOKEN = os.environ["TOKEN"]

    
    def run(self):
        super().run(Client.__TOKEN)

    async def on_ready(self):
        ChannelHolder.fetch_channel(self.get_channel)

        self.hour_loop.start()

    async def on_message(self, message):
        pass

    @tasks.loop(minutes=60)
    async def hour_loop(self):
        pass