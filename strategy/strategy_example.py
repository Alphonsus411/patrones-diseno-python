from abc import ABC, abstractmethod


class IRouteStrategy(ABC):
    @abstractmethod
    def calculate_route(self, A, B):
        pass


class AvoidHighwayRouteStrategy(IRouteStrategy):
    def calculate_route(self, A, B):
        return "Route avoiding highways calculated"


class FastestRouteStrategy(IRouteStrategy):
    def calculate_route(self, A, B):
        return "Fastest route calculated"


class ShortestRouteStrategy(IRouteStrategy):
    def calculate_route(self, A, B):
        return "Shortest route calculated"


class Navigator:
    def __init__(self, strategy: IRouteStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: IRouteStrategy):
        self.strategy = strategy

    def execute_strategy(self, A, B):
        return self.strategy.calculate_route(A, B)


navigator = Navigator(ShortestRouteStrategy())
user_choice = input("Please enter your preferred route strategy(1- Shortest, 2- Fastest, 3- AvoidHighway):")

if user_choice == "1":
    navigator.set_strategy(ShortestRouteStrategy())
elif user_choice == "2":
    navigator.set_strategy(FastestRouteStrategy())
elif user_choice == "3":
    navigator.set_strategy(AvoidHighwayRouteStrategy())
else:
    print("Invalid choice. Defaulting to Shortest route strategy.")
    navigator.set_strategy(ShortestRouteStrategy())

print(navigator.execute_strategy("A", "B"))


