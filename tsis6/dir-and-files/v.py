import os

d_p = os.getcwd()
p = os.path.join(d_p, "tsis6/dir-and-files/dd")

s1 = input("Enter text you want to write in file: ").split()
f = open(os.path.join(p, "input.txt"), 'w')
f.write(str(s1))
print('Done! Your input text is located in "../tsis6/dir-and-files/dd/input.txt"')
f.close()