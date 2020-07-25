from datetime import datetime
from datetime import timedelta
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
        print("3. View Cart")
        print("4. Check Out")
        print("5. Go Back")
        userInp = input()
        try:
            userInp=int(userInp)
        except:
            print("Please enter a valid option")
            continue
        if userInp == 1:
            print("Browsing inventory")
            row=server.command("SELECT  * FROM item")
            number=0
            processed=list()
            for x in row:
                temp=str(x).split(",")
                tempId=temp[0][4:-2]
                tempDescrip=temp[2][2:-1]
                tempQuan=temp[3][:-1]
                tempPrice=temp[1][10:-2]
                temp=[tempId,tempPrice,tempDescrip,tempQuan]
                processed.append(temp)               
                print(f"{number}) {tempDescrip} - {tempQuan} -- ${tempPrice}")
                number=number+1
            row=server.command("SELECT * FROM full_set")
            holder=list()
            for x in row:
                temp=str(x).split(",")
                temp[0]=temp[0][4:-2]
                temp[1]=temp[1][2:-2]
                holder.append(temp)  
            for x in holder:
               
                row=server.command("SELECT * FROM set_item WHERE set_id='"+x[0]+"';")
                tempIdAndCount=list()
                for y in row:                   
                    tempIdAndCount.append((str(y[1][2:-1]),y[2]))
                total=0
                for y in tempIdAndCount:
                    t1, t2=y
                    row=server.command("SELECT item_price FROM item WHERE item_id='"+t1+"';")
                    t3=float()
                    for z in row:
                        t3=str(z)
                        t3=t3[10:-4]
                        t3=float(t3)
                    total=total+(t3*t2)
                    total=round(total, 2)
                print(f"({number}) - {x[1]} -- ${total}")
                tempAll=[x[0],total,x[1],2]
                processed.append(tempAll)
                number=number+1
            print("-------------------------------------")
            Item=input("Do you want to add one of items to the order(Enter y for yes or n for no): ")
            while Item !='n':
                tempItem=input("Enter the Item number you want to add: ")
                try:
                    tempItem=int(tempItem)
                except:
                    print("Please enter a valid option")
                    continue
                if tempItem < number:
                    temp=processed[tempItem]
                    if int(temp[3]) > 0:
                        cost=cost+float(temp[1])
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
                if customerName == 'NULL' and employee == 'NULL':
                    print("Order has been placed!")
                else:
                    while 1:
                        print("1: Master Card")
                        print("2: Visa")
                        if employee != 'NULL':
                            print("3: Cash")
                        print("4: Go Back")
                        menu=input()
                        try:
                            menu=int(menu)
                        except:
                            print("Please enter a valid option")
                            continue
                        card=""
                        if menu == 1 or menu == 2:
                            if menu == 2:
                                card = "'visa'"
                            if menu == 1:
                                card="'mc'"
                            payment=input("Please enter a valid credit card number: ")
                            #payment="1111111111111111111111111111111111"
                            while len(str(payment))<16:
                                print("number was invalid")
                                payment=input("Please enter a valid credit card number: ")
                        if menu == 3:
                            card="'cash'"
                        if menu == 4:
                            break
                  
                        StringCommand="INSERT INTO orders(customer_id, employee_id, store_id, order_date, order_price,payment_type, delivery_date, active) VALUES("
                    
                        nowDate=str(datetime.date(datetime.now())+timedelta(days=10))
                        StringCommand=StringCommand+customerName+" ,"+ employee+","+"(SELECT store_id FROM store WHERE store_name ="+store+") , '"+str(datetime.date(datetime.now()))+"' , "+str(cost)+", "+card+", '"+nowDate+"', 'yes');"
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