from placeOrder import *
def OrderManagement(server, pref):
    print("----Order Management---")
    while 1:
        print("1) Order more Sets or Bricks")
        print("2) Reorder")
        print("3) Stop Order")
        print("4) Returns")
        print("5) Go Back")
        n = int(input())
        if n == 1:
            PlaceOrder('NULL', 'NULL', server, pref)       
        elif n ==2:
            print("----All Orders----")

            stringcommand = "SELECT * FROM orders;"
            orders = server.sqlSelect(stringcommand)
            orders = orders.fetchall()
            it = 0
            for o in orders:
                it = it+1
                print(f"{it}) Date: {o[4]} Total: {o[5]} Active: {o[8]}")
            while 1:
                print("Which one would you like to reorder? (Press 0 to go back)")
                n = int(input())
                if n >0 and n <= it:
                    it = n-1
                    print("Reordered!")
                    customerName = orders[it][1]
                    employee = orders[it][2]
                    store = orders[it][3]
                    if customerName != None:
                        customerName=customerName[1:]
                    else:
                       customerName = 'NULL'
                    if store != None:
                        store = store[1:]
                    else:
                        store = 'NULL'
                    if employee != None:
                        employee=employee[1:]
                    else:
                        employee = 'NULL'
                    cost = float(orders[it][5])
                    StringCommand="INSERT INTO orders(customer_id, employee_id, store_id, order_date, order_price,payment_type, delivery_date, active) VALUES("            
                    nowDate=str(datetime.date(datetime.now())+timedelta(days=10))
                    StringCommand=StringCommand+customerName+" ,"+ employee+","+store+", '"+str(datetime.date(datetime.now()))+"' , '"+str(cost)+"', '"+orders[it][6]+"', '"+nowDate+"', 'yes');"
                    server.command(str(StringCommand))   
                    server.command("COMMIT TRANSACTION")
                    break
                if n == 0:
                    break
                else:
                    print("Not a Valid Option")
            break
        elif n == 3:
            print("----All Active Orders----")

            stringcommand = "SELECT * FROM orders WHERE active = 'yes';"
            orders = server.sqlSelect(stringcommand)
            orders = orders.fetchall()
            it = 0
            for o in orders:
                it = it+1
                print(f"{it}) Date: {o[4]} Total: {o[5]}")
            while 1:
                print("Which one would you like to Stop? (Press 0 to go back)")
                n = int(input())
                if n >0 and n <= it:
                    it = n-1
                    print("Order Stopped and Removed!")
                    order= orders[it][0]
                    order = order[1:]
                    stringcommand = "DELETE FROM orders WHERE order_id = "+order+";"
                    server.sqlInsert(stringcommand)
                    break
                if n == 0:
                    break
                else:
                    print("Not a Valid Option")
            break
        elif n == 4:
            print("----All Orders----")
            stringcommand = "SELECT * FROM orders;"
            orders = server.sqlSelect(stringcommand)
            orders = orders.fetchall()
            it = 0
            for o in orders:
                it = it+1
                print(f"{it}) Date: {o[4]} Total: {o[5]} Active: {o[8]}")
            while 1:
                print("Which one is being returned? (Press 0 to go back)")
                n = int(input())
                if n >0 and n <= it:
                    it = n-1
                    order= orders[it][0]
                    order = order[1:]
                    stringcommand = "UPDATE orders SET active = 'RET' WHERE order_id = "+order+";"
                    server.sqlInsert(stringcommand)
                    cost = float(orders[it][5])
                    store = orders[it][3]
                    store = store[1:]
                    returnSales(cost, server, store)
                    break
            break
        elif n == 5:
            break
        else:
            pass


    
