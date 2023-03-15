#  Write a Python program to map two lists into a dictionary.

list1 =['a', 'b', 'c']

list2=[1,2,3]


dict_1 = zip(list1, list2)

# print(set(dict_1))
# {('c', 3), ('a', 1), ('b', 2)}

print(dict(dict_1))
# {'a': 1, 'b': 2, 'c': 3}
