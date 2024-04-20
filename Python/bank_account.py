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


from BankAccount import BankAccount

def main():
    print("Welcome to BankAccount Application!")
    
    # Get account information from the user
    accNo = input("Enter the account #: ")
    accName = input("Enter the Account Name: ")
    bal = float(input("Enter your starting balance: "))
    
    # Create a BankAccount object
    account = BankAccount(accNo, accName, bal)
    
    # Deposit the user's paycheck
    paycheck = float(input("How much money would you like to deposit? "))
    account.deposit(paycheck)
    print(f"I will deposit the amount into your account. Your balance is ${account.get_balance():.2f}")
    
    # Prompt the user to enter payment for the week
    payment = float(input("How much would you like to deposit? "))
    account.deposit(payment)
    print(f"I will deposit the amount into your account. Your balance is ${account.get_balance():.2f}")
    
    # Prompt the user to enter how much they would like to withdraw
    withdraw_amount = float(input("How much would you like to withdraw? "))
    account.withdraw(withdraw_amount)
    print(f"I will withdraw the amount from your account. Your balance is ${account.get_balance():.2f}")
    
    # Display account information
    print(account)

if __name__ == "__main__":
    main()
