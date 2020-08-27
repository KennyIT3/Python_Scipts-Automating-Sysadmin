import os
import sys

os.system('dir')
os.chdir('C:\\Users\demo\Desktop')
current=os.getcwd()
print()

print("What is the current directory", current)
print()

file=0

for foldername, subfolder, filenames in os.walk(current):
	for files in filename:
		#If file doesn't end with .txt or .zip the file will be skipped over for count
		if not files.endswith(('.txt' , '.zip')):
			continue
		if files.endswith(('.txt' , '.zip')):
			#Add + 1 to each file with that file extension
			file += 1 
			
			#joins the foldername with the name of the file
			print(os.path.join(foldername, files))
print(file)