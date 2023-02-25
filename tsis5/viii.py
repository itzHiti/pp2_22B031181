import re # importing Regular Expressions

a = input()
fnd = re.findall("[A-Z][^A-Z]*", a)
print(" ".join(fnd))