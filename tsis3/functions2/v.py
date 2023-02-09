from dictionary import movies

def check(category):
    count = 0
    sum = 0
    for i in movies:
        if i["category"] == category:
            count += 1
            sum += i["imdb"]
    return round(sum / count, 1) # 1 - 6.4, #2 - 6.44
print(check("Romance"))