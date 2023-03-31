import datetime
import random


class Transaction:
    def __init__(self, w_d_type, amount, total):
        self.date = datetime.datetime.now()
        self.id = random.randint(1, 10000)
        self.type = w_d_type
        self.amount = amount
        self.total = total


#     def get_transaction(self):
#         return self.__dict__  # تعتبر خصائص وليست ميثود بالتالي بدها برنت
#
# nour_transaction = Transaction("nour", 50, 10)
# print(nour_transaction.get_transaction())


class BankAccount:

    def __init__(self, full_name, age):
        self.id = random.randint(1, 1000000)
        self.full_name = full_name
        self.age = age
        self.balance = 0
        self.transaction = []

    def add_money(self):  # or def add_money(self, amount) but you have to add as argument
        amount = float(input("Enter the amount you want deposit: "))
        if amount < 0:
            print("Invalid input")
            return  # تساوي break في الفور والوايل لوب ، أو ممكن اعمل التالي داخل else
        self.balance += amount
        transaction_obj = Transaction(w_d_type="Deposit", amount=amount, total=self.balance)
        self.transaction.append(transaction_obj)
        print(f"Your deposit is {amount}, and your account is {self.balance}")

    def withdraw(self):  # or def withdraw(self, withdrawal) but you have to withdraw as argument
        withdrawal = float(input("Enter the amount you want withdraw: "))
        if self.balance < withdrawal or withdrawal < 0:
            print("The amount is not enough")
            return
        self.balance -= withdrawal
        transaction_obj = Transaction(w_d_type="Withdraw", amount=withdrawal, total=self.balance)
        self.transaction.append(transaction_obj)
        print(f"Your withdraw is {withdrawal}, and your account is {self.balance}")

    def get_balance(self):
        print(f"Full name: {self.full_name} , Age: {self.age}, Current balance: {self.balance}")

    def get_transaction_history(self):
        print("Date\t\tID\t\t|Transaction type\t\t|Transaction amount\t\t|Total")
        for transaction in self.transaction:
            print(
                f"{transaction.date}\t\t|{transaction.id}\t\t|{transaction.type}\t\t|{transaction.amount}\t\t|{transaction.total}")


name = input("Enter full name: ")
age = input("Enter the age: ")
nour_account = BankAccount(name, age)
nour_account.add_money()
nour_account.add_money()
nour_account.add_money()
nour_account.add_money()
nour_account.withdraw()
nour_account.withdraw()
nour_account.withdraw()
nour_account.withdraw()
nour_account.get_balance()
nour_account.get_transaction_history()
