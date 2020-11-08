from random import randint

class BankAccount:
    account_number = randint(10000000, 99999999)
    routing_number = 123456789
    balance = 0

    def __init__(self, full_name):
        self.full_name = full_name

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: ${amount}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Amount Withdrawn: ${amount}")
        if (self.balance < amount):
            print("Insufficient funds, you have been charged an overdraft fee of $10.")
            self.balance -= 10.00

    def get_balance(self):
        print(f"Hello {self.full_name}, you currently have a balance of ${self.balance} in your bank account.")
        return self.balance

first = BankAccount("Jim Lars")
# print(first.__dict__)
first.withdraw(20.49)
# print(first.balance)
first.deposit(230.99)
# print(first.balance)
first.withdraw(20.49)
# print(first.balance)
first.get_balance()