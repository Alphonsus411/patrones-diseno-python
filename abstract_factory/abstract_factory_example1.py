from abc import ABC, abstractmethod


class IButton(ABC):
    @abstractmethod
    def render(self):
        pass


class IDropDown(ABC):
    @abstractmethod
    def render(self):
        pass


class ITextBox(ABC):
    @abstractmethod
    def render(self):
        pass


class IThemeFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_drop_down(self):
        pass

    @abstractmethod
    def create_text_box(self):
        pass


class LinuxButton(IButton):
    def render(self):
        print("Rendering Linux Button")


class LinuxDropDown(IDropDown):
    def render(self):
        print("Rendering Linux DropDown")


class LinuxTextBox(ITextBox):
    def render(self):
        print("Rendering Linux TextBox")


class LinuxFactory(IThemeFactory):
    def create_button(self):
        return LinuxButton()

    def create_drop_down(self):
        return LinuxDropDown()

    def create_text_box(self):
        return LinuxTextBox()


class MacButton(IButton):
    def render(self):
        print("Rendering Mac Button")


class MacDropDown(IDropDown):
    def render(self):
        print("Rendering Mac DropDown")


class MacTextBox(ITextBox):
    def render(self):
        print("Rendering Mac TextBox")


class MacFactory(IThemeFactory):
    def create_button(self):
        return MacButton()

    def create_drop_down(self):
        return MacDropDown()

    def create_text_box(self):
        return MacTextBox()


class WindowsButton(IButton):
    def render(self):
        print("Rendering Windows Button")


class WindowsDropDown(IDropDown):
    def render(self):
        print("Rendering Windows DropDown")


class WindowsTextBox(ITextBox):
    def render(self):
        print("Rendering Windows TextBox")


class WindowsFactory(IThemeFactory):
    def create_button(self):
        return WindowsButton()

    def create_drop_down(self):
        return WindowsDropDown()

    def create_text_box(self):
        return WindowsTextBox()


linux_factory = LinuxFactory()
linux_button = linux_factory.create_button()
linux_button.render()

win_factory = WindowsFactory()
win_button = win_factory.create_button()
win_button.render()

mac_factory = MacFactory()
mac_button = mac_factory.create_button()
mac_button.render()