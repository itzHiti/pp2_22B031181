# https://python-scripts.com/import-os-example

import os, termcolor

d_p = os.getcwd() # current dir (in my case it is C:\Users\Мади\Desktop\python tsis\pp2_22B031181)

def show_files(path):
    for item in os.listdir(path):
        target_path = os.path.join(path, item)
        if os.path.isfile(target_path):
            print(item)
def show_dirs(path):
    for item in os.listdir(path):
        target_path = os.path.join(path, item)
        if os.path.isdir(target_path):
            print(item)
def show(path, d):
    for item in os.listdir(path):
        target_path = os.path.join(path, item)
        if os.path.isfile(target_path):
            print('  '*d, "File: {0}".format(item))
        if os.path.isdir(target_path):
            print('  '*d, "In Dir: {0}".format(item))
            show(target_path, d+1)

s1 = input("Path: ") # for debugging enter this: "tsis6/dir-and-files/d"
p = os.path.join(d_p, s1) # <- to avoid any mistakes in writing paths "join(path, *paths)"

print("")
print(termcolor.colored("Found this:", "green"))
print("")

print(termcolor.colored("FILES:", "blue", attrs=["underline"]))
show_files(p)
print(termcolor.colored("DIRS:", "yellow", attrs=["underline"]))
show_dirs(p)
print(termcolor.colored("DIRS and FILES:", "green", attrs=["underline"]))
show(p , 1)