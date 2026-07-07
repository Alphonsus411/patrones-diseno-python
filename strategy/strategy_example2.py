from abc import ABC, abstractmethod

class ITransportModeStrategy(ABC):
    @abstractmethod
    def go_to_work(self):
        pass


class BikeStrategy(ITransportModeStrategy):
    def go_to_work(self):
        return "Going to work by bike. It´s healthy!"


class BusStrategy(ITransportModeStrategy):
    def go_to_work(self):
        return "Going to work by bus. It´s economical and convenient."


class CarStrategy(ITransportModeStrategy):
    def go_to_work(self):
        return "Going to work by car. It´s confortable and fast."


class WalkingStrategy(ITransportModeStrategy):
    def go_to_work(self):
        return "Going to work by walking. It´s economical and healthy."


class Commute:
    def __init__(self, strategy: ITransportModeStrategy):
        self.strategy = strategy

    def set_transport_mode_strategy(self, strategy: ITransportModeStrategy):
        self.strategy = strategy

    def go_to_work(self):
        return self.strategy.go_to_work()


morningCommute = Commute(CarStrategy())
middayCommute = Commute(BusStrategy())
eveningCommute = Commute(BikeStrategy())

hour = int(input("Enter the time (in hours from 0 to 23):"))

if 7 <= hour <= 9:
    print("Morning commute with Car: ")
    print(morningCommute.go_to_work())
elif 10 <= hour <= 16:
    print("Midday commute with Bus: ")
    print(middayCommute.go_to_work())
elif 17 <= hour <= 19:
    print("Evening commute with Bike: ")
    print(eveningCommute.go_to_work())
else:
    print("Off peak hours, using Car by default: ")
    print(morningCommute.go_to_work())

