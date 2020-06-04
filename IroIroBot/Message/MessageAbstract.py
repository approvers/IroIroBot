import discord
from abc import ABCMeta, abstractmethod



class MessageAbstract(metaclass=ABCMeta):
        
    @abstractmethod
    async def run(self, message: discord.Message):
        pass