import re # importing Regular Expressions

a = input()
#fnd = re.sub("[a-z]*_*[a-z]", "", a) # sub(pattern, replace, string)
fnd = re.findall("[a-z][^_]*", a)
print("".join(wrd.capitalize() for wrd in fnd))