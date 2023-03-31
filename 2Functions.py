# functions

# # By enter the values
# def sin():
#     opposite_side = float(input('Enter opposite: '))
#     hypo = float(input('Enter hypo: '))
#     sin = opposite_side/hypo
#     return sin
#
# x = sin()
# print(x)


# # more simple
# def sin():
#     opposite_side = float(input('Enter opposite: '))
#     hypo = float(input('Enter hypo: '))
#     return opposite_side/hypo
#
# x = sin()
# print(x)


# # enter the value as a parameters (arguments)
# def sin(opposite_side,hypo):
#     return opposite_side/hypo
#
# x = sin(1,2)
# print(x)
# # or
# def sin(opposite_side,hypo):
#     return opposite_side/hypo
#
# x = sin(hypo=1, opposite_side=2)
# print(x)
# # or
# def sin(opposite_side,hypo):
#     return opposite_side/hypo
#
# opposite_side = float(input('Enter opposite: '))
# hypo = float(input('Enter hypo: '))
# x = sin(hypo=hypo, opposite_side=opposite_side)
# print(x)



# # define the arguments as a defaults
# def sin(opposite_side,hypo=2):  # the argument has default value must the last argument
#     return opposite_side/hypo
#
# opposite_side = float(input('Enter opposite: '))
# hypo = float(input('Enter hypo: '))
# x = sin(opposite_side=opposite_side)  # I do not request the hypo value, so the hypo's input is useless
# print(x)
# #or
# def sin(opposite_side,hypo=2): # here the hypo's argument definition is useless, cause the value will enter later
#     return opposite_side/hypo
#
# opposite_side = float(input('Enter opposite: '))
# hypo = float(input('Enter hypo: '))
# x = sin(opposite_side=opposite_side)
# print(x)


# ------------------------------------------------------------------------------------------------------

def add(num1, num2):
    return num1 + num2
#
# def sub(num1, num2):
#     return num1 - num2
#
# def multi(num1, num2):
#     return num1 * num2
#
# def div(num1, num2):
#     return num1 / num2
#
# def power(num1, num2):
#     return num1 ** num2
#
# num1 = float(input('enter num1 value: '))
# num2 = float(input('enter num2 value: '))
# x = add(num1, num2)+sub(num1, num2)+multi(num1, num2)+div(num1, num2)+power(num1, num2)
# print(x)


# def add(num1 = 10 , num2 = 5):
#     return num1 + num2
#
# def sub(num1 = 10 , num2 = 5):
#     return num1 - num2
#
# def multi(num1 = 10 , num2 = 5):
#     return num1 * num2
#
# def div(num1 = 10 , num2 = 5):
#     return num1 / num2
#
# def power(num1 = 10 , num2 = 5):
#     return num1 ** num2
#
#
# x = add()+sub()+multi()+div()+power()
# print(x)
