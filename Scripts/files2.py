import os

os.chdir('C:\\Users\TestServer\Deskto')
s=os.getcwd()

print("\nHere is the current directory {}".format(s))

files = [i for i in os.listdir(s) if os.path.splitext(i)[1] == '.zip' or os.path.splitext(i)[1] == '.txt']
file_count = len(files)
for file in files:
    print(os.path.join(s, file))
print(file_count)
