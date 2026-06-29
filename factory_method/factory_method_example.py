from abc import ABC, abstractmethod


class IVehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass


class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass

    def order_vehicle(self):
        vehicle = self.create_vehicle()
        vehicle.start()
        vehicle.stop()
        vehicle.drive()

        return vehicle


class Bike(IVehicle):
    def drive(self):
        print("Riding the bike.")

    def start(self):
        print("Starting the bike.")

    def stop(self):
        print("Stopping the bike.")


class Car(IVehicle):
    def drive(self):
        print("Driving the car.")

    def start(self):
        print("Starting the car.")

    def stop(self):
        print("Stopping the car.")


class Motorcycle(IVehicle):
    def drive(self):
        print("Driving the motorcycle.")

    def start(self):
        print("Starting the motorcycle.")

    def stop(self):
        print("Stopping the motorcycle.")


class BikeFactory(VehicleFactory):
    def create_vehicle(self):
        return Bike()

class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()

class MotorcycleFactory(VehicleFactory):
    def create_vehicle(self):
        return Motorcycle()


vehicle_factory = BikeFactory()
vehicle = vehicle_factory.create_vehicle()
print(f"You have used a {vehicle.__class__.__name__}.")

vehicle_factory = CarFactory()
vehicle = vehicle_factory.create_vehicle()
print(f"You have used a {vehicle.__class__.__name__}.")

vehicle_factory = MotorcycleFactory()
vehicle = vehicle_factory.create_vehicle()
print(f"You have used a {vehicle.__class__.__name__}.")