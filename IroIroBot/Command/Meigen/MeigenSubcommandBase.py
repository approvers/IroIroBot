import discord
from abc import ABCMeta, abstractmethod

from IroIroBot.Command.CommandParameters import CommandParameters



class MeigenSubcommandBase(metaclass=ABCMeta):
    COMMAND = None
    HELP = None


    def __new__(cls, *_, **__):
        if cls.COMMAND is None:
            raise AttributeError("COMMAND is undefined")
        if cls.HELP is None:
            raise AttributeError("HELP is undefined")
        self = super().__new__(cls)
        return self
        
    @abstractmethod
    async def run(self, params: CommandParameters):
        pass