class bankAccount:
    def __init__(self, int_rate, balance, accountType):
        self.interestRate = int_rate
        self.balance = balance
        self.type = accountType

    def deposit(self, amount, type):
        self.balance += amount
        print(f"{amount} has been deposited into your {type} account.")
        return self
    
    def withdrawal(self, amount, type):
        if amount > self.balance:
            print("Insufficient funds {type}: Charging a $5 fee.")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    
    def display_account_info(self, type):
        print(f"Account: {type}, Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.interestRate
        return self

class User:
    def __init__(self, name, email_address, accountType):
        self.Name = name
        self.Email = email_address
        self.Account = bankAccount(int_rate=0.02, balance=0, accountType="checking")

    def makeDeposit(self, amount, accountType):
        self.Account.deposit(amount, accountType)
        return self

    def makeWithdrawal(self, amount, accountType):
        self.Account.withdrawal(amount, accountType)
        return self
    
    def display_user_balance(self, accountType):
        self.Account.display_account_info(accountType)
        # print(f"User: {self.Name}, Balance: {self.Account.balance}")
        return self

    def transfer_money(self, recipient, amount):
        print(recipient.Name)
        recipient.Account.balance += amount
        self.Account.balance -= amount
        print(f"{recipient.Name} now has: ${recipient.Account.balance}")
        print(f"{self.Name} now has: ${self.Account.balance}")
        return self

# guido = User("Guido van Rossum", "guido@python.com")
# monty = User("Monty Python", "mondy@python.com")

# justin = User("Justin Smith", "justins@mybank.com")
# laura = User("Laura Pierczynski", "laurap@mybank.com")
# mallory = User("Mallory Adiego", "mallorya@mybank.com")
my = User("My Truong", "my@mybank.com", "checking")


# justin.transfer_money(laura, 15)

my.makeDeposit(15, "checking")