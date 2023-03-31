# # for loop
#
# start_point = int(input("Enter start point: "))
# end_point = int(input("Enter end point: "))
# steps = int(input("Enter steps value: "))
# for i in range(start_point, end_point+1, steps):        # step in default is 1
#     print(i)


# student_numbers = int(input("Enter total students: "))
# for j in range(student_numbers):
#     family_name = input(f"Enter {j+1} student name: ")


# marks_number = int(input("Enter number of students: "))
# total_marks = 0
# for k in range(marks_number):
#     mark = int(input(f"Enter {k+1} student mark: "))
#     total_marks += mark
# average = total_marks / marks_number
# if average >= 90:
#     print(f"Average = {average} - Excellent")
# elif average >= 80:
#     print(f"Average = {average} - Very Good")
# elif average >= 70:
#     print(f"Average = {average} - Good ")
# elif average >= 60:
#     print(f"Average = {average} - Passed")
# else:
#     print(f"Average = {average} - Failed")

# start_point = int(input("Enter start point: "))
# end_point = int(input("Enter end point: "))
# steps = int(input("Enter steps value: "))
# for i in range(start_point, end_point+1, steps):        # step in default is 1
#     print(i)


# for i in range(0 , 101):
#     if i == 0:
#         print(f"{i} neither even nor odd")
#     elif i % 2 == 0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")


# for i in range(0 , 101):        # continue : Skip this step and continue
#     if i == 0:
#         print(f"{i} neither even nor odd")
#         continue
#     elif i % 2 == 0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")
#     print("Hello")


# for i in range(0 , 101):        # break : Stop this step
#     if i == 0:
#         print(f"{i} neither even nor odd")
#         break
#     elif i % 2 == 0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")
#     print("Hello")

# for i in range(0, 101):  # break : Stop this step
#         if i == 0:
#             print(f"{i} neither even nor odd")
#             break
#         elif i % 2 == 0:
#             print(f"{i} is even")
#         else:
#             print(f"{i} is odd")
# print("Hello")


# for i in range(0, 13):  # multiplication table of number 6
#         print(f"6 * {i} = {i*6}")

# for i in range(0, 13):  # multiplication tables
#         print(f"_______START {i}_______")
#         for j in range(0,13):
#             print(f"{i} * {j} = {i*j}")
#         print(f"________END {i}________")


# number_test = 10   # while loop
# while number_test >= 0:
#     print(f"{number_test}")
#     number_test -= 1


# number_test = 10
# while number_test <= 10:
#     print(f"{number_test}")
#     number_test -= 1
#     if number_test == 0:
#         break


# # marks_number = int(input("Enter number of students: "))
# # while marks_number > 100 or marks_number < 0:
# #     marks_number = int(input("Enter number of students: "))
# while True:
#     marks_number = int(input("Enter number of students: "))
#     if marks_number > 100 or marks_number < 0:
#         pass
#     else:
#         break
# total_marks = 0
# for k in range(marks_number):
#     while True:
#         mark = int(input(f"Enter {k+1} student mark: "))
#         if mark > 100 or mark < 0:
#             pass
#         else:
#             total_marks += mark
#             break
# average = total_marks / marks_number
# if average >= 90:
#     print(f"Average = {average} - Excellent")
# elif average >= 80:
#     print(f"Average = {average} - Very Good")
# elif average >= 70:
#     print(f"Average = {average} - Good ")
# elif average >= 60:
#     print(f"Average = {average} - Passed")
# else:
#     print(f"Average = {average} - Failed")


# num = int(input("Enter the number: "))
# while True:
#     if num > 5:
#         print(num)
#         num -= 1
#     elif num == 5:
#         num -= 1
#         continue
#     elif num < 5 and num >= 0:
#         print(num)
#         num -= 1
#     else:
#         break


# num = 100
# while num != 0:
#     if num == 5:
#         num -= 1
#         continue
#     print(num)
#     num -= 1


# my_list = [40,50,60,10,20,30,80,90,60,10,20,30,80,60,10,20,30,80,60,10,20,30,80]
# i = 2
# while i < len(my_list):
#     print(my_list[i])
#     i += 3


# student_name = []
# student_number = int(input('enter students number: '))
# for i in range(student_number):
#     name = input('enter student name: ')
#     student_name.append(name)
# print(student_name)