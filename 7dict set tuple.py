# student = {
#     "Name" : 'nour',
#     "Age" : 29,
#     "Address" : {
#         "Country" : "Palestine",
#         "city" : "Gaza",
#         "street" : "Abdelqader alhusaini"
#     }
# }

# print(student)
# print(student["Address"])
# print(student.keys()) # returns list of the keys
# print(student["Address"].keys()) # returns list of sub dict keys.
# print(student.values()) # to return the values for the keys
# print(student["Address"].values()) # to return the values of the sub dict.
#
# print(student["Address"]["street"]) # to return selected value of the sub dict.
#
# print(student.get("Age")) # to return the value if found, None if not found
# print(student.get("Full_name"))

# print(student.items())  # print the key,value as list of tuples [(,),(,)]


# for i in student:  # print the key separately
#     print(i)

# for i , j in student.items():
#     print(i , j)
# for i, j in student.items():
#     print(f"Key = {i}, Value = {j}")
# for i, j in student.items():
#     print(f"Key = {i},\nValue = {j}")
# for i in student.values():
#     print(i)
# for i in student.keys():
#     print(i)

# if "Age" in student:
#     print("Yes")

# if 29 in student.values():
#     print("Yes")

# Ages = {
#     "Age1" : 20,
#     "Age1" : 30
# }
# print(Ages)

# ___________________________________________________________________________________________________________________

# students_number = int(input("Enter Student Number: "))
# students_data = []
# for i in range(students_number):
#     name = input("Enter Student Name: ")
#     age = int(input("Enter Student Age: "))
#     total_marks = int(input("Enter Student Total Marks: "))
#     marks = []
#     for j in range(total_marks):
#         mark = float(input(f"Enter {i+1} Student mark {j+1}: "))
#         marks.append(mark)
#     student_data = {
#         "Name" : name,
#         "Age" : age,
#         "Marks" : marks
#     }
#     students_data.append(student_data)
#
# print(students_data)
#
# for k in students_data: # you can calculate the avg inside the last step
#     extract_marks = k["Marks"]
#     average = sum(extract_marks)/len(extract_marks)
#     k["average"] = average
#
# print(students_data)
#
# ___________________________________________________________________________________________________________________

# students_number = int(input("Enter number of students: "))
# student_data = []
# for i in range(students_number):
#     name = str(input(f"Enter {i+1} name of student: "))
#     marks_number = int(input(f"Enter {i+1} number of marks: "))
#     for j in range(marks_number):
#         marks = float(input(f"Enter {j+1} mark: "))
#         marks_list.append(marks)
#     average = sum(marks_list)/marks_number
#     student_list = {
#         "name": name,
#     marks_list = []
#         "marks_list": marks_list,
#         "average": average,
#     }
#     student_data.append(student_list)
# print(student_data)


# for k in student_data:
#     extract_marks = k["marks_list"]
#     average2 = sum(extract_marks)/len(extract_marks)
#     k["average2"] = average2
# print(student_data)


# for i in student_data:
#     for j in i.values():
#         print(j)

# for i in student_data:
#     for j in i:
#         print(j)
# __________________________________________________________________________________________________________________
#
# my_tuple = (10,20,30,40,50,60,70,80,90)     # static list, unchangeable
# print(my_tuple)
# # example for unaccountability
# # my_tuple[0] = 40
# # my_tuple.pop()
# # example for printing
# print(my_tuple[0])
# # example for casting to edit
# print(list(my_tuple).pop())
# print(list(my_tuple)[2])
# my_edit_tuple = list(my_tuple)
# my_edit_tuple[4] = 45
# my_edit_tuple.insert(10,10)
# print(my_edit_tuple)

# for i in my_tuple:
#     print(i)
#
# for i in list(my_tuple):
#     print(i)
#
# my_list_tuple = [(1,2,3,4,5,6,7,8,9)]
# for i in my_list_tuple:
#     print(i)
#
# my_list_tuple = [(1,2,3,4,5,6,7,8,9)]
# for i,j,k,l,m,n,o,p,q in my_list_tuple:
#     print(i , j , k , l , m , n , o , p , q)

# __________________________________________________________________________________________________________________
# # set data type = return unique values
# my_set = {1,2,3,4,5,6,5,7,8,9,1,1,1,2,2,2}
# print(my_set)
# # unordered
# # print(my_set[3])
# # print(my_set.index(9))
#
# my_set.pop() # remove the first item
# my_set.pop()
# # my_set.remove() # will not work cause this method needs index
# my_set.add(40) # use this method to add
# my_set.add(1)
# print(my_set)
#
# for i in my_set:
#     print(i)
#
# if 9 in my_set:
#     print("Yes")
#
# my_list = [1,1,2,2,3,3,4,4,5,5]
# print(my_list)
# print(set(my_list)) # to remove the duplications

