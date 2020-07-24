from datetime import datetime
from addRevenue import *
def PlaceOrder(customerName,server):
    cart=list()
    cartIds=list()
    cost=0
    while 1:     
        print("1. Browse Inventory")
        print("2. Search Inventory")
        print("3. View Cart")
        print("4. Check Out")
        print("5. Go Back")
        userInp = int(input())
        if userInp == 1:
            print("Browsing inventory")
            print("item number, Price, Description, Amount in Stock")
            row=server.command("SELECT  * FROM item")
            number=0
            processed=list()
            for x in row:
                temp=str(x).split(",")
                processed.append(temp)
                print(str(number)+":   "+temp[1][10:-2]+" , "+temp[2]+" , "+temp[3][:-1])
                number=number+1
            Item=input("Do you want to add one of items to the order(Enter y for yes or n for no): ")
            while Item !='n':
                tempItem=int(input("Enter the Item number you want to add: "))
                if tempItem < number:
                    temp=processed[tempItem]
                    if int(temp[3][:-1]) > 0:
                        cost=cost+float(temp[1][10:-2])
                        cost=round(cost, 2)
                        cartIds.append(temp[0])
                        cart.append(temp[2])
                    else:
                        print("Sorry the Item is out of stock")
                Item=input("Do you want to add another item to the order(Enter y for yes or n for no): ")
        elif userInp == 2:
            print("Search Inv")
            Item=input("Enter the description of the Item you are looking for: ")
            print("item number, Price, Description, Amount in Stock")
            StringCommand="SELECT * FROM item WHERE item_description="+"'"+str(Item)+"'"+";"
            row=server.command(StringCommand)
            if row == None:
                print("could not find item")
            else:
                for x in row:
                    holder=x
                    temp=str(x).split(",")
                    print(temp[1:])
                tempInput=input("Would you like to add this item to your order(y for yes, n for no)?: ")
                if tempInput == 'y':
                    temp=str(holder).split(",")
                    cost=cost+float(temp[1][10:-2])
                    cost=round(cost, 2)
                    cartIds.append(temp[0])
                    cart.append(temp[2])
                    
        elif userInp == 3:
            print(cart)
            print("Total Cost : "+str(cost))
        elif userInp ==4:
            #payment=input("Please enter a valid credit card number: ")
            payment="1111111111111111111111111111111111"
            while len(str(payment))<16:
                print("number was invalid")
                payment=input("Please enter a valid credit card number: ")
            StringCommand="INSERT INTO orders(customer_id, employee_id, store_id, order_date, order_price) VALUES("
            customerInfo=server.command("SELECT * FROM customers WHERE customer_username= '%s'"% customerName)
            for x in customerInfo:
                customer=str(x).split(",")
            #print(x)
            StringCommand=StringCommand+customer[0][3:-1]+" ,NULL ,"+"(SELECT store_id FROM store WHERE store_name ="+customer[3]+") , '"+str(datetime.date(datetime.now()))+"' , "+str(cost)+");"
            #print(StringCommand)
            server.command(str(StringCommand))
            server.command("COMMIT TRANSACTION")
            addRevenue(cost, server, customer[2], bool(1))
        elif userInp == 5:
            break
        else:
            print("Not an option!")