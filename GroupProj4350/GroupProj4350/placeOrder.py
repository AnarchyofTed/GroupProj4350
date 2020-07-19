def PlaceOrder():
    while 1:
        print("1. Browse Inventory")
        print("2. Search Inventory")
        print("3. Go Back")
        userInp = int(input())
        if userInp == 1:
            print("Browsing inventory")
        elif userInp == 2:
            print("Search Inv")
        elif userInp == 3:
            break
        else:
            print("Not an option!")