def generator(n):
    while(int(n) >= 0):
        yield n
        n = int(n) - 1

n = input("Enter number: ")
for i in generator(n):
    print(i)