class Student:
    count = 1
    student_data = []  # Student's data collection list, it is a static variable

    def __init__(self, name, level):
        self.student_id = Student.count
        self.student_name = name
        self.student_level = level
        self.student_courses = []  # student's courses list, it is an object variable, it's come from Course class
        Student.count += 1

    @staticmethod
    def add_student():
        new_student_name = str(input("Enter the student name: ")).capitalize()
        while True:  # validation of the spelling of level
            new_student_level = str(input("Enter the student level (A, B, or C): ")).upper()
            if new_student_level in ["A", "B", "C"]:
                break
        student_obj = Student(name=new_student_name, level=new_student_level)
        Student.student_data.append(student_obj)
        print(f"The student: {new_student_name}, with level {new_student_level}, has been added successfully")

    @staticmethod
    def remove_student():
        ids = []
        for student in Student.student_data:
            ids.append(student.student_id)
        while True:  # validation of input ID and  its existence in the students data
            try:
                removed_id = int(input("Enter student ID: "))
            except ValueError:  # (ValueError) Exception to any error comes after casting the input
                print("Invalid input")
                continue
            if removed_id > 0 and removed_id in ids:
                for student in Student.student_data:
                    if removed_id == student.student_id:
                        Student.student_data.remove(student)
                        print(f"The student name: {student.student_name}, with ID: {student.student_id}, has been "
                              f"deleted successfully")
                break
            else:
                print("The ID does not found")
                continue

    @staticmethod
    def edit_student():
        ids = []
        for student in Student.student_data:
            ids.append(student.student_id)
        while True:  # validation of input ID and  its existence in the students data
            try:
                edit_id = int(input("Enter student ID: "))
            except ValueError:  # (ValueError) Exception to any error comes after casting the input
                print("Invalid input")
                continue
            if edit_id > 0 and edit_id in ids:
                for student in Student.student_data:
                    if edit_id == student.student_id:
                        student.student_name = str(input("Enter the student name: ")).capitalize()
                        while True:  # validation of the spelling of level
                            student.student_level = str(input("Enter the student level (A, B, or C): ")).upper()
                            if student.student_level in ["A", "B", "C"]:
                                break
                        print(f"The ID: {student.student_id}'s data has been modified successfully")
                break
            else:
                print("The ID does not found")
                continue

    @staticmethod
    def add_student_course():
        ids = []
        for student in Student.student_data:
            ids.append(student.student_id)
        while True:  # validation of input ID and  its existence in the students data
            try:
                look_for_student_id = int(input("Enter student ID: "))
            except ValueError:  # (ValueError) Exception to any error comes after casting the input
                print("Invalid input")
                continue
            if look_for_student_id > 0 and look_for_student_id in ids:
                for student in Student.student_data:
                    if look_for_student_id == student.student_id:
                        look_for_course_id = int(input("Enter course ID: "))
                        course = Course.get_course_id(look_for_course_id)
                        student.student_courses.append(course.course_name)
                break
            else:
                print("The ID does not found")
                continue

    @staticmethod
    def get_students_data():
        print("|ID\t\t|"
              "student Name\t\t|"
              "Level\t\t|"
              "Courses")
        for student in Student.student_data:
            print(f"|{student.student_id}\t\t\t|"
                  f"{student.student_name}\t\t\t|"
                  f"{student.student_level}\t\t\t|"
                  f"{student.student_courses}")


class Course:
    count = 1
    courses_data = []  # course's data collection list, it is a static variable

    def __init__(self, name, level):
        self.course_id = Course.count
        self.course_name = name
        self.course_level = level
        Course.count += 1

    @staticmethod
    def add_course():
        new_course_name = str(input("Enter the course name: ")).capitalize()
        while True:  # validation of the spelling of level
            new_course_level = str(input("Enter the course level (A, B, or C): ")).upper()
            if new_course_level in ["A", "B", "C"]:
                break
        course_obj = Course(name=new_course_name, level=new_course_level)
        Course.courses_data.append(course_obj)
        print(f"The {new_course_name} course with level {new_course_level} has been added successfully")

    @staticmethod
    def get_course_id(look_for_course_id):
        ids = []
        for course in Course.courses_data:
            ids.append(course.course_id)
        while True:  # validation of input ID and  its existence in the students data
            try:
                int(look_for_course_id)
            except ValueError:  # (ValueError) Exception to any error comes after casting the input
                print("Invalid input")
                break
            if look_for_course_id > 0 and look_for_course_id in ids:
                for course in Course.courses_data:
                    if look_for_course_id == course.course_id:
                        return course
                break
            else:
                print("The ID does not found")
                break

    @staticmethod
    def get_courses_data():
        print("|ID\t\t|"
              "Course Name\t\t|"
              "Level")
        for course in Course.courses_data:
            print(f"|{course.course_id}\t\t\t|"
                  f"{course.course_name}\t\t\t|"
                  f"{course.course_level}")


while True:
    try:
        select_list = int(input("1- Add new student\n"
                                "2- Remove student\n"
                                "3- Edit student\n"
                                "4- Display all students\n"
                                "5- Create new course\n"
                                "6- Add course to student\n"
                                "7- Display all courses\n"
                                "0- Exit\n"
                                ": "))
    except ValueError:
        print("Invalid Input")
        continue
    if select_list not in [0, 1, 2, 3, 4, 5, 6, 7]:
        print("Enter a value from 0 to 7")
        continue
    else:
        pass
        if select_list == 1:
            Student.add_student()
            Student.get_students_data()
        elif select_list == 2:
            Student.remove_student()
            Student.get_students_data()
        elif select_list == 3:
            Student.edit_student()
            Student.get_students_data()
        elif select_list == 4:
            Student.get_students_data()
        elif select_list == 5:
            Course.add_course()
            Course.get_courses_data()
        elif select_list == 6:
            Student.add_student_course()
            Student.get_students_data()
        elif select_list == 7:
            Course.get_courses_data()
        else:
            exit()
