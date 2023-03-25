def my_generator(x):
    for i in range (x):
        yield i**3

result_values = my_generator(4)         #Created an iterator
print(next(result_values))              #0
print(next(result_values))              #1
print(next(result_values))              #8
print(next(result_values))              #27
# print(next(result_values))              # It raises StopIteration error sunce the iteration is completed 


'''The same result in be acheived using for loop'''
for item in result_values:
    print(item)