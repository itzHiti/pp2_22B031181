import math

#4
""" def filter_prime(num):
    numbers = []
    for i in num:
        prime = True
        if int(i) < 2:
            continue
        for j in range(2, int(i) - 1):
            if int(i) % j == 0:
                prime = False
        if prime == True:
            numbers.append(int(i))
    return numbers
'''
x = input("Enter numbers: ").split()
print(filter_prime(x))
''' """
#5
""" from itertools import permutations
s1 = str(input("Enter a string: "))
s2 = permutations(s1)
for x in s2:
    print(x) """
#6
"""
def reversecard(s2, start):
    while 1:

        # to avoid errors which happen after last word in list
        try:
            end = s2.index(' ', start)
            reversing(s2, start, end - 1)
            start = end + 1
    
        except ValueError: # reverse for last word
            reversing(s2, start, len(s2) - 1)
            break
    s2.reverse()
    s2 = "".join(s2) # converting list to string
    print(s2)
 

def reversing(s1, start, end):
    while start < end:
        s1[start], s1[end] = s1[end], s1[start]
        start = start + 1
        end -= 1

s = input("Enter a sentence: ")
s = list(s)
strt = 0
reversecard(s, strt)
"""

#7
"""
def has_33(numbers):
    for x in range(0, len(numbers) - 1):
        if numbers[x] == 3 and numbers[x + 1] == 3:
            return True # only if 3 is next to 3
    return False
'''
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
'''
"""
#8
"""def spy_game(numbers):
    center = 0
    for x in range(0, len(numbers)):
        if numbers[x] == 0:
            center += 1
        if center >= 2 and numbers[x] == 7:
            return True
    return False
'''
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
'''
"""
#9
"""
def volume():
    r = float(input())
    v = 4 / 3 * math.pi * r * r * r
    return v
'''
print(volume())
'''
"""
#10 
"""
def uniquefun(l):
    d = {}
    myList = []
    for x in l:
        if x not in d.keys():
            d[x] = 1
    for x in d.keys():
        myList.append(x)
    return myList
'''
l = input("Enter numbers: ").split()
print(uniquefun(l))
'''
"""