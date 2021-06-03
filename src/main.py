print("Akemi\nROFL\nMaker\nPython\nEdition") #enter block
print("\nAvailable commands:")
print("devTest - testing/debug\nTKinter - GUI stuff\n")


swcompl = int(0) 

while swcompl == 0 :
    startcommand = input()           
    if startcommand == "devTest":
        print("Launching " + startcommand)   #всякая дебуг шляпа и тест фич перед внедрением
        swcompl=int(1)
    elif startcommand == "iddqd":
        print("Launching " + startcommand)   #тестю запуск кода из внешних файлов. ссылка на ориг: https://github.com/Pink-Silver/PyDoom
        swcompl=int(1)
    elif startcommand == "TKinter":
        print("Launching " + startcommand)   #тестю ткинтер
        swcompl=int(1)
    else:
        print("Wrong command")