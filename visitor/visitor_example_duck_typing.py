

class Lion:
    def accept(self, operation):
        operation.visit_lion(self)


class Monkey:
    def accept(self, operation):
        operation.visit_monkey(self)


class Feed:
    def visit_lion(self, lion):
        print("The lion has been fed.")

    def visit_monkey(self, monkey):
        print("The monkey has been fed.")


class MedicalCheck:
    def visit_lion(self, lion):
        print("The lion has been checked.")

    def visit_monkey(self, monkey):
        print("The monkey has been checked.")


animals = [Lion(), Monkey()]
operations = [Feed(), MedicalCheck()]

for animal in animals:
    for operation in operations:
        animal.accept(operation)
