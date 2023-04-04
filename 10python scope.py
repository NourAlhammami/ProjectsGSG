اللوكال سكوب هو اي متغير معرف داخل الميثود ما بيظهر هذا المتغير لو استدعيته من خارج الميثود او من ايدينتيشن خارجي
الجلوبل ميثود هو استدعاء متغير موجود من خارج الميثود حتى لو كان داخل اف ستيتمنت او لوب معين او ايدنتيشن زيرو


----------------------------------
a = 10


def outer_method():
    a = 20
    b = 30
    print(
        f"a = {a} from inner method scope")  # تطبع الداخل لانها معرفه بالداخل فالأولوية للداخل ولو كانت غير معرفة بالخارج وغير معرفة بالداخل تأخذ الخارج


outer_method()
print(f"a = {a} from outer method scope")  # تطبع الخارج لأنها معرفه بالخارج
print(
    f"b = {b} from outer method scope")  # لن تطبع لانها غير معرفة بالخارج ولا تطبع الداخل مطلقا حتى لو معرف داخل الميثود

----------------------------------
num1 = 1
num2 = 2


def add():
    return print(num1 + num2)


add()

----------------------------------
num1 = 1
num2 = 2


def add():
    num1 = 3
    num2 = 4
    return print(num1 + num2)


# add()
print(add())  # تظهر القيمة مع none لأنك عامل امر طباعة داخلي في حال ما كنت عامل امر طباعة يمكن طباعته بشكل طبيعي
# print(num1 + num2)

----------------------------------
def outer_function():
    a = 10

    def inner_function():
        b = 20
        print(f"b= {b} from inner function")

    inner_function()
    print(f"a= {a} from outer function")


outer_function()  # هنا لا يمكن استدعاء الانر لانها داخليه ولا أيضا بالدوت لانها ليست اوبجكت اورينتد بالتالي يمكن استدعاؤها داخل الاوتر

----------------------------------
def outer_function():
    a = 10

    def inner_function():
        b = 20
        print(f"b= {b} from inner function")
        print(
            f"a= {a} from outer function")  # في هذه الحالة يمكن للانر الخروج للاوتر وقراءة المتغيرات منها لانهم جميعا داخل ميثود، بالتالي الميثود تأخذ من الخارج لكن الخارج لا يأخذ من داخل الميثود، والميثود الداخلية تأخذ من الخارجية لكن الخارجية لا تأخذ من الميثود الداخلية،

    inner_function()
    print(f"a= {a} from outer function")


outer_function()

----------------------------------
def outer_function():
    a = 10

    def inner_function():
        b = 20
        a = 50
        print(f"b= {b} from inner function")
        print(
            f"a= {a} from outer function")  # هنا الداخلية التي تظهر وفي حال عدم وجودها داخليا تاخذ من الخارجية

    inner_function()
    print(f"a= {a} from outer function")  # هنا تاخذ من الخارجية لعدم قدرة الخارجي على القراءة من الداخلي
    # print(f"b= {b} from inner function")


outer_function()

----------------------------------
def outer_function():
    a = 10

    def inner_function():
        b = 20
        nonlocal a
        a = 50
        print(f"b= {b} from inner function")
        print(
            f"a= {a} from outer function")

    inner_function()
    print(
        f"a= {a} from outer function")  # في حال اردتها تاخذ من الداخلي اذهب للداخلي واعرفله عن طريق nonlocal a بأنه اذهب للخارجي وجيبها جوا واقراها أو وعدل عليها ورجعها برا
    # print(f"b= {b} from inner function")

outer_function()

----------------------------------
a = 100


def outer_function():
    global a  # عندنا تريد التعديل على الخارج ولكن الخارج يكون خارج ميثود فإنك بحاجة لاستخدام جلوبل وليس نونلوكال
    a = 10  # في جميع الحالات هذه تصبح ليست متغير جديد هي فقط عملية لتعديل المتغير الخارجي

    def inner_function():
        b = 20
        global a  # هنا انت لن تستطيع استخدام نون لوكال حتى لو كنت بدك تستدعي الخارجي الي هو اصلا عبارة عن ميثود لان الخارجي الخاص بالميثود هو اصلا جلوبل
        a = 50
        print(f"b= {b} from inner function")
        print(f"a= {a} from outer function")

    inner_function()
    print(f"a= {a} from outer function")


outer_function()
print(a)

----------------------------------
a = 100


def outer_function():
    globals()["a"] = 50
    a = 10 # هنا المتغير هذا جديد كليا يختلف عن الخارجي ومنفصل عنه تماما يمكن حتى تغييره من ميثود داخلي
    print(a)


outer_function()
print(a)

----------------------------------
a = 100


def outer_function():
    globals()["a"] = 90 # هنا أنا فقط بعدل على الخارجي بدون تعديل الداخلي
    a = 80

    def inner_function():
        globals()["a"] = 70 # هنا أنا فقط بعدل على الخارجي بدون تعديل الداخلي
        a = 60
        print(f"a= {a} from inner function")

    inner_function()
    print(f"a= {a} from outer function")


outer_function()
print(f"a= {a} from global")

----------------------------------
a = 100


def outer_function():
    globals()["a"] = 90
    a = 80

    def inner_function():
        nonlocal a
        a = 60
        print(f"a= {a} from inner function")

    inner_function()
    print(f"a= {a} from outer function")


outer_function()
print(f"a= {a} from global")
