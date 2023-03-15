#  Write a Python script to add a key to a dictionary. 

# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

dict_1 = {0: 10, 1: 20}
dict_1[2] = 30
print(dict_1)
# {0: 10, 1: 20, 2: 30}
dict_1.update({3:40})

print(dict_1)
# {0: 10, 1: 20, 2: 30, 3: 40}