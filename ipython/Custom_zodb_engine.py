import persistent

class OutOfFounds(Exception):
    pass
class Account(persistent.Persistent):
    def __init__(self, name, starting_balance=4):
        self.name = name
        self.balance = starting_balance

    def __str__(self):
        return f"Account {self.name} balance {self.balance}"

    def __repr__(self):
        return f"Account {self.name}, Balance {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self. balance:
            raise  OutOfFounds

        self.balance -= amount
        return self.balance





