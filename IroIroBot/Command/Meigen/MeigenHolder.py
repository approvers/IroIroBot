import random

from IroIroBot.Singleton import Singleton
from IroIroBot.ChannelHolder import ChannelHolder



class MeigenHolder(Singleton):
    LEN_LIMIT = 50
    HOLD_LIMIT = 30
    FORMAT = \
        "```\n" +\
        "{text}\n" +\
        "    --- {name}\n" +\
        "```"


    def _set_up(self):
        self.meigen_list = []

    def prepend(self, meigen: str):
        self.meigen_list.insert(0, meigen)

    async def append(self, name: str, text: str) -> str:
        if len(name) + len(text) > MeigenHolder.LEN_LIMIT:
            return \
                "```\n" +\
                "†キレた†\n" +\
                f"   名前と内容の合計は{MeigenHolder.LEN_LIMIT}以下にしろカス\n" +\
                "```"

        meigen = MeigenHolder.FORMAT.format(
            name=name, text=text
        )
        self.meigen_list.append(meigen)
        if len(self.meigen_list) > MeigenHolder.HOLD_LIMIT:
            self.meigen_list = self.meigen_list[1:]

        await ChannelHolder().get_channel("meigen").send(meigen)
        return  f"[{len(self.meigen_list)}]\n" +\
                f"{meigen}\n"

    def print(self, number: int) -> str:
        if number <= 0 or MeigenHolder.HOLD_LIMIT < number:
            return \
                "```\n" +\
                "†キレた†\n" +\
                f"   1~{MeigenHolder.HOLD_LIMIT}以内にしろよカス\n" +\
                "```"
        
        text = ""
        if number > len(self.meigen_list):
            number = len(self.meigen_list)

        for i in range(number):
            index = len(self.meigen_list) + i - number
            if index < 0:
                break

            text += f"[{index+1}]\n" +\
                    f"{self.meigen_list[index]}\n"

        return text

    async def delete(self, index: int) -> str:
        if index <= 0 or MeigenHolder.HOLD_LIMIT < index:
            return \
                "```\n" +\
                "†キレた†\n" +\
                f"   1~{MeigenHolder.HOLD_LIMIT}以内にしろよカス\n" +\
                "```"

        if index > len(self.meigen_list):
            return \
                "```\n" +\
                "†キレた†\n" +\
                f"   その添字は正しくないよカス\n" +\
                "```"
        
        meigen_channel = ChannelHolder().get_channel("meigen")
        del_message_index = len(self.meigen_list) - index
        count = 0
        async for history_message in meigen_channel.history():
            if count != del_message_index:
                count += 1
                continue

            await history_message.delete()
            break

        del_meigen = self.meigen_list.pop(index-1)
        return "[削除しました]\n" + del_meigen

    def random(self, number: int) -> str:
        index_list = [i for i in range(1, len(self.meigen_list)+1)]
        random.shuffle(index_list)

        if number <= 0 or len(self.meigen_list) < number:
            return \
                "```\n" +\
                "†キレた†\n" +\
                f"   1~{len(self.meigen_list)}以内にしろよカス\n" +\
                "```"
        
        text = ""
        for i in range(number):
            text += f"{self.meigen_list[index_list[i]]}\n"
        
        return text