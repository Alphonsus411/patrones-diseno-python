

class EmptyState:
    def select_product(self, product):
        print("The vending machine is empty. Please restock")

    def insert_payment(self, amount):
        print("The vending machine is empty. No payment can be processed")

    def dispense_product(self):
        print("The vending machine is empty. Please restock")


class DispensingProductState:
    def select_product(self, product):
        print("Please wait! Dispensing in progress...")

    def insert_payment(self, amount):
        print("Please wait! Dispensing in progress...")

    def dispense_product(self):
        print("Dispensing in progress...")


class WaitingForPaymentState:
    def select_product(self, product):
        print(f"Product '{product}' has already been selected, waiting for payment.")

    def insert_payment(self, amount):
        print(f"Inserted payment of '{amount}'.")

    def dispense_product(self):
        print("Please insert payment first.")


class WaitingForProductSelectionState:
    def select_product(self, product):
        print(f"Product '{product}' has been selected.")

    def insert_payment(self, amount):
        print("Please select a product first.")

    def dispense_product(self):
        print("Please select a product first.")


class VendingMachine:
    def __init__(self):
        self.state = WaitingForProductSelectionState()

    def set_state(self, state):
        self.state = state

    def select_product(self, product):
        self.state.select_product(product)

    def insert_payment(self, amount):
        self.state.insert_payment(amount)

    def dispense_product(self):
        self.state.dispense_product()


vending_machine = VendingMachine()
vending_machine.select_product("Candy")
vending_machine.set_state(WaitingForPaymentState())

vending_machine.insert_payment(50)
vending_machine.set_state(DispensingProductState())

vending_machine.dispense_product()
vending_machine.set_state(EmptyState())

vending_machine.select_product("Coke")

