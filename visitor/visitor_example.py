from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def accept(self, operation):
        pass


class AnimalOperation(ABC):
    @abstractmethod
    def visit_lion(self, lion):
        pass

    @abstractmethod
    def visit_monkey(self, dog):
        pass


class Lion(Animal):
    def accept(self, operation):
        operation.visit_lion(self)


class Monkey(Animal):
    def accept(self, operation):
        operation.visit_monkey(self)


class Feed(AnimalOperation):
    def visit_lion(self, lion):
        print("The lion has been fed.")

    def visit_monkey(self, monkey):
        print("The monkey has been fed.")


class MedicalCheck(AnimalOperation):
    def visit_lion(self, lion):
        print("The lion has been checked.")

    def visit_monkey(self, monkey):
        print("The monkey has been checked.")


animals = [Lion(), Monkey()]
operations = [Feed(), MedicalCheck()]

for animal in animals:
    for operation in operations:
        animal.accept(operation)




