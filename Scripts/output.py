import subprocess
import os

p = os.popen("docker images").read()
out = p
# print(out)

line = out.split()[0:8]
# for line in out
#     matches=
#
if "IMAGE ID" in out:

    print("alot of images")
    # print(out.split())
    print("Which Image:" , line)
else:
    print("done")
# for lines in out:
#     s=lines.split()[2]
#     print(s)
# #
# for line in out:
#     print(out)


# def main():
# for line in out:
#     print(line.strip())

#             print(s)
#     print( "")
# main()
