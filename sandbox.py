from app.schemas import Exercise


def adding(num1:int, num2:int)->int:
    return num1 + num2

def subtracting(num1:int, num2:int)->int:
    return num1 - num2

def dividing(num1:int, num2:int)->float:
    return num1 / num2

def multiplying(num1:int, num2:int)->int:
    return num1 * num2

class InsufficientFunds(Exception):
    pass


class BankAcc():
    def __init__(self, starting_balance=0):
        self.balance = starting_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds("Insufficient money")
        self.balance -= amount

    def collect_interest(self):
        self.balance *= 1.1