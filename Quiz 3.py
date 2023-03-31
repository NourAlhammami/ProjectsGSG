students_number = int(input("Enter the students number: "))
avg_marks = []
for i in range(students_number):
    marks_number = int(input(f"Enter the {i+1} marks number: "))
    mark_list = []
    for j in range(marks_number):
        marks = float(input(f"Enter {j+1} mark: "))
        mark_list.append(marks)
    avg_marks.append(sum(mark_list)/marks_number)
print(avg_marks)
print(min(avg_marks))
print(max(avg_marks))
