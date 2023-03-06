def bif2(s):
    U = 0
    l = 0
    for i in range(len(s)):
        if s[i].islower():
            l+=1
        elif s[i].isupper():
            U+=1
    return (U, l)
print(bif2(input("Enter string: ")))