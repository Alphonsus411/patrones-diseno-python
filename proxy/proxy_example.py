from abc import ABC, abstractmethod


class IBankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self, amount):
        pass


class BankAccount(IBankAccount):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def get_balance(self, amount):
        return self.balance


class BankAccountProxy(IBankAccount):
    def __init__(self, bank_account):
        self._bank_account = bank_account

    def deposit(self, amount):
        self._bank_account.deposit(amount)

    def get_balance(self):
        return self._bank_account.get_balance()

    def withdraw(self, amount):
        if amount > 10000:
            print("You need manager approval for withdrawals over 10000")
            return False
        else:
            self._bank_account.withdraw(amount)


my_account = BankAccount(15000)
my_account_proxy = BankAccountProxy(my_account)

result = my_account_proxy.withdraw(500)

if result:
    print(f"Withdraw successful. Balance is now: {my_account_proxy.get_balance()}")
else:
    print("Withdraw failed.")

result = my_account_proxy.withdraw(12000)

if result:
    print(f"Withdraw successful. Balance: {my_account_proxy.get_balance()}")
else:
    print("Withdraw failed.")
    



