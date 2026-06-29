

class Bike:
    def drive(self):
        print("Riding the bike.")

    def start(self):
        print("Starting the bike.")

    def stop(self):
        print("Stopping the bike.")


class Car:
    def drive(self):
        print("Driving the car.")

    def start(self):
        print("Starting the car.")

    def stop(self):
        print("Stopping the car.")


class Motorcycle:
    def drive(self):
        print("Driving the motorcycle.")

    def start(self):
        print("Starting the motorcycle.")

    def stop(self):
        print("Stopping the motorcycle.")


class BikeFactory:
    def create_vehicle(self):
        return Bike()

    def order_vehicle(self):
        vehicle = self.create_vehicle()
        vehicle.start()
        vehicle.stop()
        vehicle.drive()

        return vehicle

class CarFactory:
    def create_vehicle(self):
        return Car()

    def order_vehicle(self):
        vehicle = self.create_vehicle()
        vehicle.start()
        vehicle.stop()
        vehicle.drive()

        return vehicle

class MotorcycleFactory:
    def create_vehicle(self):
        return Motorcycle()

    def order_vehicle(self):
        vehicle = self.create_vehicle()
        vehicle.start()
        vehicle.stop()
        vehicle.drive()

        return vehicle


vehicle_factory = BikeFactory()
vehicle = vehicle_factory.create_vehicle()
print(f"You have used a {vehicle.__class__.__name__}.")

vehicle_factory = CarFactory()
vehicle = vehicle_factory.create_vehicle()
print(f"You have used a {vehicle.__class__.__name__}.")

vehicle_factory = MotorcycleFactory()
vehicle = vehicle_factory.create_vehicle()
print(f"You have used a {vehicle.__class__.__name__}.")