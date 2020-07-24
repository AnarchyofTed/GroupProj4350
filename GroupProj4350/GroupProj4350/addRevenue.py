def addRevenue(amount, server, store): 
    totrev = server.sqlSelect("SELECT store_sales FROM store WHERE store_name = %s;"%store) 
    totrev = totrev.fetchone()
    flrev = float(totrev[0])
    flrev = flrev + amount
    stringcommand = "UPDATE store SET store_sales = "
    stringcommand = stringcommand+str(flrev)+ " WHERE store_name = "+store+";"
    store = server.sqlInsert(stringcommand)
   
def addSales(amount, server, employee):
    totrev = server.sqlSelect("SELECT employee_sales FROM employees WHERE employee_id = %s;"%employee) 
    totrev = totrev.fetchone()
    flrev = float(totrev[0])
    flrev = flrev + amount
    stringcommand = "UPDATE employees SET employee_sales = "
    stringcommand = stringcommand+str(flrev)+ " WHERE employee_id = "+employee+";"
    store = server.sqlInsert(stringcommand)

def returnSales(amount, server, store):
    totrev = server.sqlSelect("SELECT store_sales FROM store WHERE store_id = %s;"%store) 
    totrev = totrev.fetchone()
    flrev = float(totrev[0])
    flrev = amount - flrev
    stringcommand = "UPDATE store SET store_sales = "
    stringcommand = stringcommand+str(flrev)+ " WHERE store_id = "+store+";"
    store = server.sqlInsert(stringcommand)

def orderItems(itemList, server):
    for i in itemList:
        stringcommand = "UPDATE item SET quantity_inStock = quantity_inStock + 1 WHERE item_description = '"+i+"'"
        server.sqlInsert(stringcommand)
