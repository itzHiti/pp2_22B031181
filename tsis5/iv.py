import re # importing Regular Expressions

a = input()
fnd = re.findall("[A-Z]{1}[a-z]", a) # findall(pattern, string, flags=0)
print("Found:",fnd)