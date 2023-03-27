def generator(n):

    for i in range(int(n)):
        if (i % 7 == 0):
            yield i

n = input("Enter number: ")
for i in generator(n):
    print(i)

# No limit in range (line 3)
# Difference between lists and generators