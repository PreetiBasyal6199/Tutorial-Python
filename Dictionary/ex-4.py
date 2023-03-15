# Write a Python script to check whether a given key already exists in a dictionary.

dict1={
    'a':1,
    'b':2,
    'c':3
}

def check_key(dict, key):
    return key in dict.keys() 

print(check_key(dict1, 'a'))
# True

print(check_key(dict1, 'd'))
# False
