

class SimpleCofee:
    def get_cost(self):
        return 1.0

    def get_description(self):
        return "Simple cofee"


class CoffeeDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def get_cost(self):
        return self._coffee.get_cost()

    def get_description(self):
        return self._coffee.get_description()


class MilkDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def get_cost(self):
        return self._coffee.get_cost() + 0.5

    def get_description(self):
        return self._coffee.get_description() + ", milk"


class WhippedCreamDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def get_cost(self):
        return self._coffee.get_cost() + 0.7

    def get_description(self):
        return self._coffee.get_description() + ", whipped cream"

coffee = SimpleCofee()
print(f"{coffee.get_description()}: ${coffee.get_cost()}")

coffee = MilkDecorator(coffee)
print(f"{coffee.get_description()}: ${coffee.get_cost()}")

coffee = WhippedCreamDecorator(coffee)
print(f"{coffee.get_description()}: ${coffee.get_cost()}")