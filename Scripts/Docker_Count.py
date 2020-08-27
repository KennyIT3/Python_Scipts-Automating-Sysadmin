#python
import re
import os
import subprocess 

p = os.popen("docker images").read()
#p=subprocess.run(['docker' , 'images'])
docker=p

print(type((docker)))

columns = [list() for images in docker]
for line in docker.split("\n"):
    line = re.sub(" +", " ", line)
    for images,dock in enumerate(line.split(" ")):
       columns[images].append(dock)
print("\n")

for images in columns[2]:
     print("List of Images:", images)
