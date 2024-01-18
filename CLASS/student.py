class School:

    def __init__(self,name,age,dob,address,Class,batch):
        self.name = name
        self.age = age
        self.dob = dob
        self.address = address
        self.Class = Class
        self.batch = batch


    def update_name(self,new_name):
        current_name = self.name
        self.name = new_name
        print(f" {current_name} has been updated their name to {new_name}") # __ has been updated to __

    def get_student_details(self):
        return f"Name:- {self.name}\n Age:- {self.age}\n DOB:- {self.dob}\n Address:- {self.address}\n Class:- {self.Class}\n Batch:- {self.batch}"

    def update_age(self,new_age):
        self.age = new_age
        print(f"{self.name} has been updated their age to {new_age}") # __ has been updated to __

    def update_dob(self, new_dob):
        self.dob = new_dob
        print(f"{self.name} has been updated their Dob to {new_dob}") # __ has been updated to __

    def update_address(self, new_address):
        self.address = new_address
        print(f"{self.name} has been updated new address {new_address}") # __ has been updated to __

    def student_type(self):
        if self.age <=0:
            print("Please enter positive age")
        elif self.age < 18:
            print(" Student is minor")
        else:
            print("Student is not minor")

    @staticmethod
    def Is_Holiday(dateTime):
      if dateTime.weekday()==5:
          return True
      # else:
      return False

obj_class = School(name="Raj",age=27,dob="14/12/1998",address="Amra",Class=10,batch="2022-23")
# obj_class1 = School(name="Mukesh",age=13,dob="24/11/2007",address="noida",Class="M.A",batch="2020-21")
# print(obj_class.dob)
#
# 
obj_class.update_name("Sangam Bhardwaj")
obj_class.update_address("Noida, 201301")
obj_class.update_age(4)
#
# obj_class.get_student_details()
obj_class.student_type()
# obj_class.update_name("shivam")
# obj_class.update_age(55)
print(obj_class.get_student_details())

import datetime
print(datetime.datetime.now().year)
print(obj_class.Is_Holiday(datetime.datetime.now()))
