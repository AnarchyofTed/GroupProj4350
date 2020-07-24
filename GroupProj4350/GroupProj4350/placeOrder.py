from datetime import datetime
from addRevenue import *
def PlaceOrder(customerName,employee,server,store):
    if customerName != "NULL":
        customerName=customerName[1:]
    if store != "NULL":
        store ="'"+store+"'"
    if employee != "NULL":
        employee=employee[1:]
    cart=list()
    cartIds=list()
    cost=0
    while 1:     
        print("1. Browse Inventory")
        print("2. Search Inventory")
        print("3. Veiw Cart")
        print("4. Check Out")
        print("5. Go Back")
        userInp = int(input())
        if userInp == 1:
            print("Browsing inventory")
            #print("item number, Price, Description, Amount in Stock")
            row=server.command("SELECT  * FROM item")
            number=0
            processed=list()
            for x in row:
                temp=str(x).split(",")
                processed.append(temp)
                print(str(number)+":   "+temp[2][2:-1]+", Quanity: "+temp[3][:-1]+", Price: "+temp[1][10:-2])
                number=number+1
            row
            print("-------------------------------------")
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
                        print(f"({temp[2]} - {temp[3]} -- ${cost}")
                        print("Item Added to Cart")
                    else:
                        print("Sorry the Item is out of stock")
                        print("-------------------------------------")
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
            print("-------------------------------------")
            print(cart)
            print("-------------------------------------")
            print("Total Cost : "+str(cost))
        elif userInp ==4:
            if cart == []:
                print("Cart is empty")
            else:
               # payment=input("Please enter a valid credit card number: ")
                payment="1111111111111111111111111111111111"
                while len(str(payment))<16:
                    print("number was invalid")
                    payment=input("Please enter a valid credit card number: ")
                StringCommand="INSERT INTO orders(customer_id, employee_id, store_id, order_date, order_price) VALUES("
            
                StringCommand=StringCommand+customerName+" ,"+ employee+","+"(SELECT store_id FROM store WHERE store_name ="+store+") , '"+str(datetime.date(datetime.now()))+"' , "+str(cost)+");"
               # print(StringCommand)
                server.command(str(StringCommand))   
                server.command("COMMIT TRANSACTION")
                addRevenue(cost, server, store)
                if employee != "NULL":
                    addSales(cost, server, employee)
                print("Have Fun!")
                break
        elif userInp == 5:
            break
        else:
            print("Not an option!")