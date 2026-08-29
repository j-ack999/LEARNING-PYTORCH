class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __str__(self):
        return (f"Balance = {self.balance}")

class SavingsAccount(BankAccount):

    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate


    def add_interest(self):
        self.deposit(self.balance * self.interest_rate)



bank = BankAccount(1000)

bank.deposit(10)

print(bank)

savings = SavingsAccount(1000, 3.5) # balance is 1000 with an interest rate of 3.5 

savings.add_interest()
print(savings)
    
