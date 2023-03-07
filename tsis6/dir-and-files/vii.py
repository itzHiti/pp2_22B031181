import os

d_p = os.getcwd()
path1 = input("Path to file to copy from: ") # use: tsis6/dir-and-files/d/lips.txt
path2 = input("Path to file to copy to: ") # use: tsis6/dir-and-files/dd

p1 = os.path.join(d_p, path1)
p2 = os.path.join(d_p, path2)

f1 = open(p1, "r")
f2 = open(os.path.join(p2, "input.txt"), "w")
f2.write(f1.read()) # kostil' btw, no ya odobryayu
f1.close()
f2.close()