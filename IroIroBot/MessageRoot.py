import discord

from IroIroBot.MessageReceiver import MessageReceiver
from IroIroBot.CommandReceiver import CommandReceiver



class MessageRoot:
    def __init__(self):
        message_receiver = MessageReceiver()
        command_receiver = CommandReceiver()

    async def receive(self, message: discord.Message):
        if message.author.bot:
            return


        await message_receiver.receive(message)