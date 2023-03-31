# from modules import sin , x # استدعاء فانكشن معين
# from modules import * # استدعاء جميع المعادلات الموجودة بنفس الملف
# print(sin(1,2))
# print(x)

import modules # عند استدعاء الملف كاملا نستكمل الاستدعاء بالدوت
print(modules.sin(2,3))
print(modules.x)

import math
print(math.sin(2/3))
print(math.e)
print(math.floor(1.2))
print(math.ceil(1.2))

import random
print(random.random())
print(random.random() *10)
print(random.randint(100,1000))
mylist = [1,2,3]
print(random.choices(mylist,weights=[10,1,1],k=10)) # عدد الوحدات يعبر عنها بالكي والوزن يعبر عن وزن كل خانة في القائمة

import datetime
print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)
print(datetime.datetime.now().microsecond)

print(datetime.datetime.now().strftime("%a"))  # click https://www.w3schools.com/python/python_datetime.asp
print(datetime.datetime.now().strftime("%a-%d-%m-%y"))
print(datetime.datetime.now().strftime("%A-%d-%m-%Y"))
current_time = datetime.datetime.now()
next_date = current_time + datetime.timedelta(days=10)
print(next_date)

import time
print(time.time())  # time value from 1-1-1970 by second