import os
path = "/tmp"
try:
    def enumeratepaths():
    #    """Returns the path to all the files in a directory recursively"""
        path_collection = []
        
        for dirpath, dirnames, filenames in os.walk(path):
            for file in filenames:
                fullpath = os.path.join(dirpath, file)
                path_collection.append(fullpath)
        print(path_collection)

    def enumeratefiles(path=path):
    #    """Returns all the files in a directory as a list"""
        file_collection = []
        for dirpath, dirnames, filenames in os.walk(path):
            for file in filenames:
                file_collection.append(file)
        print(file_collection)

    def enumeratedir(path=path):
    #print("Returns all the directories in a directory as a list")
        dir_collection = []
        for dirpath, dirnames, filenames in os.walk(path):
            for dir in dirnames:
                dir_collection.append(dir)
        print(dir_collection)

    if __name__ == "__main__":
        print("\nRecursive listing of all paths in a dir:")
        print("\n")

    for path in enumeratepaths():
        print(path)
        print('\n' "Recursive listing of all files in paths:")
    for file in enumeratefiles():
        print(file)
        print('\n' "Recursive listing of all dirs in files:")
    for dir in enumeratedir():
        print (dir)
        print('\n'"Recursive listing of all dirs in dir:")
        
except (RuntimeError, TypeError, NameError):
    pass
