import discord

from IroIroBot.Singleton import Singleton



class ChannelHolder(Singleton):
    CHANNEL_ID_DICT = {
        "meigen" : 711911809430454325
    }


    def _set_up(self):
        self.channel_dict = {}
        
    def fetch_channel(self, get_channel_function):
        """channel_dictにチャンネルをセットする関数

        Arguments:
            get_channel_function {function} -- Client.get_channel
        """
        for channel_name, channel_id in ChannelHolder.CHANNEL_ID_DICT.items():
            self.channel_dict[channel_name] = get_channel_function(channel_id)

    def get_channel(self, channel_name: str) -> discord.TextChannel:
        """事前登録しているチャンネルを返す関数

        Arguments:
            channel_key {str} -- チャンネルの名前

        Returns:
            discord.TextChannel -- 対応するチャンネル
        """
        return self.channel_dict[channel_name]