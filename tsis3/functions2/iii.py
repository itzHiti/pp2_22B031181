from dictionary import movies

def check(category):
    List = []
    for i in movies:
        if i["category"] == category:
            List.append(i["name"])
    return List
print(check("Suspense"))