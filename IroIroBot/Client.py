import discord
from discord.ext import tasks
import os

from IroIroBot.ChannelHolder import ChannelHolder
from IroIroBot.Command.Meigen.MeigenHolder import MeigenHolder
from IroIroBot.MessageRoot import MessageRoot



class Client(discord.Client):
    __TOKEN = os.environ["TOKEN"]


    def __init__(self):
        super().__init__()
        self.message_root = MessageRoot()


    def run(self):
        super().run(Client.__TOKEN)

    async def on_ready(self):
        channel_holder = ChannelHolder()
        meigen_holder = MeigenHolder()
        meigen_holder._set_up()
        channel_holder.fetch_channel(self.get_channel)

        #TODO ここをクラス化
        async for message in channel_holder.get_channel("meigen").history(limit=MeigenHolder.HOLD_LIMIT):
            meigen_holder.prepend(message.content)

        self.hour_loop.start()

    async def on_message(self, message: discord.Message):
        await self.message_root.receive(message)

    @tasks.loop(minutes=60)
    async def hour_loop(self):
        pass