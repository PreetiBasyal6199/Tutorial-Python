# Write a Python program to get the maximum and minimum value in a dictionary.

dict1={
    'a':1,
    'b':2,
    'c':3,
    'd':6,
    'e': 5
}
print ("The minimum value from the dictionary is",((sorted(dict1.values()))[0]))
# The minimum value from the dictionary is 1

print ("The maximum value from the dictionary is",((sorted(dict1.values(), reverse=True))[0]))
# The maximum value from the dictionary is 6

