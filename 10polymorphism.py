# # print(len("nour"))
# # تستخدم لتصميم فانكشن بتشتغل بأكثر من طريقة وهي ليست لوب او oop
#
# def add(num1=0, num2=0, num3=0):
#     return num1 + num2 + num3
#
#
# print(add(10))
# print(add(10, 20))
# print(add(10, 20, 30))
#
# # print(add(10, 20, 30, 40))  # هنا ستحدث مشكلة لانك لم تعرف اكثر من متغير

# -------------------
# def add(*args):
#     print(args)
#
#
# print(add(10, 20, 30, 40))  # هنا ستخرج لنا قائمة من نوع tuple

# --------------------
# def add(*args):  # هذا في حالة بدك تمرر قيم كلست
#     result = 0
#     for arg in args:
#         result += arg
#     return result
#
#
# print(add(50, 30, 50, 40))


# --------------------
def add(**kwargs):  # في حالة بدك تمرر قيم key and value
    result = 0
    print(kwargs)


print(add(name="nour", age=40))

# هذا على مستوى الفانكشن اما على مستوى الاوبجكت اورينتد بدك تستعمل الoverride
