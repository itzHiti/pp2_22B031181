def generator(n):

    for i in range(int(n)):
        i+=1 # removing zero :)
        if (i % 3 == 0 & i % 4 == 0):
            yield i

n = input("Enter number: ")
for i in generator(n):
    print(i)