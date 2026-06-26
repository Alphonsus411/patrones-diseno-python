from abc import ABC, abstractmethod


class Burger:
    def __init__(self):
        self.bread = ""
        self.meat = ""
        self.cheese = ""
        self.dressing = ""
        self.lettuce = False
        self.tomato = False

    def display_information(self):
        print(f"Bread: {self.bread}, Meat: {self.meat},"
              f" Cheese: {self.cheese}, Dressing: {self.dressing}, "
              f"Lettuce: {self.lettuce}, Tomato: {self.tomato}")


class IBurgerBuilder(ABC):
    @abstractmethod
    def add_bread(self):
        pass

    @abstractmethod
    def add_meat(self):
        pass

    @abstractmethod
    def add_cheese(self):
        pass

    @abstractmethod
    def add_dressing(self):
        pass

    @abstractmethod
    def add_lettuce(self):
        pass

    @abstractmethod
    def add_tomato(self):
        pass

    @abstractmethod
    def get_burger(self):
        pass


class ClassicBurgerBuilder(IBurgerBuilder):
    def __init__(self):
        self.burger = Burger()

    def add_bread(self):
        self.burger.bread = "Sesame Bread"

    def add_meat(self):
        self.burger.meat = "Chicken Meat"

    def add_cheese(self):
        self.burger.cheese = "Cheddar"

    def add_dressing(self):
        self.burger.dressing = "Ketchup"

    def add_lettuce(self):
        self.burger.lettuce = True

    def add_tomato(self):
        self.burger.tomato = True

    def get_burger(self):
        return self.burger


class VeggieBurgerBuilder(IBurgerBuilder):
    def __init__(self):
        self.burger = Burger()

    def add_bread(self):
        self.burger.bread = "Whole Wheat"


    def add_meat(self):
        self.burger.meat = "Lentil patty"


    def add_cheese(self):
        self.burger.cheese = "Vegan Cheese"


    def add_dressing(self):
        self.burger.dressing = "Vegan Mayo"


    def add_lettuce(self):
        self.burger.lettuce = True


    def add_tomato(self):
        self.burger.tomato = True

    def get_burger(self):
        return self.burger


class BurgerDirector:
    def make_burger(self, burger_builder):
        burger_builder.add_bread()
        burger_builder.add_meat()
        burger_builder.add_cheese()
        burger_builder.add_dressing()
        burger_builder.add_lettuce()
        burger_builder.add_tomato()

chef = BurgerDirector()

classic_builder = ClassicBurgerBuilder()
chef.make_burger(classic_builder)
classic_burger = classic_builder.get_burger()
print("Classic Burger:")
classic_burger.display_information()

veggie_builder = VeggieBurgerBuilder()
chef.make_burger(veggie_builder)
veggie_burger = veggie_builder.get_burger()
print("Veggie Burger:")
veggie_burger.display_information()

