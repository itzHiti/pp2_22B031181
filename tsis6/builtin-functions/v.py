ex1 = (False, True, 1, 1, True)
ex2 = (True, 1, True, True, 1)
print(all(ex1)) # False? Yes. OK
print(all(ex2)) # True? Yes. OK
"""
all([True, True, True]) # True
all([True, True, 0]) # False
all(("", True, 5)) # False
all((True, 1.75, "Hello")) # True
all({False, "World", True}) # False
all({"Hi", -0.5, True}) # True
all({0: "Hello", 1: "World"}) # False
all({"Hello World": -1.75, 5: 6}) # True
"""