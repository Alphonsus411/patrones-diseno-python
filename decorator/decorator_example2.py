from abc import ABC, abstractmethod


class IBurger(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


class BasicBurger(IBurger):
    def get_cost(self):
        return 3.0

    def get_description(self):
        return "Basic Burger"


class BurgerDecorator(IBurger):
    def __init__(self, burger):
        self._burger = burger

    def get_cost(self):
        return self._burger.get_cost()

    def get_description(self):
        return self._burger.get_description()


class CheeseDecorator(BurgerDecorator):
    def __init__(self, burger):
        super().__init__(burger)
        self._burger = burger

    def get_cost(self):
        return self._burger.get_cost() + 0.5

    def get_description(self):
        return self._burger.get_description() + ", cheese"


class BaconDecorator(BurgerDecorator):
    def __init__(self, burger):
        super().__init__(burger)
        self._burger = burger

    def get_cost(self):
        return self._burger.get_cost() + 1.0

    def get_description(self):
        return self._burger.get_description() + ", bacon"


burger = BasicBurger()
print(f"{burger.get_description()}: ${burger.get_cost()}")

burger = CheeseDecorator(burger)
print(f"{burger.get_description()}: ${burger.get_cost()}")

burger = BaconDecorator(burger)
print(f"{burger.get_description()}: ${burger.get_cost()}")


