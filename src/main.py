print("Akemi\nROFL\nMaker\nPython\nEdition") #enter block
print("\nAvailable commands:")
print("devTest - testing/debug\nTKinter - GUI stuff\n")


swcompl = int(0)

while swcompl == 0 :
    startcommand = input()
    if startcommand == "devTest":
        print("Launching " + startcommand)
        swcompl=int(1)
    elif startcommand == "iddqd":
        print("Launching " + startcommand)
        swcompl=int(1)
    elif startcommand == "TKinter":
        print("Launching " + startcommand)
        swcompl=int(1)
    else:
        print("Wrong command")