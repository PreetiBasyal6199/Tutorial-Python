#  Write a Python program to iterate over dictionaries using for loops.

dict1={
    'a': 1,
    'b': 2,
    'c': 3,
    'd':4
}

for key, value in dict1.items():
    print(f"{key} is {value}")

# a is 1
# b is 2
# c is 3
# d is 4