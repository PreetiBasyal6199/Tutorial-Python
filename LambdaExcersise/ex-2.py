# Write a Python program to create a function that takes one argument, and that argument will be
#  multiplied with an unknown given number.

def new_func(num):
    return lambda x: x * num

result =new_func(2)
print(result(4))