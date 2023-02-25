import re # importing Regular Expressions

a = input()
fnd = re.findall("[a-zA-z][^A-Z]*", a)
print("_".join(fnd).lower())