

class IButton:
    def render(self):
        pass


class IDropDown:
    def render(self):
        pass


class ITextBox:
    def render(self):
        pass


class IThemeFactory:
    def create_button(self):
        pass

    def create_drop_down(self):
        pass

    def create_text_box(self):
        pass


class LinuxButton:
    def render(self):
        print("Rendering Linux Button")


class LinuxDropDown:
    def render(self):
        print("Rendering Linux DropDown")


class LinuxTextBox:
    def render(self):
        print("Rendering Linux TextBox")


class LinuxFactory:
    def create_button(self):
        return LinuxButton()

    def create_drop_down(self):
        return LinuxDropDown()

    def create_text_box(self):
        return LinuxTextBox()


class MacButton:
    def render(self):
        print("Rendering Mac Button")


class MacDropDown:
    def render(self):
        print("Rendering Mac DropDown")


class MacTextBox:
    def render(self):
        print("Rendering Mac TextBox")


class MacFactory:
    def create_button(self):
        return MacButton()

    def create_drop_down(self):
        return MacDropDown()

    def create_text_box(self):
        return MacTextBox()


class WindowsButton:
    def render(self):
        print("Rendering Windows Button")


class WindowsDropDown:
    def render(self):
        print("Rendering Windows DropDown")


class WindowsTextBox:
    def render(self):
        print("Rendering Windows TextBox")


class WindowsFactory:
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