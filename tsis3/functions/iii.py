def solve(numheads, numlegs):
    rabbits = (int(numlegs) - 2*int(numheads))/2
    chickens = int(numheads) - int(rabbits)
    print("Rabbits:", int(rabbits), "Chickens:", int(chickens))
    
'''
a = input("Enter number of heads: ")
a = input("Enter number of legs: ")
solve(a, b)
'''