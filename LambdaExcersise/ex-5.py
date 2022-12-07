#Write a Python program to filter a list of integers using Lambda. Go to the editor


list_1 =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list = list(filter(lambda x: x%2==0, list_1))
print(even_list)
# [2,4,6,8,10]


odd_list = list(filter(lambda x: x%2!=0, list_1))
print(odd_list)
# [1,3,5,7,9]