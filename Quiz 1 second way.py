mark_list = []
for i in range(3):
    marks = int(input(f"Enter {i+1} mark: "))
    mark_list.append(marks)

# print(max(mark_list))

if (mark_list[0] > mark_list[1]) and (mark_list[1] > mark_list[2]):
    print(mark_list[0])
elif (mark_list[0] < mark_list[1]) and (mark_list[1] > mark_list[2]):
    print(mark_list[1])
else:
    print(mark_list[2])
