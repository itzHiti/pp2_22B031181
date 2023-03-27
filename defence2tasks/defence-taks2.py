import os, termcolor, sys, re

"data.txt"

# replace "ab" -> "bc"

d_p = os.getcwd()
try: 
    f = open(os.path.join(d_p, "task.txt"), "r")
except FileNotFoundError:
    termcolor.cprint("Oops... There is no such path.", "red")
    sys.exit()
except OSError:
    termcolor.cprint("Oops... It looks like you made mistake somewhere in the path.", "red")
    sys.exit()
i = 0
for item in f.readlines():
    if (item == "ab" or item == "AB"):
        i+=1
        item = re.sub("a.*b$", "bc", item) # sub(pattern, replace, string)
f.close()


# REDO
# Also revise regex speical characters