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


first = BankAccount("Jim Lars")
# print(first.__dict__)
first.deposit(230.99)