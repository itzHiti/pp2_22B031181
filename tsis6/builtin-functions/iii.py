def bif3(s):
    print("Is Palindrome? ")
    if list(s) == list(reversed(s)):
        return True
    return False
print(bif3(input("Enter string: ")))