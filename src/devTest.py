import os
import pathlib

def SumInt(x,y):   #тестю методы 1
    return x+y

def openUserfile(userName):
    
    os.chdir(pathlib.Path(__file__).parent.absolute())
    os.chdir("../users")
    
    userFilePath = os.getcwd() + "\\" + userName + ".txt"
    print(userFilePath)
    
    try:
        with open(userFilePath) as userFile:
            print(userFile.read())
    except FileNotFoundError:
        print("FileNotFoundError(is fine)")

def createDir(path,name):
    dirFull = path + name
    os.mkdir("dirFull")




