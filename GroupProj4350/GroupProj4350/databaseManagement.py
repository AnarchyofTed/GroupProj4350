
#This is used for generalizing updates to the server
def UpdateServer(server, table, field, newItem, ID, SpecificId):
    InsertString="UPDATE "+table+" SET "+field+"='"+newItem+"' WHERE "+ID+"='"+SpecificId+"';"
    #print(InsertString)
    server.command(InsertString)
    server.command("COMMIT TRANSACTION")



def DatabaseManagement(server, access):
    print("This is Database Management")

    #This checks if the employee has an valid access level
    if access<2:
        print("Not high enough access level")
        return
    while 1:
        print("1: Customer Management")
        print("2: Employee Management")
        print("3: Go Back")
        n = input()
        try:
            n=int(n)
        except:
            print("Please enter a valid option")
            continue
        if n>3:
            print("please enter a valid input")
            continue
        if n==3:
            break
        if n==2:
            #Pulls the employee table
            row=server.command("SELECT * FROM employees")
            number=0
            holder=list()
            for x in row:
                #Formats table
                temp=str(x).split(",")
                #ID
                temp[0]=temp[0][4:-2]
                #name
                temp[1]=temp[1][2:-1]
                #Username
                temp[2]=temp[2][2:-1]
                #password
                temp[3]=""
                #Store
                temp[4]=temp[4][2:-1]
                #access
                temp[5]=temp[5][2:-1]
                #phone
                temp[7]=temp[7][2:-2]
                print(str(number)+":   "+str(temp[1:]))
                #Stores each row of the table locally
                holder.append(temp)
                number=number+1
            while 1:
                m=input("Select which to edit(enter "+str(number)+" escape): ")
                try:
                    m=int(m)
                except:
                    print("Please enter a valid option")
                    continue
                if m == number:
                    break
                if m>number:
                    print("please enter a valid input")
                    continue
                #Menu for the employees
                while 1:
                    #Grabs employee Id
                    Id=holder[m][0]
                    print("What do you want to edit")
                    print("1: Name")
                    print("2: Username")
                    print("3: Password")
                    print("4: Store Preference")
                    print("5: Access Level")
                    print("6: Phone Number")
                    print("7: Go Back")
                    t=input()
                    #This are used to changes the paramaters of the update function
                    ServerInput=''
                    WhatToChange=''
                    try:
                        t=int(t)
                    except:
                        print("Please enter a valid option")
                        continue
                    if t>7:
                        print("Please enter a valid input")
                        continue
                    if t==7:
                        break
                    if t==1:
                        WhatToChange='employee_name'
                        ServerInput=input("Enter a new name: ")
                    if t==2:
                        WhatToChange='employee_username'
                        ServerInput=input("Enter a new Username: ")
                    if t==3:
                        WhatToChange='employee_password'
                        ServerInput=input("Enter a new Password: ")
                    if t==4:
                        WhatToChange='employee_storePreference'
                        ServerInput=input("Enter a new Store: ")
                    if t==5:
                        WhatToChange='employee_accessLevel'
                        ServerInput=input("Enter a new Access Level: ")
                    if t==6:
                        WhatToChange='employee_phone'
                        ServerInput=input("Enter a new Phone Number: ")
                    try:
                        UpdateServer(server,"employees",WhatToChange,ServerInput,"employee_id",Id)
                    except:
                        print("Could not update server")
        if n==1:
            row=server.command("SELECT * FROM customers")
            number=0
            holder=list()
            #Formates customers
            for x in row:
                temp=str(x).split(",")
                temp[0]=temp[0][4:-2]
                temp[1]=temp[1][2:-1]
                temp[2]=temp[2][2:-1]
                temp[3]=temp[3][2:-1]
                temp[4]=temp[4][2:-1]
                temp[5]=""
                print(str(number)+":   "+str(temp[1:]))
                holder.append(temp)
                number=number+1
            while 1:
                m=input("Select which to edit(enter "+str(number)+" escape): ")
                try:
                    m=int(m)
                except:
                    print("Please enter a valid option")
                    continue
                if m == number:
                    break
                if m>number:
                    print("please enter a valid input")
                    continue
                #All most a repeat of the employee menus
                while 1:
                    Id=holder[m][0]
                    print("What do you want to edit")
                    print("1: Name")
                    print("2: Phone Number")
                    print("3: Store Preference")
                    print("4: Username")
                    print("5: Password")
                    print("6: Go Back")
                    t=input()
                    ServerInput=''
                    WhatToChange=''
                    try:
                        t=int(t)
                    except:
                        print("Please enter a valid option")
                        continue
                    if t>6:
                        print("Please enter a valid input")
                        continue
                    if t==6:
                        break
                    if t==1:
                        WhatToChange='customer_name'
                        ServerInput=input("Enter a new name: ")
                    if t==2:
                        WhatToChange='customer_phone'
                        ServerInput=input("Enter a new number: ")
                    if t==3:
                        WhatToChange='customer_storePreference'
                        ServerInput=input("Enter a new Store: ")
                    if t==4:
                        WhatToChange='customer_username'
                        ServerInput=input("Enter a new Username: ")
                    if t==5:
                        WhatToChange='customer_password'
                        ServerInput=input("Enter a new Password: ")
                    try:
                        UpdateServer(server,"customers",WhatToChange,ServerInput,"customer_id",Id)
                    except:
                        print("Could not update server")
