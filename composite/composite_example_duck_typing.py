

class AppFile:
    def __init__(self, name):
        self._name = name

    def display(self, indent = ""):
        print(f"{indent}- {self.__class__.__name__}: {self._name}")


class Folder:
    def __init__(self, name):
        self._name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display(self, indent = ""):
        print(f"{indent}- {self.__class__.__name__}: {self._name}")
        for item in self.items:
            item.display(indent + "  ")


file1 = AppFile("File1")
file2 = AppFile("File2")
file3 = AppFile("File3")

folder1 = Folder("Folder1")
folder1.add_item(file1)

folder2 = Folder("Folder2")
folder2.add_item(file2)
folder2.add_item(file3)

root = Folder("Root")
root.add_item(folder1)
root.add_item(folder2)

root.display()