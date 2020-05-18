import discord
from discord.ext import tasks
import os

from IroIroBot.ChannelHolder import ChannelHolder
from IroIroBot.MessageRoot import MessageRoot



class Client(discord.Client):
    __TOKEN = os.environ["TOKEN"]


    def __init__(self):
        super().__init__()
        self.message_root = MessageRoot()


    def run(self):
        super().run(Client.__TOKEN)

    async def on_ready(self):
        ChannelHolder.fetch_channel(self.get_channel)

        self.hour_loop.start()

    async def on_message(self, message: discord.Message):
        self.message_root.receive(message)

    @tasks.loop(minutes=60)
    async def hour_loop(self):
        pass