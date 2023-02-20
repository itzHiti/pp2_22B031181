def generator(n):

    for i in range(int(n)):
        i = i+1
        yield i*i

n = input("Enter number: ")
for i in generator(n):
    print(i)

# before defence: https://pythonist.ru/generatory-v-python/