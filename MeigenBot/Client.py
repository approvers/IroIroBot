import discord
from discord.ext import tasks
import os

from MeigenBot.MessageReceiver import MessageReceiver



class Client(discord.Client):
    __TOKEN = os.environ["TOKEN"]


    def __init__(self):
        super().__init__()
    
    def run(self):
        super().run(Client.__TOKEN)

    async def on_ready(self):
        send_channel = self.get_channel(690909527461199922)
        voice_channel = self.get_channel(683939861539192865)
        my_user = self.get_user(603487410487296000)
        if my_user.dm_channel is None:
            await my_user.create_dm()
        dm_channel = my_user.dm_channel
        self.message_receiver = MessageReceiver(send_channel, voice_channel, dm_channel)

        async for message in dm_channel.history(limit=10):
            if len(message.content) > 100:
                continue
            self.message_receiver.meigen_list.insert(0, message.content)
        
        await send_channel.send("おっぱい！（再起動）")
        self.hour_loop.start()

    async def on_message(self, message):
        await self.message_receiver.receive(message)

    @tasks.loop(minutes=60)
    async def hour_loop(self):
        await self.message_receiver.random_event()
