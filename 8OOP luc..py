# class Chair:  # class starts with uppercase
#     chair_color = "white"  # create a properties
#     chair_thickness = 4
#
#
# chair_1 = Chair()  # creating object, chair_1 is an object
# print(type(chair_1))
# print(chair_1.chair_color)  # query about property, the property is static
# print(chair_1.chair_thickness)  # query about property, the property is static
#
# # here I can't change the color or thickness, so if you want change, you have to overwrite the default value as follows:
#
# chair_1.chair_color = "red"
# print(chair_1.chair_color)
#
# chair_11 = Chair()
# print(chair_11.chair_color)
#
#
# # الكرسي يعتبر كلاس، (قالب الكرسي) والكرسي الأول يعتبر اوبجكت والكرسي الثاني يعتبر اوبجكت، اللون والسماكة في هذه الحالة تعتبر خصائص للكرسي
# # في هذه الحالة عملية تغيير الخاصية وتعتبر مرهقة لأنك بحاجة لاستدعاء الخاصية وتغييرها
# # يمكن تعريف انستراكتور يجعل عملية تغييير الخصائص أو إنشاؤها لكل اوبجكت يكون عن طريق البارميرتز الموجودين داخل أقواس الكلاس
#
# class InitChair:
#     def __init__(self):  # الأن أنا عرفت انستراكتور خاص أصبح كل اوبجكت يؤشر عليه وليس على الكلاس
#         # هذه الانستراكتور مسؤولة عن إنشاء الاوبجكتس وإعطاء كل اوبجتك القيم الأولية والخصائص الأولية لهذا الأوبجكت
#         # هذا الانستراكتور خاص لا يتكرر، بمعنى أنك لا يمكنك تكرار الميثود هذا لا يمكنك استدعاؤه مرة أخرى
#         # السلف عبارة عن الريفيرنس الأساسي للأوبجكت الي انت واقف عليها والي انت قاعد بتنشئها، بمعنى أنك لمن أنشأت كرسي ثاني أنت قاعد بتنشئ خصائص لنفس الأوبجكت وليس لكل الكراسي
#         self.chair_color = "white"
#         self.chair_thickness = 4  # هنا أنا عرفت ميثود وخصائص انه هذه مخصصة فقط للاوبجيكت وتتع له بناء على نفس المرجع سيلف
#         # هذه التعريفات مؤقتة او ديفولد فقط تتغير من داخل الأقواس مباشرة كباراميترز
#         # نمقص خطوة صغيرة لتعريفها كباراميترز وهو تعريفها بجانب السيلف عن تعريف init
#         # بالتالي بدنا نرجع ونغير القيم الديفولد بحيث انها تسير تاخد المدخلات القادمة من المدخل (القادمة من الكونستراكتور (من بين الأقواس))
#
#
# # chair_2 = InitChair() # هنا ما طلع خطأ لأني معرف قيم ثابتة تابع بالأسفل
# # print(chair_2.chair_color)
# # print(chair_2.chair_thickness)
#
# class InitChairParam:
#     def __init__(self, color, thickness):  # أصبح Parameterized constractor
#         self.chair_color = color  # غالبا تكون القيم المعرفة داخل الكونستراكتور والمعرفة هنا للميثود هي نفس اسم الميثود يعني self.chair = chair_color
#         self.chair_thickness = thickness
#
#
# chair_3 = InitChairParam(color="yellow",
#                          thickness=2)  # هنا السيلف تتبع الاوبجكت الجديد بمعنى أنها صارت مرجع له وبمعنى آخر أصبحت داخل الكونستراكتورعبارة عن chair_3.chair_color = color
# chair_4 = InitChairParam(color="pink", thickness=5)
# chair_5 = InitChairParam("black", 5)
# print(chair_3.chair_color)
# print(chair_3.chair_thickness)
# print(chair_4.chair_color)
# print(chair_4.chair_thickness)
# print(chair_5.chair_color)
# print(chair_5.chair_thickness)
#
# chair_4.chair_thickness = 10
# print(chair_4.chair_thickness)
# print(chair_3.chair_thickness)
#
#
# # ---------------------------------------------------
# # تصميم واجهة تطبيقات فيه واجهتين أساسيتين الأولى صفحة شخصية والثانية صفحة التطبيق الأساسية
# # الأولى اسمها Profile والثانية اسمها Home
# # هناك رموز Icons خاصة بكل واحد
# # جميع هذه المعطيات تعتبر خصائص Properties
# class TabButton:  # الآن أنا عرفت قالب مخصص للواجهات
#     def __init__(self, tab_id, tab_icon):
#         self.tab_id = tab_id
#         self.tab_icon = tab_icon
#
#     def on_click(
#             self):  # الآن بدي اعرف ميثود (action) تظهر نتيجة عملية الضغط داخل نفس الكلاس (لاحظ self تم تعبئتها تلقائياً)
#         if self.tab_id == "Profile":
#             print("Profile Clicked")
#         elif self.tab_id == "Home":
#             print("Home Clicked")
#         else:
#             print(f"{self.tab_id} Clicked")
#
#
# prfile_btn = TabButton("Profile", "Profile.png")
# home_btn = TabButton("Home", "Home.png")
# print(prfile_btn.tab_id)  # هذه لعرض الخصائص
# print(home_btn.tab_id)
# prfile_btn.on_click()  # هذه اسمها ميثود
# home_btn.on_click()
#
#
# # -------------------------------------------------------
#
# class Car:
#     def __init__(self, brand, color):
#         self.brand_name = brand
#         self.color = color
#         self.speed = 0
#
#     def speed_up(self):
#         self.speed += 10
#         print(self.speed)
#
#     def speed_down(self, decrease):
#         if self.speed <= 0:
#             print("Car already stopped")
#         else:
#             self.speed -= decrease
#             print(self.speed)
#
#
# car1 = Car("KIA", "yellow")
# print(car1.speed)  # استعلام عن خاصية عن طريق الطباعة
# car1.speed_down(5)
# car1.speed_up()  # تنفيذ الأمر عن طريق
# car1.speed_down(3)
#
#
# # ------------------------------------------------------
class Student:
    def __init__(self, name, age, no):
        self.student_name = name
        self.student_age = age
        self.student_marks_no = no
        self.student_marks = []

    def add_mark(self, add):
        if len(self.student_marks) < self.student_marks_no:
            self.student_marks.append(add)
            print(f"marks are {self.student_marks}")
