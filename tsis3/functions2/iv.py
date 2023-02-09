import math
from dictionary import movies

def check():
    count = 0
    sum = 0
    for x in movies:
        count += 1
        sum += x["imdb"]
    return round(sum / count, 1) # 1 - 6.5, 2 - 6.49
print(check())