#  Write a Python program to sort a given dictionary by key.

dict1={
    1:'a',
    2:'b'
}

print(dict(sorted(dict1.items(), key = lambda x: x[0])))
# {1: 'a', 2: 'b'}

print(dict(sorted(dict1.items(), key = lambda x: x[0], reverse=True)))
# {2: 'b', 1: 'a'}