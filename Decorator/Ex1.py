# decorator example

def my_decorator(func):
    def inner():
        func()
        print ("I am decorator returned object")
    return inner


@my_decorator
def greet():
    print ("hello I am here....")

greet()