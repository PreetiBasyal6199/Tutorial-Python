# Write a Python program to check a dictionary is empty or not.

dict1={
    'a':1,
    'b':2,
    'c':3,
    'd':6,
    'e': 5,
    'a':1,
    'b': 2
}
print(bool(dict1))
if len(dict1)==0:
    print( "The dictionary is empty")
else:
    print("Not")