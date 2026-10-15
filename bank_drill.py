from abc import ABC,abstractmethod

class Account(ABC):

    bank_name: str = "BRAC Bank"

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    @abstractmethod
    def withdraw(self, amount: float) -> float:
        pass

class SavingAccount(Account):

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

class CheckingAccount(Account):

    def __init__(self,owner: str, balance: float, fee: float):
        super().__init__(owner,balance)
        self.fee = fee

    def withdraw(self, amount):
        self.balance = (self.balance - amount - self.fee)
        return self.balance

savingaccount = SavingAccount("Prappo", 50000)
savingaccount.withdraw(20000)
print(savingaccount.balance)
checkingaccount = CheckingAccount("Sakib", 12000, 1500)
checkingaccount.withdraw(5000)
print(checkingaccount.balance)