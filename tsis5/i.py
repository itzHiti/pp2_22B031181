import re # importing Regular Expressions

a = input()
fnd = re.findall("ab*", a) # findall(pattern, string, flags=0)
print("Found:",fnd)