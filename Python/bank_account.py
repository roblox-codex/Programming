class BankAccount:
    def __init__(self, accNo, accName, bal):
        self.accountNumber = accNo
        self.accountName = accName
        self.balance = bal

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account#: {self.accountNumber}\nAccount Name: {self.accountName}\nAccount Balance: ${self.balance:.2f}"
