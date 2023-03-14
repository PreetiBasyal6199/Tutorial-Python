

class Student:
    name = "Ram"            #class attribute

    def __init__(self, age):
        self.age = age          #instance attribute

    @classmethod
    def to_string(cls):
        print (f"Hello I am ",cls.name)
    

stu = Student("hary")
stu.to_string()             #Hello I am Ram    ; since the class attribute cannot be modified outside the class

stu.name = "Bikram"
stu.to_string()             #Hello I am Ram    ; since the class attribute cannot be modified outside the class


class School:

    def __init__(self, address):
        self.address = address          #instance attribute

    @classmethod
    def get_address(cls):
        print(f"The scool is in {cls.address}")         # We can not access the instance attribute inside class method

school = School("Butwal")
school.get_address()                #AttributeError: type object 'School' has no attribute 'address'