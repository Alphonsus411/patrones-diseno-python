

class InventorySystem:
    def __init__(self, mediator=None):
        self.mediator = mediator

    def set_mediator(self, mediator):
        self.mediator = mediator

    def check_item_availability(self, item):
        print(f"Checking how many {item} are available...")


class ShoppingCart:
    def __init__(self, mediator=None):
        self.mediator = mediator

    def set_mediator(self, mediator):
        self.mediator = mediator

    def add_item(self, item):
        print(f"Adding {item} to the shopping cart...")
        self.mediator.notify(self, item)


class EcommercePlatform:
    def __init__(self, shopping_cart, inventory_system):
        self.shopping_cart = shopping_cart
        self.inventory_system = inventory_system

    def notify(self, sender, event_code):
        if isinstance(sender, ShoppingCart):
            self.inventory_system.check_item_availability(event_code)


inventory_system = InventorySystem()
shopping_cart = ShoppingCart()

ecommerce_platform = EcommercePlatform(shopping_cart, inventory_system)

inventory_system.set_mediator(ecommerce_platform)
shopping_cart.set_mediator(ecommerce_platform)

shopping_cart.add_item("Apple")
shopping_cart.add_item("Banana")
shopping_cart.add_item("Orange")
