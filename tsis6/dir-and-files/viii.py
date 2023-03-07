import os, termcolor

d_p = os.getcwd()
s = input("Path: ")
f = input("File (w/ extension): ")
e = os.path.exists(os.path.join(os.path.join(d_p, s), f))
if (os.access(os.path.join(os.path.join(d_p, s), f), os.R_OK), e == True):
    os.remove(os.path.join(os.path.join(d_p, s), f))
    termcolor.cprint("File deleted.", "yellow")
else:
    termcolor.cprint("Oops... There is no such file (maybe you already deleted it).", "red")
# example: tsis6/dir-and-files/ddd
# "LETTER".txt