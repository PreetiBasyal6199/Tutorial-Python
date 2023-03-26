'''
Reverse a number or string without using type casting
'''


def reverse_num(number):
    result = 0
    while number>0:
        rem = number%10
        number = number //10
        result = result*10+rem
    return result

print(reverse_num(23))

