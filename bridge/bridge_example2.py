from abc import ABC, abstractmethod


class IEngine(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Vehicle(ABC):
    def __init__(self, engine: IEngine):
        self.engine = engine

    @abstractmethod
    def drive(self):
        pass


class Bus(Vehicle):
    def drive(self):
        print("Driving the bus")
        self.engine.start()

class Car(Vehicle):
    def drive(self):
        print("Driving the car")
        self.engine.start()


class ElectricEngine(IEngine):
    def start(self):
        print("Starting the electric engine")

    def stop(self):
        print("Stopping the electric engine")


class PetrolEngine(IEngine):
    def start(self):
        print("Starting the petrol engine")

    def stop(self):
        print("Stopping the petrol engine")


car_with_petrol_engine = Car(PetrolEngine())
car_with_petrol_engine.drive()

bus_with_electric_engine = Bus(ElectricEngine())
bus_with_electric_engine.drive()
