import re # importing Regular Expressions

a = input()
fnd = re.findall("a.*b$", a) # findall(pattern, string, flags=0)
print("Found:",fnd)