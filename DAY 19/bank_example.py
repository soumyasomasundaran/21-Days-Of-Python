class Account:
    def __init__(self, account_number, account_balance):
        self.account_number = account_number
        self.account_balance = account_balance

    def withdraw(self, amount):
        if self.account_balance - amount > 0:
            self.account_balance = self.account_balance - amount
        else:
            print("Withdrawal Failed")

    def display(self):
        print("Your account balance is {}".format(self.account_balance))


account_one = Account('A1234', 5000)
account_two = Account('B4567', 900)
amount = int(input("Enter the amount to withdraw from account_two"))
account_two.withdraw(amount)
account_two.display()
