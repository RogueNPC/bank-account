from random import randint

class BankAccount:
    routing_number = 123456789

    def __init__(self, full_name):
        self.account_number = randint(10000000, 99999999)
        self.balance = 0
        self.full_name = full_name

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: ${amount}")

    def withdraw(self, amount):
        print(f"Amount Withdrawn: ${amount}")
        if (self.balance < amount):
            print("Insufficient funds, you have been charged an overdraft fee of $10.")
            self.balance -= 10.00
        self.balance -= amount

    def get_balance(self):
        print(f"Hello {self.full_name}, you currently have a balance of ${round(self.balance, 2)} in your bank account.")
        return round(self.balance, 2)

    def add_interest(self):
        interest = self.balance * 0.00083
        final_interest = round(interest, 2)
        self.balance += final_interest

    def print_receipt(self):
        hidden_account = '****'
        hidden_account += str(self.account_number)[4:]
        print(f"""{self.full_name}
Account No.: {hidden_account}
Routing No.: {self.routing_number}
Balance: ${round(self.balance, 2)}""")

# Examples
print()
# BankAccount 1
jim = BankAccount("Jim Lars")
jim.deposit(230.99)
jim.withdraw(20.49)
jim.get_balance()
jim.add_interest()
jim.get_balance()
jim.print_receipt()
print()
# BankAccount 2
will = BankAccount("Will Powers")
will.deposit(50.99)
will.withdraw(10.01)
will.get_balance()
will.add_interest()
will.withdraw(40.98)
will.print_receipt()
print()
# BankAccount 3
guy = BankAccount("Guy Eldoon")
guy.deposit(20.49)
guy.withdraw(50.00)
guy.get_balance()
guy.print_receipt()