from devTest import openUserfile,SumInt,createDir
from login import user,loginMeth,registerMeth
import os
import pathlib

print("Type \"login\" to log in")
print("Type \"register\" to register a new user")
print("Type \"skip\" to skip loging in")


isLoginComplete = False
#-------------------------------------------------------------
while isLoginComplete == False:
    loginState = input()
    if loginState == "login":
        loginMeth(input("Enter your username:"),input("Enter your password:"))

        isLoginComplete = True
#-------------------------------------------------------------        
    elif loginState == "register":
        registerMeth(input("Enter your username:"),input("Enter your password:"))
    
        isLoginComplete = True
#-------------------------------------------------------------        
    elif loginState == "skip":
        print("nologin")
        isLoginComplete = True
#-------------------------------------------------------------    
    else:
        print("wrong command")

print("\n")
Title = "Akemi ROFL Maker Python Edition"
TitleLine = "_______________________________________________________________________"
print(TitleLine)
print(Title) 

run = True
while run:

    print("\nAvailable commands:")
    print("devTest - testing/debug")
    print("TKinter - GUI stuff")
    print("gacha - simple gacha game(main feature by now)")
    print("exit - guess what it does by yourself\n")

    isCommandComplete = False 
#-------------------------------------------------------------
    while isCommandComplete == False :
        startcommand = input()           
        if startcommand == "devTest":
            print("Launching " + startcommand)   #всякая дебуг шляпа и тест фич перед внедрением
       

            openUserfile("ALLterago")
        
            isCommandComplete = True
#-------------------------------------------------------------
        elif startcommand == "iddqd":
            print("Launching " + startcommand)  
            isCommandComplete = True
#-------------------------------------------------------------
        elif startcommand == "TKinter":
            print("Launching " + startcommand)   #тестю ткинтер

            isCommandComplete = True
#-------------------------------------------------------------
        elif startcommand == "gacha":
            print("Launching " + startcommand) 

            isCommandComplete = True
#-------------------------------------------------------------
        elif startcommand == "exit":
            print("Bye...")
            isCommandComplete = True
            run = False
#-------------------------------------------------------------        
        else:
            print("Wrong command")
            isCommandComplete = True
            