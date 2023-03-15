# Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

new = d1.copy()

for key, value in d2.items():
    if key in new.keys():
        new[key] += value
    else:
        new[key] = value
    
print(new)
# {'a': 400, 'b': 400, 'c': 300, 'd': 400}

# Next Solution 
# from collections import Counter
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d = Counter(d1) + Counter(d2)
# print(d)