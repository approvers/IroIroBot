import discord

from IroIroBot.Command.CommandParameters import CommandParameters
from IroIroBot.Command.MeigenCommand import MeigenCommand



class CommandReceiver:
    PREFIX = "!"
    PREFIX_LEN = len(PREFIX)


    def __init__(self):
        self.commands = [MeigenCommand()]
    
    async def receive(self, message: discord.Message):
        HEAD = message.content.split()[0]
        HEAD = HEAD[CommandReceiver.PREFIX_LEN:]

        for command in self.commands:
            if HEAD != command.COMMAND:
                continue

            words = message.content.split()
            if len(words) < 2:
                await command.send_help(
                    message.channel, CommandReceiver.PREFIX
                )
                return
            
            args = message.content[len(words[0]):].lstrip()
            await command.run(
                CommandParameters(message, args)
            )
            return