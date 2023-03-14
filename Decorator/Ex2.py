class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name 

    @name.setter
    def name(self, name):
        self.__name=name

    @name.deleter
    def name(self):
        print('Deleting..')
        del self.__name


student_obj = Student("Ram")
print(student_obj.name)                 #Ram
student_obj.name = "Hary"           
print(student_obj.name)                 #hary

del student_obj.name


