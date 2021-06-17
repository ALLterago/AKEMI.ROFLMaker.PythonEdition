import os
import pathlib

class user:
    userName = None
    passWord = None
    saveFile = None


def loginMeth(userName,passWord):

    print("did some login staff")

def registerMeth(userName,passWord):

    os.chdir(pathlib.Path(__file__).parent.absolute())
    os.chdir("../users")

    newUserName = input("Enter username") + ".txt"
    newUserPass = input("Enter password")
    newUserFile = open(newUserName)
    
    


    


    