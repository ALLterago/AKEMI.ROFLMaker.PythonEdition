from devTest import SumInt
from login import user



Title = "Akemi\nROFL\nMaker\nPython\nEdition"
TitleLine = "_______________________________________________________________________"
print(TitleLine)
print(Title) #enter block
print("\nAvailable commands:")
print("devTest - testing/debug\nTKinter - GUI stuff\nexit - guess what it does by yourself\ngacha - simple gacha game(main feature by now)\n")



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

