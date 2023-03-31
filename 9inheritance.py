# # parent inheritance توريث من الأبو للأبناء
#
# class Employee:
#     def __init__(self, name, dob, nod):
#         self.name = name
#         self.dob = dob
#         self.nod = nod
#
#
# class Fulltimeemployee(Employee):  # inheritance
#     pass
#
#
# class Parttimeemployee(Employee):  # inheritance
#     pass
#
#
# person = Employee("nour", "04-08-1993", 804718245)
# print(person.nod)
# print(person.dob)
# print(person.name)
# full_time_employee = Fulltimeemployee("zain", "09-05-2020", 48888840)
# print(full_time_employee.nod)
# print(full_time_employee.dob)
# print(full_time_employee.name)
# part_time_employee = Parttimeemployee("maryam", "19-09-1994", 410503601)
# print(part_time_employee.nod)
# print(part_time_employee.dob)
# print(part_time_employee.name)
#
#
# # في طريقة توريث الأباء للأبناء يكون الأب على غير دراية بما يضاف من جديد للإبن لكن الإبن يكون على دراية بكامل المتغيرات للأب مع إضافاته، يمكن التوضيح بالمثال التالي
#
# class Employee1:
#     def __init__(self, name, dob, nod):
#         self.name = name
#         self.dob = dob
#         self.nod = nod
#
#
# class Fulltimeemployee1(Employee1):  # inheritance
#     def __init__(self, salary, name, dob,
#                  nod):  # يجب عن تعريف كونستراكتور داخل سب كلاس يجب الضغط غلى alt+enter واعمل ادد حتى استدعي السوبر كونستراكتور
#         super().__init__(name, dob, nod)
#         self.salary = salary
#
#
# class Parttimeemployee1(Employee1):  # inheritance
#     pass
#
#
# full_time_employee1 = Fulltimeemployee1(5000, "zain", "09-05-2020", 48888840)
# print(full_time_employee1.salary)
# person1 = Employee1("nour", "04-08-1993", 804718245)
#
#
# # print(person1.salary)   # does not found
#
#
# # ------------------------------------


# # Type of inheritance
# # simple inh        child class >> parent class
#
# class parent_class:
#     pass
#
#
# class child_class(parent_class):
#     pass
#


#
# # Hierarchical inh  child 1 class >> parent class and child 2 class >> parent class     as previous
#
# class parent_class:
#     pass
#
#
# class child_1_class(parent_class):
#     pass
#
#
# class child_2_class(parent_class):
#     pass


# # multiple inh      child class >> parent 1 class and child class >> parent 2 class
#
# class parent_1_class:
#     def method_1(self):
#         print("That is method 1")
#
#     def method_3(self):
#         print("That is method 3")
#
#
# class parent_2_class:
#     def method_2(self):
#         print("That is method 2")
#
#     def method_3(self):
#         print("That is method 3")
#
#
# class child_class(parent_1_class, parent_2_class):
#     pass
#
#
# child_class = child_class()
# print(child_class.method_1())
# print(child_class.method_2())
# print(
#     child_class.method_3())  # come from the first class, because you are define the parent 1 then parent 2 as inherit.\
#
#
# # and the same will be in super class
#
#
# class PARENT_1_CLASS:
#
#     def __init__(self):
#         self.a_value = 30
#
#     def method_a(self):
#         print("method A from PARENT 1")
#
#     def method_c(self):
#         print("method C from PARENT 1")
#
#
# class PARENT_2_CLASS:
#     def method_b(self):
#         print("method B from PARENT 2")
#
#     def __init__(self):
#         self.a_value = 40
#
#     def method_c(self):
#         print("method C from PARENT 2")
#
#
# class CHILD_CLASS(PARENT_1_CLASS, PARENT_2_CLASS):
#
#     def __init__(self):
#         super().__init__()
#         self.a_value = 10
#
#     def method_c(self):
#         print("method C from Child ")
#
#
# child_class = CHILD_CLASS()
# child_class.method_c()  # from the first
# print(child_class.a_value)  # if the a_value define in child will be selected, if not will be the first from the
# # parent selected


# multi level inh       child class >> parent class and parent class >> grandparent class

# class PARENT_CLASS:
#
#     def method_a(self):
#         print("METHOD A FROM PARENT")
#
#
# class CHILD_CLASS_1(PARENT_CLASS):
#
#     def method_b(self):
#         print("METHOD B FROM CHILD1 ")
#
#
# class CHILD_CLASS_2(PARENT_CLASS):
#
#     def method_c(self):
#         print("METHOD C FROM CHILD 2")
#
#
# class CHILD_CLASS_3(CHILD_CLASS_1, CHILD_CLASS_2):  # hyper inheritance
#     pass


# --------------------------------------------------------------

class Shape:

    @abstractmethod
    def get_area(self):
        pass

    # def print_hello(self):
    #     print("Hello")


class Rectangle(Shape):
    def get_area(self):
        width = 4
        length = 5
        return width * length


class Circle(Shape):
    def get_area(self):
        radius = 5
        return math.pi * math.pow(radius, 2)


class Triangle(Shape):
    def get_area(self):
        base = 10
        height = 5
        return 0.5 * base * height


shape = Shape()
print(shape.get_area())  # NONE
rectangle = Rectangle()
print(rectangle.get_area())  # 20
circle = Circle()
print(circle.get_area())  # 3.14*25
triangle = Triangle()
print(triangle.get_area())  # 0.5 * 10 * 5 = 25
