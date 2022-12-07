# Write a Python program to find if a given string starts with a given character using Lambda.

result = lambda string, char: True if string.startswith(char) else False
print(result("Preeti", "Q"))
print(result("Preeti", "P"))

# False
# True
