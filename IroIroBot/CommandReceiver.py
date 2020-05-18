class CommandReceiver:
    PREFIX = "!"
    PREFIX_LEN = len(PREFIX)


    def __init__(self):
        self.commands = []
    
    async def receive(self, message):
        pass