from dictionary import movies


def check(film):
    for i in movies:
        if i["name"] == film:
            if i["imdb"] >= 5.5:
                return True
    return False
print(check("Exam"))
print(check("The Help"))