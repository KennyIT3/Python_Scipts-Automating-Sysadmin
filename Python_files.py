#Python
import pathlib
import os
import datetime

# This shows what directory you are in
path= pathlib.Path.cwd()
path_window=pathlib.WindowsPath('C:/Users/demo/Desktop')

print(f"What is the current directory:", path)
print()
print(f"What is in the directory:", path_window)

python = 0

for file in path_window.glob('*.py'):
	#Gets the modified time for each file
	time=os.path.getmtime(file)
	#Adds 1 for each file that is .py extension
	python += 1
	#Prints out the files and the modified time
	print(file, ' ' "Data Modified: " + time.ctime(time))
	
	print("")
print()	

print(f"How many python files are in this directory: ", python)
if python > 5:
	print("That's alot of files")
else:
	print("You need to script more")