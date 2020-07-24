from datetime import date
import sys


def EmployeeSale(server, emp):
    while 1:
        print("---Sales Page---")
        print("1. Browse Catalogy")
        print("2. Search For Item")
        try:
            n =  int(input())
            if n == 1:
                BrowseCatalog(server, emp)
            elif n == 2:
                print("whh")
            elif n == 3:
                break
            else:
                print("Not a valid osption!")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise


def BrowseCatalog(s, e):
    itemlist = []
    addeditems = []
    itemcount = []
    ordertotal = 0.00
    
    items = s.sqlSelect("SELECT * FROM item")
    itemlist.clear()
    for row in items:           
        itemlist.append(row)
        print(f"{len(itemlist)}. {itemlist[len(itemlist)-1][2]} -- ${itemlist[len(itemlist)-1][1]}")
    
    while 1:
        if len(addeditems) != 0:
            print("")
            print('Total : $' + format(ordertotal, ',.2f'))
            count =0
            for i in addeditems:           
                print(f"{count+1}. {addeditems[count][2]} -- ${addeditems[count][1]}")
                count = count + 1
        print("--Select an item to add to an order--")
        print("Type 0 when you're ready to finish the sale.")
        selection = int(input())
        if selection in range(1,10000):
            max = itemlist[selection-1][3]
            while 1:
                print(f"How many? Max = {max}")
                qselection = int(input())
                if qselection in range(1,max):
                    ordertotal = ordertotal + (float(itemlist[selection-1][1]) * qselection)
                    addeditems.append(itemlist[selection-1])
                    itemcount.append(qselection)
                    break
                else:
                    print("Not a valid option!")
        elif selection == 0:
            while 1:
                 print('Total : $' + format(ordertotal, ',.2f'))
                 print('1. Card')
                 print('2. Cash')
                 n = int(input())
                 if n == 1:
                     print("Card No: ")
                     str(input())
                     print("Enjoy your Lego!!")  
                     if e.preference == 'Mrs. LegoTron':
                         store = s.sqlSelect("SELECT * FROM store WHERE store_name = 'Mrs.LegoTron';")
                     else:
                         store = s.sqlSelect("SELECT * FROM store WHERE store_name = '%s';"% e.preference)
                     store = store.fetchone()
                     o = float("{:.2f}".format(ordertotal))
                     now = date.today()
                     formatted_date = now.strftime('%Y-%m-%d')                     
                     thisstring='%s' % e.id
                     thisstring = thisstring[1:]
                     storestring ='%s' % store[0]
                     storestring = storestring[1:]
                     s.sqlInsert("INSERT INTO orders (employee_id, store_id, order_date, order_price) VALUES(%s, %s, '%s', %f)" %(thisstring, storestring, formatted_date, o))
                     addSales(o, s,thisstring)
                     break
                 if n == 2:
                     print("Enjoy your Lego")
                 else:
                     print("Not a valid Option!")
            break
        else :
            break
