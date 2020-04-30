import discord
import random



class MessageReceiver:
    def __init__(self, send_channel, voice_channel, dm_channel):
        self.send_channel = send_channel
        self.voice_channel = voice_channel
        self.dm_channel = dm_channel
        self.meigen_list = []

    async def receive(self, message:discord.Message):
        if message.author.bot:
            return

        content = message.content

        if "なん" in content or "何" in content or "ナン" in content:
            nans = ["ナン！", "ナンですね", "ナンじゃん", "ナン！？","ん？今ナンって言ったよね？", "NaN"]
            await message.channel.send(random.choice(nans))

        if "美少女" in content:
            await message.channel.send("呼ばれた気がした")
            
        if content == "おやすみ":
            await message.channel.send("おやすみなさい")
            if len(self.meigen_list) < 1:
                    return

            content = random.choice(self.meigen_list)
            await message.channel.send(content)
            return
        
        words = content.split()
        head = words[0]
        if head == "!meigen":
            if len(words) == 1:
                await message.channel.send(
                    "```"
                    " †軽く説明† \n"
                    "   みんなの名言（迷言）を表示してくれる神Botだよ\n"
                    " †使い方† \n"
                    "    !meigen [発言者] [名言]    : 名言追加\n"
                    "    !meigen print [名言数=5]   : 名言列挙\n"
                    "    !meigen random             : ランダムで名言表示\n"
                    "```"
                )
                return

            command = words[1]

            if command == "print":
                if len(self.meigen_list) < 1:
                    return

                meigen_lim = 5
                #名言数が指定されているか
                if len(words) == 3:
                    #キャスト可能か
                    try:
                        int(words[2])
                    except:
                        await message.channel.send(
                            "```"
                            " †キレた† \n"
                            "   整数指定しろよカス\n"
                            "```"
                        )
                        return

                    meigen_lim = int(words[2])
                    #入力された整数が制約を満たしているか
                    if not (0 < meigen_lim <= 10):
                        await message.channel.send(
                            "```"
                            " †キレた† \n"
                            "   1~10以内にしろよカス\n"
                            "```"
                        )
                        return

                text = ""
                for i in range(len(self.meigen_list)):
                    if i >= meigen_lim:
                        break
                    text = self.meigen_list[-(i+1)] + text
                
                await message.channel.send(text)
                return

            if command == "random":
                if len(self.meigen_list) < 1:
                    return

                content = random.choice(self.meigen_list)
                await message.channel.send(content)
                return

            #ここから名言追加の処理
            if len(message.content) > 100:
                await message.channel.send(
                    "```"
                    " †キレた† \n"
                    "   100文字以内にしろよカス\n"
                    "```"
                )
                return
            
            if len(self.meigen_list) >= 10:
                self.meigen_list = self.meigen_list[1:]

            meigen = "```\n"+content[len(words[1])+8:].replace('`', '\'')+"\n　−−− "+words[1].replace('`', '\'')+"\n```"
            self.meigen_list.append(meigen)

            await message.channel.send(meigen)
            await self.dm_channel.send(meigen)
            
    async def random_event(self):
        if len(self.voice_channel.members) == 0:
            return

        if len(self.meigen_list) < 1:
            return

        content = random.choice(self.meigen_list)
        await self.send_channel.send(content)