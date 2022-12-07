# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
#  also create a lambda function that multiplies argument x with argument y and print the result.

result = lambda number: number + 15
print(result(25))


result_2 = lambda arg1, arg2 : arg1 * arg2
print(result_2(2,3))