def EmployeeSale(server):
    while 1:
        print("---Sales Page---")
        print("1. Browse Catalogy")
        print("2. Search For Item")
        try:
            n =  int(input())
            if n == 1:
                BrowseCatalog(server)
            elif n == 2:
                print("whh")
            elif n == 3:
                break
            else:
                print("Not a valid osption!")
        except:
            print("Except : Not a valid option!")


def BrowseCatalog(s):
    itemlist = []
    currentlist = []
    ordertotal = 0.0
    while 1:
        items = s.sqlSelect("SELECT * FROM item")
        itemlist.clear()
        for row in items:           
            itemlist.append(row)
            print(f"{len(itemlist)}. {itemlist[len(itemlist)-1][2]} -- ${itemlist[len(itemlist)-1][1]}")
        print("--Select an item to add to an order--")
        print("Type 0 when you're ready to finish the sale.")
        selection = int(input())
        if selection in range(1,10000):
            ordertotal = ordertotal + 1.2#itemlist[selection-1][1]
            currentlist.append(itemlist[selection-1])
        elif selection == 0:
            break
        else :
            break
        print("{:.2}".format(ordertotal))
