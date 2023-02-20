def generator(n):

    for i in range(int(n)):
        i = i+1
        if i % 2 == 0:
            yield i

n = input("Enter number: ")
for i in generator(n):
    print(i)