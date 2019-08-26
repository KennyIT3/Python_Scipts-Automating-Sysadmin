#python
import os
import sys
import subprocess
import platform

print("Checking docker")
d = "docker"

test= subprocess.call(["ps", "-C" , d])
if test == 0:
    print("This service is running")
else:
    print("This service is not running")



# s = subprocess.check_output('docker images', shell=True).decode
# print('Results of docker ps' + "\n" + str(s))
# if s.find('containername') != -1:
#     print('found!')
# else:
#     print('not found.')
# if s >=8:
#     print("Alot of Images")
# else:
#     print("Few Images")
# n=os.system("docker images")
# p = subprocess.Popen(["docker images"], shell=True, stdout=subprocess.PIPE)
# s = p.split('\n')
# print(s)
# for line in p.stdout:
#     s= line.strip()
#     print((str), s)
#     if "IMAGE ID" in line:
#         print(IMAGE)
#     else:
#         print("done")
     #    for s in line
     #
     #
     #
     #
     # if "IMAGE ID" in line:
     #     print(out)
     # else:
     #     print("done")
# out = p.stdout.read()
# output=n.communicate()
# print(out)
# for images in n:
#     print(line.rstrip(n))
#     print("\n")
# if out >= 8:
#     print("You have alot of images")
# else:
#     print("Keep the images low")
