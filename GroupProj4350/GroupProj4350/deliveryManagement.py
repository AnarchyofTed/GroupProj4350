from datetime import datetime

def DeliveryManagement(server):
    print("This is DeliveryManagement")
    while 1:
        print("1: Show Active Orders")
        print("2: Show Inactive Orders")
        print("3: Go Back")
        n = input()
        try:
            n=int(n)
        except:
            print("Please enter a valid option")
            continue
        if n==3:
            break
        if n==1:
            row=server.command("SELECT order_id, customer_name, employee_name, store_name, order_date, order_price, payment_type, delivery_date, active  FROM  ((orders LEFT JOIN customers ON orders.customer_id=customers.customer_id) LEFT JOIN employees ON orders.employee_id=employees.employee_id) LEFT JOIN store ON orders.store_id=store.store_id WHERE active='yes';")
        if n==2:
            row=server.command("SELECT order_id, customer_name, employee_name, store_name, order_date, order_price, payment_type, delivery_date, active  FROM  ((orders LEFT JOIN customers ON orders.customer_id=customers.customer_id) LEFT JOIN employees ON orders.employee_id=employees.employee_id) LEFT JOIN store ON orders.store_id=store.store_id WHERE active='no';")
        print("----------------------------------------------")
        holder=list()
        number=0
        for x in row:
            temp=str(x).split(",")
            #order ID
            temp[0]=temp[0][4:-2]
            #Customer ID
            if temp[1] != ' None':
                temp[1] = temp[1][2:-1]
            else:
                temp[1]="NULL"
            #Employee ID
            if temp[2] != ' None':
                temp[2]=temp[2][2:-1]
            else:
                temp[2]="NULL"
            #Store ID
            temp[3]=temp[3][2:-1]
            #Order Date
            temp[4]=temp[4][2:-1]
            #Cost
            temp[5]=temp[5][10:-2]
            #payment
            temp[6]=temp[6][2:-1]
            #Delivery Date
            if temp[7]==" None":
                temp[7]="NULL"
            else:
                temp[7]=temp[7][2:-1]
            #Activity
            temp[8]=temp[8][2:-2]
            holder.append(temp)
            print(str(number)+":     "+str(temp[1:]))
            number=number+1

        while 1:
            m=input("Select the order you want to edit(type "+str(number)+" to exit): ")
            try:
                m=int(m)
            except:
                print("Please enter a valid option")
                continue
            if m==number:
                break
            if m > number:
                print("Please enter a valid number")
                continue
            else:
                while 1:
                    print("which item do you want to edit")
                    temp=holder[m]
                    print("1: Edit Delivery date ")
                    print("2: Edit payment method ")
                    if n==1:
                        print("3: Do you wish to cancel")
                    print("4: Go Back")
                    t=input()
                    try:
                        t=int(t)
                    except:
                        print("Please enter a valid option")
                        continue
                    if t==1:
                        date=str(input("Enter date in the format year(last 2 digits), month, day   **/**/**: "))
                        date=datetime.strptime(date, "%y/%m/%d")
                        row=server.command("UPDATE orders SET delivery_date='"+str(date)+"' WHERE order_id='"+temp[0]+"';")
                        row=server.command("COMMIT TRANSACTION")
                    elif t==2:
                        pay=str(input("Enter the new payment type: "))
                        row=server.command("UPDATE orders SET payment_type='"+pay+"' WHERE order_id='"+temp[0]+"';")
                        row=server.command("COMMIT TRANSACTION")
                    elif t==3:
                        row=server.command("UPDATE orders SET active='no' WHERE order_id='"+temp[0]+"';")
                        row=server.command("COMMIT TRANSACTION")
                        print("Order was cancelled")
                    elif t==4:
                        break
            