
from abc import ABC, abstractmethod

class Account(ABC):

    @abstractmethod
    def checkBalance(self):
        pass

class Savings(Account):

    def deposit(self, amt):
        print(f"{amt} credited into the account.....")

    def checkBalance(self):
        print("balance in the account is ######.##")


sav = Savings()
sav.deposit(250000)
sav.checkBalance()

