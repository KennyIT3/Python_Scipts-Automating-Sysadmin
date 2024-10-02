#! Python
import os
import subprocess

p = os.popen("docker images").read()
docker=p
print(docker)

s=subprocess.run(['docker' , 'images'])
for imags in s:
   print(imags)
#docker2=s
#print(type(s))
#print(docker2)
