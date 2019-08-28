#Python
import os
import sys


rhel6= [ '/var' , '/root' , '/tmp' ]
rhel6.sort()
os.system("ls -al")

for list in rhel6:
    os.chdir(list)
    s=os.getcwd()

    print("\n")
    print(s, "Here is the directory")
    print("\n")
    print("Here is disk usage for directory")
    t=os.system("du -sh")
    print("\n")

    n=os.listdir(list)

def linux ():
    print("\n")
    print("File Systems Storage")
    print("\n")
    os.system("df -Th")
linux()

# python

import os
import sys


rhel6= [ '/var' , '/root' , '/tmp' ]
rhel6.sort()
os.system("ls -al")

for list in rhel6:
    os.chdir(list)
    s=os.getcwd()

    print("\n")
    print(s, "Here is the directory")
    print("\n")
    print("Here is disk usage for directory")
    t=os.system("du -sh")
    print("\n")

    n=os.listdir(list)

    for file in n:
        print(file)


def linux ():
    print("\n")
    print("File Systems Storage")
    print("\n")
    os.system("df -Th")
linux()
