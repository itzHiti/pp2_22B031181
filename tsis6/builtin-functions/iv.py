# Напишите программу на Python, которая вызывает функцию квадратного корня через определенные миллисекунды
# "Короче надо просто юзать sleep()"


import time,math

# Sample Input:
n1 = input() # Number to find square root
n2 = input() # Milliseconds to wait

# Sample Output:
time.sleep(int(n2)/1000) # sleep() in seconds, so to do milliseconds we must divide to 1000
print("Square root of ",n1," after ",n2, " miliseconds is ", math.sqrt(int(n1)))