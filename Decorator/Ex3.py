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