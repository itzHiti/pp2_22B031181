import os, termcolor

d_p = os.getcwd()

def show_files(path):
    for item in os.listdir(path):
        target_path = os.path.join(path, item)
        if os.path.isfile(target_path):
            print(item)

s1 = input("Path: ") # for debugging enter this: "tsis6/dir-and-files/d"
p = os.path.join(d_p, s1) # <- to avoid any mistakes in writing paths "join(path, *paths)"

print("")
print(termcolor.colored("Found this:", "green"))
print("")

print(termcolor.colored("FILES:", "blue", attrs=["underline"]))
show_files(p)

# differences between "import os" and 