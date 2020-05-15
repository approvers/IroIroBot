import discord
import random



def wordsInContent(words:list, content:str) -> bool:
    for word in words:
        if word in content:
            return True
    return False


class MessageReceiver:
    def __init__(self, send_channel, voice_channel, dm_channel):
        self.send_channel = send_channel
        self.voice_channel = voice_channel
        self.dm_channel = dm_channel
        self.meigen_list = []
        self.fmt_list = []
        self.key_list = []

    async def receive(self, message:discord.Message):
        if message.author.bot:
            return

        content = message.content


        res = random.choice(["ちんちん", "侍", "おちんちん", "ちんちん侍"])
        tin_flag = False
        
        if content == "ちんちん":
            tin_flag = True
        if content == "侍":
            tin_flag = True
            await message.channel.send("シャキーン！")
        if content == "おちんちん":
            tin_flag = True
            await message.channel.send("びろーん")
        if content == "ちんちん侍":
            tin_flag = True
            await message.channel.send("ちんちん侍！")
            
        if tin_flag:
            await message.channel.send(res)
            if res == "ちんちん侍":
                await message.channel.send("ちんちん侍！")


        if wordsInContent(["なん", "何", "ナン", "NaN"], content):
            nans = ["ナン！", "ナンですね", "ナンじゃん", "ナン！？","ん？今ナンって言ったよね？", "NaN"]
            await message.channel.send(random.choice(nans))

        if wordsInContent(["else", "クソコード", "ハードコーディング", "マジックナンバー"], content):
            await message.channel.send("ん？")

        if wordsInContent(["美少女", "天才"], content):
            await message.channel.send("呼ばれた気がした")
            
        if "おっぱい" in content:
            await message.channel.send("おっぱい！")
            
        if "おやすみ" in content:
            await message.channel.send("おやすみなさい")
            if len(self.meigen_list) < 1:
                    return

            content = random.choice(self.meigen_list)
            await message.channel.send("[ハイライト]\n"+content)
            return

        words = content.split()
        head = words[0]


        if head == "!haiku":
            if len(words) < 2:
                return

            if len(message.content) > 100:
                await message.channel.send(
                    "```"
                    " †キレた† \n"
                    "   100文字以内にしろよカス\n"
                    "```"
                )
                return

            w = words[1] + " "
            ans = w+w+w+w+w+"\n"+w+w+w+w+w+w+w+"\n"+w+w+w+w+w
            await message.channel.send(ans)
            return


        if head == "!format":
            if len(words) < 3:
                return

            if words[1] == "print":
                for fmt in self.fmt_list:
                    f_name = fmt.split()[0]
                    if f_name != words[2]:
                        continue

                    await message.channel.send(fmt[len(f_name)+1:])
                return

            if words[1] == "del":
                if len(words) < 4:
                    return

                f_s = content[len("!format del "):]
                for ind in range(len(self.fmt_list)):
                    fmt = self.fmt_list[ind]
                    if f_s != fmt:
                        continue

                    del self.fmt_list[ind]
                    async for message_h in self.dm_channel.history(limit=200):
                        if message_h.content.split()[0] != "F":
                            continue
                        
                        if f_s != message_h.content[2:]:
                            continue

                        await message_h.delete()
                        break

                    await message.channel.send("***†削除完了†***")
                    return
                return

            self.fmt_list.append(content[len(words[0])+1:])
            await message.channel.send("***†登録完了†***")
            await self.dm_channel.send("F "+self.fmt_list[-1])
            return

        
        if head == "!key":
            if len(words) < 3:
                return

            if words[1] == "print":
                for key in self.key_list:
                    key_name = key.split()[0]
                    if key_name != words[2]:
                        continue

                    await message.channel.send(key[len(key_name)+1:])
                return

            if words[1] == "del":
                if len(words) < 4:
                    return

                k_s = content[len("!key del "):]
                for ind in range(len(self.key_list)):
                    key = self.key_list[ind]
                    if k_s != key:
                        continue

                    del self.key_list[ind]
                    async for message_h in self.dm_channel.history(limit=200):
                        if message_h.content.split()[0] != "K":
                            continue
                        
                        if k_s != message_h.content[2:]:
                            continue

                        await message_h.delete()
                        break

                    await message.channel.send("***†削除完了†***")
                    return
                return

            self.key_list.append(content[len(words[0])+1:])
            await message.channel.send("***†登録完了†***")
            await self.dm_channel.send("K "+self.key_list[-1])
            return


        if head == "!meigen":
            if len(words) == 1:
                await message.channel.send(
                    "```\n"
                    "†meigen : みんなの名言（迷言）を管理† \n"
                    "   !meigen [発言者] [名言] \n"
                    "       名言追加 \n"
                    "   !meigen print [名言数=5] \n"
                    "       名言列挙 \n"
                    "   !meigen del [添字] \n"
                    "       名言削除 \n"
                    "   !meigen random\n"
                    "       ランダムで名言表示 \n"
                    "\n"
                    "†format : フォーマットを使って送信† \n"
                    "   !format [名前] [形式] \n"
                    "       フォーマット追加 \n"
                    "   !format print [名前] \n"
                    "       フォーマット表示 \n"
                    "   !format del [名前] [形式] \n"
                    "       フォーマット削除 \n"
                    "\n"
                    "†key : 単語に反応して送信† \n"
                    "   !key [キー] [内容] \n"
                    "       キーが含まれるメッセージに内容で反応 \n"
                    "   !key print [キー] \n"
                    "       key表示 \n"
                    "   !key del [キー] [内容] \n"
                    "       key削除 \n"
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
                    if not (0 < meigen_lim <= 15):
                        await message.channel.send(
                            "```"
                            " †キレた† \n"
                            "   1~15以内にしろよカス\n"
                            "```"
                        )
                        return

                text = ""
                list_len = len(self.meigen_list)
                for i in range(list_len):
                    if i >= meigen_lim:
                        break
                    text = "\n[{}]\n".format(list_len-i) + self.meigen_list[-(i+1)] + text
                
                await message.channel.send(text)
                return

            if command == "del":
                if len(words) != 3:
                    return

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
                meigen_index = int(words[2])
                #入力された整数が制約を満たしているか
                if not (0 < meigen_index <= 15):
                    await message.channel.send(
                        "```"
                        " †キレた† \n"
                        "   1~15以内にしろよカス\n"
                        "```"
                    )
                    return
                #要素があるか
                if meigen_index > len(self.meigen_list):
                    await message.channel.send(
                        "```"
                        " †キレた† \n"
                        "   要素がないよカス\n"
                        "```"
                    )
                    return

                m = self.meigen_list.pop(meigen_index-1)
                async for message_h in self.dm_channel.history(limit=200):
                    if m != message_h.content:
                        continue

                    await message_h.delete()
                    break
                text = "[削除しました]\n" + m
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
            
            if len(self.meigen_list) >= 15:
                self.meigen_list = self.meigen_list[1:]

            meigen = "```\n"+content[len(words[1])+9:].replace('`', '\'')+"\n　−−− "+words[1].replace('`', '\'')+"\n```"
            self.meigen_list.append(meigen)
            index = "[{}]\n".format(len(self.meigen_list))

            await message.channel.send(index + meigen)
            await self.dm_channel.send(meigen)

        for fmt in self.fmt_list:
            f_name = fmt.split()[0]
            if head != f_name:
                continue

            f_s = fmt[len(f_name)+1:]
            if f_s.count("{}") != len(words)-1:
                continue
            await message.channel.send(f_s.format(*words[1:]))

        for key in self.key_list:
            key_name = key.split()[0]
            if not (key_name in content):
                continue

            k_s = key[len(key_name)+1:]
            await message.channel.send(k_s)

    
            
    async def random_event(self):
        if len(self.voice_channel.members) == 0:
            return

        if len(self.meigen_list) < 1:
            return

        content = random.choice(self.meigen_list)
        await self.send_channel.send(content)