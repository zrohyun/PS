import subprocess
import os

os.chdir("/Users/0hyun/Desktop/PS")

a = subprocess.Popen(['git', 'status','-su'], stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT)


a = a.stdout.read().decode("utf-8")
# print(a)
# print(type(a))

a = list(map(str,a.split("\n")))[:-1]

if a:
    typee , fname= a[0].split()
    if typee  == 'M':
        print("modi", fname)
    elif typee == "A" :
        print("Add", fname)

    else:
        print(fname)
