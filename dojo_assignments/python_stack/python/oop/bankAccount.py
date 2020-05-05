class bankAccount:
    def __init__(self, accountType, int_rate, balance):
        self.accountType = accountType
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

checking = bankAccount("checking", .5, 1000)
savings = bankAccount("savings", 2, 5000)

checking.deposit(200).withdrawal(100).deposit(500).deposit(75).display_account_info()
savings.deposit(800).withdrawal(5).withdrawal(200).withdrawal(300).withdrawal(500).deposit(600).yield_interest().display_account_info()
