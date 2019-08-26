# #python
# import os
# import sys
# import re
# import subprocess
#
#
# # rhel6= [ '/var' , '/root', '/tmp']
# rhel5= [ '/area' , '/area1']
#
#
# for list in rhel5:
#     # time=os.system("find $list -mtime -1 -regex '.*[A-Za-z].*' -exec ls -l {} \; ")
#
#     os.chdir(list)
#     s=os.getcwd() #Gets the current directory
#     # time=os.system("find $files -mtime -1 -regex '.*[A-Za-z].*' -exec ls {} \;") #Optional arguments for file age
#     print("\n")
#     print(s, "Here is the directory")
#     # print(t)
#     print("\n")
#     n=os.listdir(list)
#     n.sort()
#     for directory in n:
#         directory.strip("\n")
#         t=os.path.isdir(os.path.join(list, directory))
#         if t == True:
#             print("These are the subdirectories: ",  directory)
#             print("\n")
#             continue
# #Check for files in the directories
#     for files in n:
#         files.strip("\n")
#         f=os.path.isfile(os.path.join(list, files))
#         if f == True:
#             # k=os.popen("du -sh /").read()
#             # k=subprocess.Popen(['du', '-sh', '$list'], shell=True)
#             #k=os.path.getsize(files) << 10 #Optional arguments for file size
#             #time=os.system("find $files -mtime -1 -regex '.*[A-Za-z].*' -exec ls {} \;") #Optional arguments for file age
#             print(f"These are the files: ",  files)
#             print("\n")
#             continue # Shows all the files but skips the remove
#     #Ask the user if he/she wants to remove files put of the directories
#             # if files == 0:
#             #     break
#         remove= input("Does the user want to remove files from the directory:")
#         # while remove == 2:
#         # continue
#         if remove=='Yes':
#             os.remove(files)
#             print('File has been removed')
#         elif remove=='yes':
#             os.remove(files)
#             print('File has been removed')
#         elif remove=="No":
#             print('No worries')
#             break
#             # sys.exit()
#         elif remove=="no":
#             print('No worries')
#             break
#             # sys.exit()
#         else:
#             print("Invalid. Please enter Yes or No")
#             # sys.exit()
#             continue
#
#     if len(directory)==0:
#
#         print("Directory is empty")
#     else:
#         # os.chdir(directory)
#         print("Directory is not empty")
#
# #Ask the user if he/she wants to remove the directory
#     remove= input("Does the user want to remove the directory:")
#     continue
#     if remove=='Yes':
#         os.rmdir(directory)
#         print('File has been removed')
#         continue
#     elif remove=='yes':
#         os.rmdir(directory)
#         print('File has been removed')
#         continue
#     elif remove=="No":
#         print('No worries')
#
#     elif remove=="no":
#         print('No worries')
#
#     else:
#         print("Invalid. Please enter Yes or No")
#         continue
