from dataclasses import dataclass


@dataclass
class Bankroll:
    _balance: int = 0

    def __init__(self, balance: int = 0):
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount: int):
        self._balance = amount

    def cash_in(self, amount: int):
        if amount <= 0:
            raise ValueError("Cash-in amount must be positive or non-zero")
        self.balance += amount

    def cash_out(self, amount: int):
        if amount <= 0:
            raise ValueError("Cash-out amount must be positive or non-zero")

        if amount > self.balance:
            raise ValueError("Cash-out amount must smaller than balance")

        self.balance -= amount
