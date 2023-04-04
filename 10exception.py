# try:
#     print(10 / 1)
#     print("Hello world!")
# except Exception:
#     print("zero divided")
#
# try:
#     print(10 / 0)
#     print("Hello world!")
# except Exception:
#     print("zero divided")

# try:
#     print(10 / 0)
#     print("Hello world!")
# except ZeroDivisionError:
#     print("Change 0")

# import math
#
# try:
#     print(math.sqrt(-2))  # will not work with zero division error, the error will appear
#     print("Hello world!")
# except ZeroDivisionError:
#     print("Change 0")

# try:
#     print(10 / 0)
#     x = int("Ali")
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except Exception:
#     print("An error occurred")

# try:
#     x = int("Ali")
#     print(10 / 0)
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except Exception:
#     print("An error occurred")
# # -------------------------

# while True:
#     try:
#         x = int(input("Enter you age: "))
#     except Exception:
#         # print("The age must be integer")
#         continue
#     if x > 0:
#         break
