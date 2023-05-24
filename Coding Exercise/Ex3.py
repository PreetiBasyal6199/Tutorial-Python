'''Create a list by picking an odd-index items from the first list and even index items
from the second'''

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3 = []
odd = l1[1::2]
even = l2[0::2]
l3.extend(odd)
l3.extend(even)
print(l3)

'''
Count the occurrence of each element from a list
'''
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
count = {}
for i in range(len(sample_list)):
    if sample_list[i] not in count.keys():
        count[sample_list[i]] = 1
    else:
        count[sample_list[i]] += 1
print(count)

'''
Slice list into 3 equal chunks and reverse each chunk
'''
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
new_len = len(sample_list) / 3
start = 0
end = int(new_len)
for i in range(3):
    chunk1 = sample_list[start:end]
    r_chunk1 = list(reversed(chunk1))
    print(r_chunk1)
    start = end
    end = int(new_len + end)

'''
Create a Python set such that it shows the element from both lists in a pair
'''
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
# Result is  {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}
rslt = set(zip(first_list, second_list))
print(rslt)


'''
Find the intersection (common) of two sets and remove those elements from the first set
'''
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
# Intersection is  {57, 83, 29}
# First Set after removing common element  {65, 42, 78, 23}

common = first_set.intersection(second_set)
new_set = first_set - common
print(new_set)

'''
Iterate a given list and check if a given element exists as a key’s value in a dictionary. 
If not, delete it from the list
'''
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
new = [x for x in roll_number if x in sample_dict.values()]
print(new)


'''
Get all values from the dictionary and add them to a list but don’t add duplicates
'''
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53,
         'july': 54, 'Aug': 44, 'Sept': 54}
speed_val = []
for x in speed.values():
    if x not in speed_val:
        speed_val.append(x)
print(speed_val)