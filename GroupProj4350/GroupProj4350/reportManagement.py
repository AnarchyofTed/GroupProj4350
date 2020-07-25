def ReportManagement(server):
    print("This is Report Management")
    while 1:
        print("1: Value of active orders")
        print("2: Value of cancelled orders")
        print("3: Value of non-active orders")
        print("4: Value of all orders")
        print("5: Value of all non-cancelled orders")
        print("6: Go Back")
        n = input()
        try:
            n=int(n)
        except:
            print("Please enter a valid option")
            continue
        if n==6:
            break
        total=float()
        active="active='yes'"
        if n==1:
            active="active='yes'"
        if n==2:
            active="active='can'"
        if n==3:
            active="NOT active='yes'"
        if n==4:
            active="NOT active='NULL'"
        if n==5:
            active="NOT active='can'"
        row=server.command("SELECT order_price FROM orders WHERE "+active+";")
        for x in row:
            temp=str(x)[10:-4]
            total=total+float(temp)
            total=round(total, 2)
        print("The total cost of your request is "+str(total))
        