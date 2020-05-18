class MeigenHolder:
    LEN_LIMIT = 50
    HOLD_LIMIT = 30
    ID_OPTION = "id"
    FORMAT = \
        "```\
        {text}\n\
            --- {name}\
        ```"

    meigen_list = []


    def prepend(self, meigen: str):
        MeigenHolder.meigen_list.insert(0, meigen)

    def append(self, name: str, text: str):
        MeigenHolder.meigen_list.append(
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
            meigen_number  = len(MeigenHolder.meigen_list) - i
            if meigen_number == 0:
                break

            text += f"[{meigen_number}]\n\
                {MeigenHolder.meigen_list[meigen_number-1]}\n"

        return text