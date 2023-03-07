import os, termcolor

d_p = os.getcwd()

def show(path, d):
    for item in os.listdir(path):
        target_path = os.path.join(path, item)
        if os.path.isfile(target_path):
            print('  '*d, "File: {0}".format(item))
        if os.path.isdir(target_path):
            print('  '*d, "In Dir: {0}".format(item))
            show(target_path, d+1)

s = input("Path: ")
e = os.path.exists(os.path.join(d_p, s))
if(e == True):
    termcolor.cprint("This path contains: ", "green", attrs=["underline"])
    show(os.path.join(d_p, s), 1)
else:
    termcolor.cprint("Oops... There is no such path.", "red")