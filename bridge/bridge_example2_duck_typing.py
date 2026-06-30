

class Vehicle:
    def __init__(self, engine):
        self.engine = engine

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


class ElectricEngine:
    def start(self):
        print("Starting the electric engine")

    def stop(self):
        print("Stopping the electric engine")


class PetrolEngine:
    def start(self):
        print("Starting the petrol engine")

    def stop(self):
        print("Stopping the petrol engine")


car_with_petrol_engine = Car(PetrolEngine())
car_with_petrol_engine.drive()

bus_with_electric_engine = Bus(ElectricEngine())
bus_with_electric_engine.drive()
