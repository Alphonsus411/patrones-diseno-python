from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ProductVisitor(ABC):
    @abstractmethod
    def visit_tv(self, tv):
        pass

    @abstractmethod
    def visit_phone(self, phone):
        pass

    @abstractmethod
    def visit_computer(self, computer):
        pass

class Computer(Product):
    def accept(self, visitor):
        visitor.visit_computer(self)

class Phone(Product):
    def accept(self, visitor):
        visitor.visit_phone(self)

class TV(Product):
    def accept(self, visitor):
        visitor.visit_tv(self)


class RepairService(ProductVisitor):
    def visit_tv(self, tv):
        print("Repairing a TV.")

    def visit_phone(self, phone):
        print("Repairing a Phone.")

    def visit_computer(self, computer):
        print("Repairing a Computer.")


tv = TV()
phone = Phone()
computer = Computer()
repair_service = RepairService()

tv.accept(repair_service)
phone.accept(repair_service)
computer.accept(repair_service)

