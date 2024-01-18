class Student:

    name = None
    age = None
    courses = []


    def __init__(self,student_name,student_age):
        self.name = student_name
        self.age = student_age
        self.courses =[]

    def Add_a_course(self,course):
        self.courses.append(course)
        print(f"{self.name } is enrolled a new course: { course} ")

    def Drop_a_course(self,course):
        if course in self.courses:
            self.courses.remove(course)
            print(f"{self.name} has droped the course: {course} ")

        else:
            print(f"{self.name} is not enrolled in this course: {course} ")

    def display_info(self):
        print(f"Student Information:\n:- Name:{self.name}\n:- Age:{self.age}\n:- Courses:{','.join(self.courses)}")
    def update_age(self,new_age):
        self.age = new_age
        print(f"{self.name}'s age has been updated to {new_age}")

get_student1 = Student(student_name="sangam",student_age=27,)
get_student1.Add_a_course("m.tech")
print(get_student1.display_info())
get_student1.Add_a_course(" Mathematics, Physics, CCC")
print(get_student1.display_info())
get_student2 = Student(student_name="SHIVAM",student_age=37,)
get_student2.display_info()
get_student2.Add_a_course("python,C,C++,JAVA,HTML")
get_student2.display_info()
get_student2.update_age(55)
get_student2.display_info()