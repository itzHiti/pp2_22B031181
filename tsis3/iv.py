class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, money):
        self.balance += money
        print(money, "was deposited on your bank account balance. Your current balance:", self.balance)
    def withdraw(self, money):
        self.balance -= money
        if self.balance < 0:
            print("Oops.. it looks like there is not enough money on your bank account to perform this operation")
        else:
            print(money, "was taken from your bank account balance. Your current balance:", self.balance)

'''
a = Account("MrBeast",69000)
a.deposit(777)
a.withdraw(357)
'''

'''
b = Account("Kanye West",500)
b.deposit(277)
b.withdraw(1337)
'''