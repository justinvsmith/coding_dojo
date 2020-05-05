class bankAccount:
    def __init__(self, int_rate, balance):
        self.interestRate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.interestRate
        return self

class User:
    def __init__(self, name, email_address):
        self.Name = name
        self.Email = email_address
        self.Account = bankAccount(int_rate=0.02, balance=0)

    def makeDeposit(self, amount):
        self.Account.balance += amount
        return self

    def makeWithdrawal(self, amount):
        self.Account.balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.Name}, Balance: {self.Account.balance}")
        return self

    def transfer_money(self, recipient, amount):
        print(recipient.Name)
        recipient.account.balance += amount
        self.Account.balance -= amount
        print(f"{recipient.Name} now has: ${recipient.Account.balance}")
        print(f"{self.Name} now has: ${self.Account.balance}")
        return self