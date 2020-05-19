import discord



class CommandParameters:
    """
    コマンドに渡す引数の集まり
    """

    def __init__(
        self,
        message: discord.Message,
        args: str
    ):
        self.message = message
        self.args = args
        self.send = message.channel.send

    def new_param(self, args: str):
        """CommandParametersを新しく生成して返す

        Arguments:
            args {str} -- 引数

        Returns:
            CommandParameters -- 新しいCommandParameters
        """
        return CommandParameters(self.message, args)