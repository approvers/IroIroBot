import discord
from abc import ABCMeta, abstractmethod



class CommandBase(metaclass=ABCMeta):
    COMMAND = None
    HELP = None
    # WARNING {prefix}を必ず用意する


    def __new__(cls, *_, **__):
        if cls.COMMAND is None:
            raise AttributeError("COMMAND is undefined")
        if cls.HELP is None:
            raise AttributeError("HELP is undefined")
        self = super().__new__(cls)
        return self
        
    @abstractmethod
    async def run(self, message: discord.Message):
        pass

    @abstractmethod
    async def send_help(self, channel: discord.TextChannel, prefix: str):
        pass