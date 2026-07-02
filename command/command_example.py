from abc import ABC, abstractmethod


class ICommand(ABC):
    @abstractmethod
    def execute(self):
        pass


class Order:
    def place(self):
        print("Order has been placed.")

    def cancel(self):
        print("Order has been cancelled.")


class PlaceOrderCommand(ICommand):
    def __init__(self, order):
        self.order = order

    def execute(self):
        self.order.place()


class CancelOrderCommand(ICommand):
    def __init__(self, order):
        self.order = order

    def execute(self):
        self.order.cancel()


class Waiter:
    def take_command(self, command):
        command.execute()


order = Order()
place_order = PlaceOrderCommand(order)
cancel_order = CancelOrderCommand(order)

waiter = Waiter()
waiter.take_command(place_order)
waiter.take_command(cancel_order)



