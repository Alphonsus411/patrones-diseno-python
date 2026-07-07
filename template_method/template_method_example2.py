from abc import ABC, abstractmethod


class PastaDish(ABC):
    def cook_pasta_dish(self):
        self.boil_water()
        self.add_pasta()
        self.drain()
        self.add_sauce()
        self.add_protein()
        self.add_cheese()


    def boil_water(self):
        print("Boiling water")

    def add_pasta(self):
        print("Add pasta")

    def drain(self):
        print("Draining water")

    @abstractmethod
    def add_sauce(self):
        pass

    @abstractmethod
    def add_protein(self):
        pass

    @abstractmethod
    def add_cheese(self):
        pass


class RavioliAlfredo(PastaDish):
    def add_sauce(self):
        print("Adding alfredo sauce")

    def add_protein(self):
        print("Adding chicken")

    def add_cheese(self):
        print("Adding parmesan cheese")


class SpaghettiCarbonara(PastaDish):
    def add_sauce(self):
        print("Adding carbonara sauce")

    def add_protein(self):
        print("Adding pancetta")

    def add_cheese(self):
        print("Adding pecorino cheese")

carbonara = SpaghettiCarbonara()
carbonara.cook_pasta_dish()

alfredo = RavioliAlfredo()
alfredo.cook_pasta_dish()