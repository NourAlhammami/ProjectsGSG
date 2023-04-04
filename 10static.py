# class Student:
#     count = 100  # هذا يسمى static/class variable
#
#     def __init__(self):  # هذا يسمى Object variable
#         self.age = 10
#
#
# # الستاتيك فاريبل يمكن استدعاؤه مباشرة من الكلاس نفسه
# print(Student.count)
# # أما استدعاء المتغير أو الانستراكتور الموجود داخل الميثود يمكن عن طريق تعريفه لمتغير جديد واستدعاؤه لذلك المتغير (فهو كالصفة او الاكشن الذي سينفذ لذلك المتغير)
# age = Student()
# print(age.count)
# print(age.age)


# ----------------------------------

# class Student:
#     count = 1  # هذا يسمى static/class variable
#
#     def __init__(self):  # هذا يسمى Object variable
#         self.id = Student.count
#         self.age = 10
#         Student.count += 1  # مع كل استدعاء تزيد واحد
#
#     def get_data(self):
#         return self.__dict__
#
#
# student_1 = Student()
# print(student_1.id)
# student_2 = Student()
# print(student_2.id)
# student_3 = Student()
# print(student_3.id)
# student_4 = Student()
# print(student_4.id)
# print(student_4.get_data())


# -----------------------------------
class Student:
    count = 1  # هذا يسمى static/class variable

    def __init__(self):  # هذا يسمى Object variable
        self.id = Student.count
        self.age = 10
        Student.count += 1

    @staticmethod  # هذه تعني أن هذا الميثود ثابت للكلاس بالتالي مش محتاج كل مرة وضع self بمعنى آخر يصبح ستاتيك ميثود وليس اوبجكت ميثود يصبح تابع للكلاس مباشرة يمكن استدعاؤه مباشرة للكلاس نفسه وليس محتاج مني تعريف متغير جديد ثم استدعاؤه للمتغير
    def get_id():
        print(Student.count)


student_1 = Student()
print(student_1.id)
student_1.get_id()  # هذا الأصل، والذي كان مسبقا فقط يُعرض من خلال الاوبجكت
Student.get_id()  # أصبح يمكن استدعاؤه مباشرة من الكلاس يعني من القالب نفسه
