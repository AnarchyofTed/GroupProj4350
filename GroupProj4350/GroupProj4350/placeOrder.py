def PlaceOrder(server):
    while 1:
        print("1. Browse Inventory")
        print("2. Search Inventory")
        print("3. Go Back")
        userInp = int(input())
        if userInp == 1:
            print("Browsing inventory")
            print("item number, Price, Description, Amount in Stock")
            row=server.command("SELECT item_price, item_description, quantity_inStock FROM item")
            number=0
            for x in row:
                print(str(number)+":   "+str(x))
                number=number+1
            Item=input("Do you want to add one of items to the order(Enter the item you want to add or type n for no): ")
            while Item !='n':
                Item=input("Do you want to add another item to the order(Enter the item you want to add or type n for no): ")
        elif userInp == 2:
            print("Search Inv")
            Item=input("Enter the description of the Item you are looking for: ")
            print("item number, Price, Description, Amount in Stock")
            StringCommand="SELECT item_price, item_description, quantity_inStock FROM item WHERE item_description="+"'"+str(Item)+"'"+";"
            row=server.command(StringCommand)
            if row == None:
                print("could not find item")
            else:
                for x in row:
                    print(str(x))
        elif userInp == 3:
            break
        else:
            print("Not an option!")