#!/usr/bin/env python
import os
import glob

#String
p=os.popen("find /mnt/hgfs/Scripts -name '*.sh' -o -name '*.py' ").read()
#How to convert String to List
out=[p]
#How to sort list by Alphabet
out.sort()
if ".py" or ".sh" in out:
    print('We have scripts')
    print
    # print(out)
    #Print the output vertical
    for line in out:
        line.strip("\n")
        line=glob.glob('*.sh')
        print("\n")
        print("The Sh files")
        print("\n")
        for sh in line:
            print(sh)
            continue

        for py_files in line:
            py_files=glob.glob('*.py')
            print("\n" + "The Python Files")
            print("\n")
            for t in py_files:
                print(t + "\n")
            break
    # for line in out.split("*.sh"):
    #     # line = re.sub(" +", " ", line)
    #    print(line)
        # print("\n")
        # print(line)
else:
    print(" We have no script")

