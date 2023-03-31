# # Best practices = 4 spaces or 1 tab (That is called by indentation)
# x = 4
# if x > 3;
#     Print('True')
from unittest import result


# # variables and data types
# c,v,b = 1,2,3
# print(c+v)
# xx = 2
# yy = 2.3
# zz = [1,2,3]
# tt = True
# ii = 'NOUR'
# print(type(xx))
# print(type(yy))
# print(type(zz))
# print(type(tt))
# print(type(ii))

# # case sensitive
# name = 'nour'
# Name = 'zain'
# print(name)
# print(name == Name)

# # data operations
# xx = 2
# yy = 2.3
# zz = [1,2,3]
# tt = True
# ii = 'NOUR'
# print(xx+yy)
# print(xx+tt)
# print(str(xx)+ii)
# print(type(xx+yy))
# print(type(xx+tt))
# print(type(str(xx)+ii))

# # Exercise 1
# first_name = input('Enter your first name')
# surname = input('Enter your surname')
# id = input('Enter your id')
# age = input('Enter your age')
# nationality = input('Enter your nationality')
# print('Personal information',first_name+surname,id,age,nationality)

# # String data type
# # you can write your output text by two ways
# my_name1 = 'nour alhammami'
# my_name2 = 'nour  \nalhammami'
# my_name3 = 'nour \talhammami'
# my_name4 = '''nour
# alhammami'''
# my_name5 = '''nour      alhammami'''
# print(my_name1)
# print(my_name2)
# print(my_name3)
# print(my_name4)
# print(my_name5)

# # Dynamic string
# first_name = input('Enter your first name')
# surname = input('Enter your surname')
# credit_number = input('Enter your CN')
# password = input('Enter your PW')
# email_text = f"Hello, your name is {first_name+surname} your credit number is {credit_number} and your password is {password+credit_number}"
# print(email_text)
# email_text = f"Hello, your name is {first_name,surname} your credit number is {credit_number} and your password is {password+credit_number}"
# print(email_text)

# # slicing
# my_name = 'Nour Alhammami'
# # The indexes are [0,1,2,3,4,5,6,7,8,9,11,12,13]
# print(len(my_name))
# print(my_name.find("i"))
# N= print(my_name[0])
# o= print(my_name[1])
# i= print(my_name[-1])
# i= print(my_name[len(my_name)-1]) # -1 to skip first digit = 0
# Nou= print(my_name[0:3])
# Nou= print(my_name[:3])
# ou= print(my_name[1:3])
# mmam= print(my_name[-5:-1])
# mmami= print(my_name[-5:])
# Nour Alha= print(my_name[:-5])
# # string type is immutable, while the list is mutable

# # Copy inside copy
# name = 'zain'
# copy_name1 = name # Copy by reference (the register is assigned by the variable nour)
# copy_name2 = name[:] # Copy by value (the register is assigned by the value zain)

# # Methods
# my_name = '   nour alhammami   '
# print(len(my_name))             # class method
# print(my_name.find("i"))        # str. method
# uppercase= print(my_name.upper())
# lowercase= print(my_name.lower())
# capital_all_first_letters= print(my_name.title())
# capital_first_letter= print(my_name.capitalize())
# count_letters= print(my_name.count('m',10))
# remove_spaces= print(my_name.strip())
# replace_m_letter = print(my_name.replace('m','*'))
# my_email = input('Enter your E-mail: ')
# print(f"Your E-mail is {my_email.replace(my_email[2:my_email.find('@')],'*******')}")
# split_word = print(*my_name.strip())
# end = print(my_name.strip().endswith('i'))


# # Operations type // floor (round down) % modulus (remind)
# num1 = 4
# num2 = 25
# print(num1+num2 , num1-num2 , num1*num2 , num1/num2 , num1**num2 , num1//num2 , num1%num2 , num2%num1)
# num2 += 5
# print(num2)
# num2 -= 5
# print(num2)
# num2 //= 3
# print(num2)

# # comparing ==/ >= /<= / < / > / != / is / is not / in / not in
# num1 = 4
# num2 = 25
# print(num1==num2)
# print(num1>=num2)
# print(num1<=num2)
# print(num1>num2)
# print(num1<num2)
# print(num1!=num2)
# num2 = 10.0
# num1 = 10
# print(num1 is num2)
# print(num1 is not num2)
# name = 'nour'
# print("n" in name)
# print("n" not in name)
