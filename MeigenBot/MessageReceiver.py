import discord



class MessageReceiver:
    def __init__(self, client:discord.Client):
        self.client = client
        self.meigen_list = []

    async def receive(self, message:discord.Message):
        if message.author.bot:
            return

        words = message.content.split()
        head = words[0]
        if head == "!meigen":
            if len(words) == 1:
                await message.channel.send(
                    "```"
                    " †軽く説明† \n"
                    "   みんなの名言（迷言）を表示してくれる神Botだよ\n"
                    " †使い方† \n"
                    "    !meigen [発言者] [名言] : 名言追加\n"
                    "    !meigen print : 名言列挙\n"
                    "```"
                )
                return

            command = words[1]

            if command == "print":
                if len(self.meigen_list) < 1:
                    return
                text = ""
                for meigen in self.meigen_list:
                    text += meigen
                await message.channel.send(text)
                return


            if len(self.meigen_list) >= 5:
                self.meigen_list = self.meigen_list[1:]

            meigen = "```\n"+message.content[len(words[1])+8:]+"\n　−−− "+words[1]+"\n```"
            self.meigen_list.append(meigen)

            await message.channel.send(meigen)
            await self.client.dm_channel.send(meigen)