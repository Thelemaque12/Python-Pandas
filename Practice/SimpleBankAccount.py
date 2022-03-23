class Account:
    def __init__(self):
        self.balance = 0
        print("congrats account is created\n")

    def deposit(self):
        amount = float(input("enter a deposit amount: "))
        self.balance = self.balance + amount
        print("your account balance is %.2f$" % self.balance)

    def withdraw(self):
        amount = float(input("enter a amount to withdraw: "))
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("your new account balance is %.2f$ " % self.balance)
        else:
            print("Sorry Insufficient funds your account only have %.2f$" %self.balance)

acc = Account()
print(acc.deposit())
print(acc.withdraw())
