class User:
    def __init__(self, name, email_address):
        self.Name = name
        self.Email = email_address
        self.Balance = 0

    def makeDeposit(self, amount):
        self.Balance += amount
        return self

    def makeWithdrawal(self, amount):
        self.Balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.Name}, Balance: {self.Balance}")
        return self

    def transfer_money(self, recipient, amount):
        print(recipient.Name)
        recipient.Balance += amount
        self.Balance -= amount
        print(f"{recipient.Name} now has: ${recipient.Balance}")
        print(f"{self.Name} now has: ${self.Balance}")
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "mondy@python.com")

justin = User("Justin Smith", "justins@mybank.com")
laura = User("Laura Pierczynski", "laurap@mybank.com")
mallory = User("Mallory Adiego", "mallorya@mybank.com")

mallory.makeDeposit(200)
mallory.makeDeposit(100)
mallory.makeDeposit(200)
mallory.makeWithdrawal (100)

mallory.display_user_balance()


laura.makeDeposit(300)
laura.makeDeposit(500)
laura.makeWithdrawal(35)
laura.makeWithdrawal(65)

laura.display_user_balance()

justin.transfer_money(laura, 20)

justin.makeDeposit(30).makeDeposit(50).display_user_balance()

laura.makeDeposit(20)