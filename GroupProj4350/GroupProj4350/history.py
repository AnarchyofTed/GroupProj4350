def History(customer, server):
    print("---Your Order History---")

    cust = server.sqlSelectPrint("SELECT * FROM orders")# WHERE customer_id= '%s'" %customer.id[2:-1])
    cust = cust.fetchall()
    print("--Your Orders--")
    for c in cust:
        print("-------------------------")
        print("Amount: " + str(c[5]))
        print("   Date: " + c[4])
        
