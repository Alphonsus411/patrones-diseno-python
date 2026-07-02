from abc import ABC, abstractmethod


class ICommand(ABC):
    @abstractmethod
    def execute(self):
        pass


class SmartTV:
    def open_amazon(self):
        print("Amazon is opened.")

    def open_netflix(self):
        print("Netflix is opened.")


class AmazonCommand(ICommand):
    def __init__(self, tv):
        self._tv = tv

    def execute(self):
        self._tv.open_amazon()


class NetflixCommand(ICommand):
    def __init__(self, tv):
        self._tv = tv

    def execute(self):
        self._tv.open_netflix()


class RemoteControl:
    def set_command(self, command):
        self._command = command

    def press_button(self):
        self._command.execute()


tv = SmartTV()
remote = RemoteControl()

remote.set_command(AmazonCommand(tv))
remote.press_button()

remote.set_command(NetflixCommand(tv))
remote.press_button()
