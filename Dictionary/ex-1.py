#  Write a Python script to sort (ascending and descending) a dictionary by value.

dict_1 = {
    'a':1,
    'b':5,
    'c':2,
    'd': 9,
    'e':6
}

asc_dict = dict(sorted(dict_1.items(), key = lambda x : x[1]))
desc_dict = dict(sorted(dict_1.items(), key = lambda x : x[1], reverse=True))
print(asc_dict)
# {'a': 1, 'c': 2, 'b': 5, 'e': 6, 'd': 9}

print(desc_dict)
#{'d': 9, 'e': 6, 'b': 5, 'c': 2, 'a': 1}