import random
#11 
"""
def isPalindrome(s):
    t = s[::-1]
    if(t == s):
        return True
    return False

'''
s = input("Enter smthng: ")

if isPalindrome(s) == True:
    print("Palindrome")
else:
    print("Not a palindrome")
'''
"""
#12 
"""
def histogram(num):
    for x in num:
        while x > 0:
            print("*", end = "")
            x -= 1
        print('')
'''
histogram([4, 9, 7])
'''
"""

#13 
"""
def check(a, name, count):
    m = int(input())
    count += 1
    if m == a:
        print("Good job,", name, "! You guessed my number in",count,"guesses!")
    if m < a:
        print("Your guess is too low.")
        check(a, name, count)
    if m > a:
        print("Your guess is too high.")
        check(a, name, count)
'''
print("Hello! What is your name?")
name = str(input())
print("Well, ", name, "," ,"I am thinking of a number between 1 and 20.")
print("Take a guess.")
count = 0
a = random.randrange(1,20)
check(a, name, count)
'''
"""