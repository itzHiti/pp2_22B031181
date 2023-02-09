from dictionary import movies


def check():
    List = []
    for i in movies:
        if(i["imdb"] >= 5.5):
            List.append(i["name"])
    return List
print(check())