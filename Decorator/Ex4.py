class Student:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_name():
        print(f"Hello I am a student")

stude_obj = Student("Harry")
stude_obj.get_name()