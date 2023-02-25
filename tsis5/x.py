import re # importing Regular Expressions

a = input()
fnd = re.findall("[a-zA-z][^A-Z]*", a)
for i in range(len(fnd)):
    fnd[i] = fnd[i].lower()
print("_".join(fnd))