#         else:
#             print(f"you can not add, marks are {self.student_marks}")
#
#     def calculate_avg(self):
#         print(sum(self.student_marks) / len(self.student_marks))
#
#
# student1 = Student("Nour", 17, 4)
# student1.add_mark(14)
# student1.add_mark(15)
# student1.add_mark(16)
# student1.add_mark(17)
# student1.add_mark(18)
# student1.calculate_avg()
# print(student1.student_marks)

# ----------------------------------------------------------------------------

# import random
#
#
# class Subject:
#     def __init__(self, mark, title):
#         self.mark = mark
#         self.title = title
#
#
# class Student:
#     def __init__(self, name, age):
#         self.id = random.randint(10000, 99999)
#         self.name = name  # لا يمكن وضع input لمدخلات الخصائص أو الباراميترز
#         self.age = age
#         self.student_marks = []
#
#     def add_mark(self):
#         title = input("Enter Subject Title")  # يمكن وضع انبوت للميثود بشرط عدم تعريفها كارجيومينت او باراميتر
#         mark = float(input(f"Enter {title} Mark : "))
#         subject_obj = Subject(mark=mark, title=title)  # عرفنا اوبجيكت من كلاس المارك // ملاحظة يمكن الاستغناء عن mark=
#         self.student_marks.append(
#             subject_obj)  # هنا اصبحت ال Student.marks عبارة عن list of objects مع الملاحظة لا يمكن طباعة هذه الليست
#         # print(self.student_marks)
#
#     def get_student_subjects(self):
#         print("--------Subjects-------")
#         for subject in self.student_marks:
#             print(subject.title)
#         print("_______________________")
#
#     def get_student_average(self):
#         total = 0
#         for subject in self.student_marks:
#             total += subject.mark
#
#         average = total / len(self.student_marks)
#         print(f"Average = {average}")
#
#
# student1 = Student("Nour", 29)
# student1.add_mark()
# student1.add_mark()
# student1.add_mark()
# student1.get_student_subjects()
# student1.get_student_average()
