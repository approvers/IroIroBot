import discord
from discord.ext import tasks
import os

from MeigenBot.MessageReceiver import MessageReceiver



class Client(discord.Client):
    __TOKEN = os.environ["TOKEN"]


    def __init__(self):
        super().__init__()

        self.message_receiver = MessageReceiver(self)

    
    def run(self):
        super().run(Client.__TOKEN)

    async def on_ready(self):
        self.minute_loop.start()

        my_id = 603487410487296000
        my_user = super().get_user(my_id)

        if my_user.dm_channel is None:
            await my_user.create_dm()

        self.dm_channel = my_user.dm_channel
        
        async for message in self.dm_channel.history(limit=5):
            self.message_receiver.meigen_list.insert(0, message.content)

    async def on_message(self, message):
        await self.message_receiver.receive(message)

    @tasks.loop(seconds=60)
    async def minute_loop(self):
        pass