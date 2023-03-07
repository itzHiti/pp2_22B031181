import os, termcolor, sys

d_p = os.getcwd()

s = input("Path: ")
txt = input("Name of text file to show (specify extension): ")
# to avoid errors
try: 
    f = open(os.path.join(os.path.join(d_p, s), txt), "r")
except FileNotFoundError:
    termcolor.cprint("Oops... There is no such path.", "red")
    sys.exit()
except OSError:
    termcolor.cprint("Oops... It looks like you made mistake somewhere in the path.", "red")
    sys.exit()
i = 0
for item in f.readlines():
    i+=1
print(i)
f.close()