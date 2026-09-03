class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
        self.transactions = []
    def debit(self, amount):
        self.balance -= amount
        self.transactions.append(-amount)
        print("Rs.", amount, "debited")
    def credit(self, amount):
        self.balance += amount
        self.transactions.append(amount)
        print("Rs.", amount, "credited")
    def show_balance(self):
        print("Total Balance =", self.balance)
    def show_transactions(self):
        print("Transactions:")
        for transaction in self.transactions:
            print(transaction)
acc = Account(10000, 12345)
acc.debit(10000)
acc.credit(5000)
acc.show_balance()
acc.show_transactions()
