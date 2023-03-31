marks_number = int(input("Enter the marks number: "))
mark_list = []
for i in range(marks_number):
    while True:
        marks = int(input(f"Enter {i + 1} mark: "))
        if marks > 100 or marks < 0:
            continue
        break
    mark_list.append(marks)
print(f"Average is {sum(mark_list)/marks_number} %")
print(f"max mark is {max(mark_list)}")
