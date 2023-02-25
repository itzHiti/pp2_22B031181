import re # importing Regular Expressions

a = input()
fnd = re.sub("[ ,.]", ":", a) # sub(pattern, replace, string)
print(fnd)