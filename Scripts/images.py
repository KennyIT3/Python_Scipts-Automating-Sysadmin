#python
import re
import os
n=10
p = os.popen("docker images").read()
# p = os.popen("df -h").read()
docker=p
columns = [list() for images in range(9)]
for line in docker.split("\n"):
    line = re.sub(" +", " ", line)
    for images,dock in enumerate(line.split(" ")):
        columns[images].append(dock)
print("\n")
print("Removing header image:", columns[2].pop(0) , "\n")

for images in columns[2]:
    print("List of Images:", images, "\n")
# for element in columns[2]:
#     print(element)
k=int(images[2])

if n <= k :
    print("Alot of Images")
else:
    print("Keep the Images at or below this number. 10:")

# for element in k:
#     s=element[0:].split("  ")
#     t=list(s)
#     # element.splitlines()
#     # printlist(element))
#     print("List of new images:", len(t) , "\n")


# print(type(k))
# s= columns[2].remove('IMAGE')
# for f in k:
#     f.strip()
#     f.replace('IMAGE', 'List of Images') #Incorpate a string replace to replace the first index in string
#     print(s)
    # print(type(f))
    # print(f, "\n")
# # print(s)
