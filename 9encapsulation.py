# import datetime
# import random
#
#
# class Transaction:
#     def __init__(self, w_d_type, amount, total):
#         self.date = datetime.datetime.now()
#         self.id = random.randint(1, 10000)
#         self.type = w_d_type
#         self.amount = amount
#         self.total = total
#
#
# #     def get_transaction(self):
# #         return self.__dict__  # تعتبر خصائص وليست ميثود بالتالي بدها برنت
# #
# # nour_transaction = Transaction("nour", 50, 10)
# # print(nour_transaction.get_transaction())
#
#
# class BankAccount:
#
#     def __init__(self, full_name, age):
#         self.id = random.randint(1, 1000000)
#         self.full_name = full_name
#         self.age = age
#         self.__balance = 0  # encapsulation طريقة الإخفاء بحيث ما نظهر بعد الدوت للمستخدم أي منعه من التعديل على الكونستراكتور
#         self.transaction = []
#
#     def add_money(self):  # or def add_money(self, amount) but you have to add as argument
#         amount = float(input("Enter the amount you want deposit: "))
#         if amount < 0:
#             print("Invalid input")
#             return  # تساوي break في الفور والوايل لوب ، أو ممكن اعمل التالي داخل else
#         self.__balance += amount
#         transaction_obj = Transaction(w_d_type="Deposit", amount=amount, total=self.__balance)
#         self.transaction.append(transaction_obj)
#         print(f"Your deposit is {amount}, and your account is {self.__balance}")
#
#     def withdraw(self):  # or def withdraw(self, withdrawal) but you have to withdraw as argument
#         withdrawal = float(input("Enter the amount you want withdraw: "))
#         if self.__balance < withdrawal or withdrawal < 0:
#             print("The amount is not enough")
#             return
#         self.__balance -= withdrawal
#         transaction_obj = Transaction(w_d_type="Withdraw", amount=withdrawal, total=self.__balance)
#         self.transaction.append(transaction_obj)
#         print(f"Your withdraw is {withdrawal}, and your account is {self.__balance}")
#
#     def get_balance(self):
#         print(f"Full name: {self.full_name} , Age: {self.age}, Current balance: {self.__balance}")
#
#     def get_transaction_history(self):
#         print("Date\t\tID\t\t|Transaction type\t\t|Transaction amount\t\t|Total")
#         for transaction in self.transaction:
#             print(
#                 f"{transaction.date}\t\t|{transaction.id}\t\t|{transaction.type}\t\t|{transaction.amount}\t\t|{transaction.total}")
#
#     def get_current_balance(
#             self):  # encapsulation في حال أردت أطهاره واستخدامه لاحقا يجب أن اعرفه كصفة حتى ارجع استخدمه بهذه الطريقة
#         return self.__balance
#
#
# name = input("Enter full name: ")
# age = input("Enter the age: ")
# nour_account = BankAccount(name, age)
# nour_account.add_money()
# nour_account.add_money()
# nour_account.add_money()
# nour_account.add_money()
# nour_account.withdraw()
# nour_account.withdraw()
# nour_account.withdraw()
# nour_account.withdraw()
# nour_account.get_balance()
# nour_account.get_transaction_history()
# nour_account.get_current_balance()  # encapsulation في هذه الحالة لن يظهر نتيجة لأنه ما أسندته لأي متغير
# balance = nour_account.get_current_balance()  # encapsulation وبهيك بكون أسندته لمتغير ويمكنني إظهاره
# print(balance)

# ---------------------------------------------------------------------
# encapsulation

# class Personal_data1:
#     def __init__(self, full_name, age, mobile_number="none"):
#         self.full_name = full_name
#         self.age = age
#         self.mobile_number = mobile_number
#
# nour = Personal_data1("nour", 19)
# print(nour.full_name)
# print(nour.mobile_number)
# nour.mobile_number = "0599053751"
# print(nour.mobile_number)

# class Personal_data2:
#     def __init__(self, full_name, age, mobile_number="none"):
#         self.full_name = full_name
#         self.age = age
#         self.__mobile_number = mobile_number
#
#     def get_show_data(self):
#         return self.__dict__
#
#
# nour = Personal_data2("nour", 19, "059905371")
# print(nour.full_name)
# # print(nour.mobile_number) # does not work because the property is hidden
# nour.mobile_number = "05990537511" # this is work as adding a new argument no editing
# print(nour.get_show_data()) # get needs print but set do not


class Personal_data3:
    def __init__(self, full_name, age, mobile_number="none"):
        self.full_name = full_name
        self.age = age
        self.__mobile_number = mobile_number

    def set_new_mobile_data(self, mobile_number):
        self.__mobile_number = mobile_number

    def get_show_data(self):
        return self.__dict__


nour = Personal_data3("nour", 19, "059905371")
print(nour.get_show_data())
nour.set_new_mobile_data("01111110")  # get needs print but set do not
print(nour.get_show_data())  # get needs print but set do not

# encapsulationمفهومة بشكل بسط هو الاكسس موديفاير بده يكون برايفت
# لو بدي اعدل عليه بدي ست
# لو بدي اظهره بدي قيت
# الأمر برمته للمبرمجين ولا يخرج للمستخدمين
# الموضوع باختصار وضع وسطاء لتغيير وعرض البيانات للديفيلوبر
