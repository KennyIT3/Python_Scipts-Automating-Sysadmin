#python
import os
import sys


rhel6= [ '/var' , '/root' , '/tmp' ]
rhel6.sort()
<<<<<<< HEAD
os.system("ls -al")
=======
<<<<<<< HEAD
<<<<<<< HEAD
os.system("ls -al")
=======
# os.system("ls -al")
>>>>>>> initial commit
>>>>>>> initial commit
=======
# os.system("ls -al")
>>>>>>> initial commit
>>>>>>> 0bc8b81863b4c7fceb570ae81440d46fd3952948

for list in rhel6:
    os.chdir(list)
    s=os.getcwd()

    print("\n")
    print(s, "Here is the directory")
    print("\n")
    print("Here is disk usage for directory")
    t=os.system("du -sh")
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
    print("\n" ,"Files in directory")
>>>>>>> initial commit
>>>>>>> initial commit
=======
    print("\n" ,"Files in directory")
>>>>>>> initial commit
>>>>>>> 0bc8b81863b4c7fceb570ae81440d46fd3952948
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
