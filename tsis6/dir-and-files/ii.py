import os, termcolor

d_p = os.getcwd()
s = input()
spec_path = os.path.join(d_p, s)
e = os.path.exists(spec_path)
if e:
    rwe = True #read, write, execute
else:
    rwe = False
print ("Path exists?: ", e)
termcolor.cprint("=== Propreties ===", "green", attrs=["bold"])
print("""Readable?: {0}
Writable?: {0}
Executable?: {0}""".format(rwe))

# Examples: tsis6/dir-and-files/d"
# tsis6/dir-and-files/dd/add