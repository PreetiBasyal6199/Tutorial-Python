from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def person_method():
        '''Interface method'''
        pass

class Student(IPerson):
    def __init__(self):
        self.name = "First Student"

    def person_method(self):
        print("I am a student") 

class Teacher(IPerson):
    def __init__(self):
        self.name = "First Teacher"

    def person_method(self):
        print("I am a teacher.")

class PersonFactory:

    @staticmethod
    def build_factory(person_type):
        if person_type =="Student":
            return Student()
        if person_type =="Teacher":
            return Teacher()
        raise ValueError("Invalid person type")
        


stu1 = Student()
stu1.person_method()

user_input = input("Please enter the person type:\n")
person_factory =PersonFactory()
person = person_factory.build_factory(user_input)
person.person_method()