class Game:
    __is_running: bool

    def is_running(self) -> bool:
        return self.__is_running

    def run(self):
        self.__is_running = self._init()

        while self.__is_running:
            self._loop()

    def quit(self):
        self.__is_running = False

    def _loop(self):
        pass

    def _init(self) -> bool:
        return True
