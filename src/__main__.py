from devTest import SumInt
from login import user,loginMeth,registerMeth

print("Type \"login\" to log in")
print("Type \"register\" to register a new user")
loginState = input()

if loginState == "login":
    loginMeth(input("Enter your username:"),input("Enter your password:"))

elif loginState == register:
    registerMeth(input("Enter your username:"),input("Enter your password:"))

print("\n")
Title = "Akemi\nROFL\nMaker\nPython\nEdition"
TitleLine = "_______________________________________________________________________"
print(TitleLine)
print(Title) #enter block
print("\nAvailable commands:")
print("devTest - testing/debug")
print("TKinter - GUI stuff")
print("gacha - simple gacha game(main feature by now)")
print("exit - guess what it does by yourself")


swcompl = int(0) 

while swcompl == 0 :
    startcommand = input()           
    if startcommand == "devTest":
        print("Launching " + startcommand)   #всякая дебуг шляпа и тест фич перед внедрением
        print(SumInt(int(input("Input first int number:")),int(input("Input second int number:"))))
        swcompl=int(1)

    elif startcommand == "iddqd":
        print("Launching " + startcommand)   #тестю запуск кода из внешних файлов. ссылка на ориг: https://github.com/Pink-Silver/PyDoom
        swcompl=int(1)

    elif startcommand == "TKinter":
        print("Launching " + startcommand)   #тестю ткинтер

        swcompl=int(1)

    elif startcommand == "exit":
        print("Bye...")
        swcompl=int(1)
        
    else:
        print("Wrong command")

