class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"Deposit successful! New balance: {self.balance}")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Error: Insufficient balance! Transaction declined.")
            return
        self.balance = self.balance - amount
        print(f"Withdrawal successful! New balance:{self.balance}")

# Instantiate Kaif's account with $100
acct = BankAccount("Kaif", 100)

# Test deposit
acct.deposit(50)

# Test successful withdraw
acct.withdraw(30)

# Test BLOCKED withdraw (Security breach!)
acct.withdraw(200)