class Example:
    x=20                #class attribute

    def normal_method(self, x):
        return f"I am ", x
    
    @classmethod
    def class_method(cls):
        return f"The value of class is {cls.x}"
    
    def static_method(x):
        return f"I am static value {x}"
    

example = Example()

#-------------------------Normal Methods Calling--------------------------------------#
normal_result =example.normal_method(5)
print(normal_result)

#-------------------------Class Methods Calling--------------------------------------#
class_result =example.class_method()
print(class_result)


#-------------------------Static Methods Calling--------------------------------------#
static_result =example.static_method()
print(static_result)

