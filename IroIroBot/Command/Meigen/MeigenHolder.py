from IroIroBot.Singleton import Singleton



class MeigenHolder(Singleton):
    LEN_LIMIT = 50
    HOLD_LIMIT = 30
    ID_OPTION = "id"
    FORMAT = \
        "```\
        {text}\n\
            --- {name}\
        ```"


    def __init__(self):
        self.meigen_list = []

    def prepend(self, meigen: str):
        self.meigen_list.insert(0, meigen)

    def append(self, name: str, text: str):
        self.meigen_list.append(
            MeigenHolder.FORMAT.format(
                name=name, text=text
            )
        )

    def print(self, number: int) -> str:
        if 0 >= number > MeigenHolder.HOLD_LIMIT:
            return \
                "```\
                †キレた†\n\
                1~{MeigenHolder.HOLD_LIMIT}以内にしろよカス\n\
                ```"

        text = ""
        for i in range(number):
            meigen_number  = len(self.meigen_list) - i
            if meigen_number == 0:
                break

            text += f"[{meigen_number}]\n\
                {self.meigen_list[meigen_number-1]}\n"

        return text

    def delete(self, index: int) -> str:
        pass