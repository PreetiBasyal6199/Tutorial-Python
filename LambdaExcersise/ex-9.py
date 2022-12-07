# Write a Python program to check whether a given string is number or not using Lambda.

test_result = lambda str: True if str.is_digit() else False
print(test_result("2"))