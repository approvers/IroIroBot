import discord



class ChannelHolder:
    CHANNEL_ID_DICT = {
        "meigen" : 711911809430454325
    }
    channel_dict = {}


    @staticmethod
    def fetch_channel(get_channel_function):
        """channel_dictにチャンネルをセットする関数

        Arguments:
            get_channel_function {function} -- Client.get_channel
        """
        for channel_name, channel_id in ChannelHolder.CHANNEL_ID_DICT.items():
            ChannelHolder.channel_dict[channel_name] = get_channel_function(channel_id)

    @staticmethod
    def get_channel(channel_name: str) -> discord.TextChannel:
        """事前登録しているチャンネルを返す関数

        Arguments:
            channel_key {str} -- チャンネルの名前

        Returns:
            discord.TextChannel -- 対応するチャンネル
        """
        return ChannelHolder.channel_dict[channel_name]