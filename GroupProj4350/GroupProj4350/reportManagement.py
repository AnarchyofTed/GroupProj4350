#This is a grabs different reports

def ReportManagement(server):
    print("This is Report Management")
    while 1:
        print("1: Value of active orders")
        print("2: Value of cancelled orders")
        print("3: Value of non-active orders")
        print("4: Value of all orders")
        print("5: Value of all non-cancelled orders")
        print("6: Value of the Store sales")
        print("7: Value of employee sales")
        print("8: Go Back")
        n = input()
        try:
            n=int(n)
        except:
            print("Please enter a valid option")
            continue
        if n==8:
            break
        total=float()
        active="active='yes'"
        #grabs the store reports
        if n==6:
            row=server.command("SELECT store_name, store_sales FROM store")
            print(" name    ,Value")
            for x in row:
                temp=str(x).split(",")
                temp[0]=temp[0][2:-1]
                temp[1]=temp[1][10:-3]
                print(temp)
        #Gets the employee reports
        if n==7:
            row=server.command("SELECT employee_name, employee_sales FROM employees")
            print(" name    ,Value")
            for x in row:
                temp=str(x).split(",")
                temp[0]=temp[0][1:-1]
                temp[1]=temp[1][10:-3]
                print(temp)
        #All of these change the options on the select to grab a report
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
        