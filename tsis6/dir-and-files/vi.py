import os, termcolor

d_p = os.getcwd()
p = os.path.join(d_p, "tsis6/dir-and-files/ddd")

# https://www.ascii-code.com/

for i in range(65,91):
    f = open( os.path.join(p, "{0}.txt".format(chr(i))) , 'x')
    f.write("this is just regular file")
    f.close()
termcolor.cprint("Files from A to Z created succesfully.", "green", attrs=["bold"])
