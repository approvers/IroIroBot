class Singleton(object):
    def _set_up(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
            cls._instance._set_up()

        return cls._instance