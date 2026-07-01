

class Employee:
    def __init__(self, name):
        self._name = name

    def display(self, indent):
        print('-' * indent + self._name)


class Manager:
    def __init__(self, name):
        self._name = name
        self._employees = []

    def add(self, employee):
        self._employees.append(employee)

    def display(self, indent):
        print('-' * indent + self._name)
        for employee in self._employees:
            employee.display(indent + 2)


john = Employee('Jhon Doe')
jane = Employee('Jane Doe')

bob = Manager('Bob Smith')
bob.add(jane)
bob.add(john)

tom = Employee('Tom Johnson')
susan = Manager('Susan Thompson')
susan.add(tom)
susan.add(bob)

susan.display(1)