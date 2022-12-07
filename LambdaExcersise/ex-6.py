# Write a Python program to square and cube every number in a given list of integers using Lambda.

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square_list = list(map(lambda x :x **2, list_1))
print(square_list)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

cube_list = list(map(lambda x: x**3, list_1))
print(cube_list)
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]