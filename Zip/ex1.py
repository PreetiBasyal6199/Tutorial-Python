list1=[1,2,3,4,5]
list2=['a','b','c','d']

a = zip(list1, list2)
list_rslt =(list(a))     
print(list_rslt)                     # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
dict_rslt = dict(a)
print(dict_rslt)                             # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}