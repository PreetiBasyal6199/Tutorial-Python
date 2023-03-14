# Public Attributes
class PublicAttributeClass:
    def __init__(self,a) :
        self.a = a


obj1 = PublicAttributeClass(2)
print(obj1.a)               #accessing public attributes
obj1.a = 45                 #setting the value of public attributes
print(obj1.a)


#Private Attributes

class SampleClass:
    def __init__(self,a) :
        self.__a = a

    def get_a(self):
        return self.__a
    
    def set_a(self,a):
        self.__a=a

obj1 = SampleClass(2)
# print(obj1.__a)             #  Error 'SampleClass' object has no attribute '__a' since private attribute cannot be accesed directly
print("Hello", obj1._SampleClass__a)   # We can access the private attribute by this naming convention
print(obj1.get_a())       #  accessing private attributes outside the class
obj1.set_a(45)             # setting the value of private attributes outside the class
print(obj1.get_a())    


class PrivateAttributeClass:
    def __init__(self, p):
        self.__p = p

    @property
    def p_method(self):
        return self.__p
    
    @p_method.setter            #@method_name.setter
    def p_method(self, p):
        self.__p = p

private_obj = PrivateAttributeClass(30)
print(private_obj.p_method)            #  accessing private attributes outside the class
private_obj.__p=31                    # setting the value of private attributes outside the class
print(private_obj.__p)
    

class ProtectedAttributeClass:
    def __init__(self, c):
        self._c = c


protected_obj = ProtectedAttributeClass(20)
print(protected_obj._c)
protected_obj._c = 56
print(protected_obj._c)




