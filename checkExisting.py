from sys import argv
from os import listdir
from os.path import isfile, isdir, join, splitext

path = argv[1]

def log(text):
    with open("logger.log", "a") as file:
        file.write("\n{}".format(text))

def checkExtensions(path):
    extensions = ["3dm", "3ds", "fbx", "obj", "STL", "jpg"]
    files2 = listdir(path)
    files = []
    for f in files2:
        files.append(f.split(".")[1])


    extensions_nera = []
    for ext in extensions:
        #print(ext)
        
        #checks if file's extension is in the list
        if ext in files:
            pass
            #print("{} exists".format(ext))
        else:
            log("{}: {}".format(path, ext))
            #print("{} doesn't exist".format(ext))
            extensions_nera.append(ext)

for folder in listdir(path):
    if isdir(join(path, folder)):
        checkExtensions(join(path, folder))
    if isfile(join(path, folder)):
        pass
