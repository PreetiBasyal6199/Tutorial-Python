# Write a Python program to sort a list of tuples using Lambda.

list_1 = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

print(sorted(list_1, key= lambda x: x[1]))

#[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]