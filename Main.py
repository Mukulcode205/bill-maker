import pyautogui
with open("Setup.txt", "a") as f:
    f.write("-------------Dmart Enterprises-------------")
    f.write("\n|")
    f.write("Item Name")
    f.write("    Item Cost")
    f.write("     Item Quantity")
    f.write("     Item Amount  |")
while True:
    item = input("Enter item name: ")
    cost = float(input("Enter item cost: "))
    quantity = float(input("Enter item quantity: "))
    blank = int(input("You can enter 000 to obtain bill.\nElse press enter.\n>>>"))
    total = quantity*cost
    cup = str(total)
    with open("setup.txt", "a") as a:
        a.write("\n|")
        a.write(str(item))
        v = int(len(str(item)))
        a.write(" "*(14-v))
        a.write(str(cost))
        v2 = int(len(str(cost)))
        a.write(" "*(14-v2))
        a.write(str(quantity))
        v3 = int(len(str(quantity)))
        a.write(" "*(17-v3))
        a.write(str(cup))
        v4 = int(len(cup))
        a.write(" "*(14-v4))
        a.write("|")
        if blank == 000:
            with open("Setup.txt", "r") as d:
                content = d.read()
                print(content)
                break
        else:
            print("Undefined function")
            continue