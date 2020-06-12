#python
import re
import os

p = os.popen("docker images").read()
docker=p

print(type((docker)))
columns = [list() for images in range(9)]
for line in docker.split("\n"):
    line = re.sub(" +", " ", line)
    for images,dock in enumerate(line.split(" ")):
        columns[images].append(dock)
print("\n")
#print("Removing header image:", columns[2].pop(0) , "\n")

for images in columns[2]:
     print("List of Images:", images)
#print("List of Images:", columns[2], "\n")
