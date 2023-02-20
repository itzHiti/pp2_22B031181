def squares(a, b):
    for i in range(int(a), int(b)):
        yield i*i 


a = input("Enter number from: ")
b = input("Enter number to: ")
for i in squares(a, b):
    print(i)