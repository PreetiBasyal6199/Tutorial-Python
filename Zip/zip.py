'''
Python zip() function returns a zip object, which maps a similar index of multiple containers. 
'''

list1=[1,2,3,4,5]
list2=['a','b','c','d']

a = zip(list1, list2)

# Converting iterator to list
list_rslt =(list(a))     
print(list_rslt)                     # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

# Converting iterator to dict
dict_rslt = dict(a)
print(dict_rslt)                             # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# Converting iterator to set
set_rslt = set(a)                       # {(3, 'c'), (2, 'b'), (4, 'd'), (1, 'a')}
print(set_rslt)

#Unpacking the list 
c,v = zip(*list_rslt)
print(c)                               # (1,2,3,4) 
print(v)                                #('a','b','c','d')


# 