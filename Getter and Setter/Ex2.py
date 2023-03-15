#--------------------------Pass By Value --------------------------------#
x = 10
y=x                   
y=11

print(y)                    #11
print(x)                    #10
print(id(x)==id(y))         #false


#--------------------------Pass By Reference --------------------------------#
x = [1,2,3]
y=x                   
y.append(4)

print(y)                    #[1,2,3,4]
print(x)                    #[1,2,3,4]
print(id(x)==id(y))         #True



