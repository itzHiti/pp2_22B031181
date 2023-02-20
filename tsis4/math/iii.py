import math

def area(a, b):
    return ((int(a) * int(b) * int(b))/4*ctg(180/int(a))) # formula for this was taken from: https://mnogoformul.ru/ploshhad-pravilnogo-mnogougolnika

def ctg(d): # there was no ctg() function in math library, so I implemented one
    return (1 / math.tan(math.radians(int(d)))) # ctg = cos / sin OR ctg = 1 / tan(or tg)


"""print(ctg(0)) # <- debuging: checked work of function above. UPD: it is working :D"""

n = input("Input number of sides: ")
a = input("Input the length of a side: ")
print("The area of the polygon is:", area(n, a)) # I think I need to round it, but I am not sure