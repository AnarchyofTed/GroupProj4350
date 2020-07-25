from customerFunction import *  
from employeeFunction import *
from newUser import *
from server import *
from Populate_Server import *
from addRevenue import *

t=0

while t==0:
	#serverName= input('Enter the server name: ')
	serverName="DESKTOP-LPJK5QO\SCHOOL"
	#databaseName=input('Enter a valid database name: ')
	databaseName="Legos"
	try:
		MainServer=server(serverName, databaseName)
		t=1
	except:
		print("could not connect")
		t=0
###Blakes Test ###
#serverName='RXLBCOXLT\BLAKESMSQLSERVER'
#databaseName='Lego'
MainServer=server(serverName, databaseName)
first=input("Do you need to create the tables for the first time?y for yes, n for no: ")
if first=='y' or first=='Y':
	MakeDataBase(serverName,databaseName)
	

#Jacobs Test Function

while 1:
	print("Please Sign In")
	print("1. Customer (Online Mode)")
	print("2. Employee (Store Mode)")
	print("3. Create New Customer (New Employees must be created by management)")
	print("4. Exit")
	n = input()
	try:
		n=int(n)
	except:
		print("Please enter a valid option")
		continue
	if n == 1:
		print("Welcome to Lego Store Online")
		print("Please Sign In")
		Uname = "MrBlake123"
		Pword = "123456"
		#Uname = input("UserName : ")
		#Pword = input("Password : ")
		customer = Customer(MainServer, Uname, Pword)


	elif n == 2:
		print("Employee's Offline Mode")
		print("Please Sign In")
		Uname = "Mr.Potter"
		Pword = "password1"
		#Uname = input("UserName : ")		
		#Pword = input("Password : ")
		employee = Employee(MainServer, Uname, Pword)
		

	elif n == 3:		
		NewUser(MainServer)

	elif n==4:
		MainServer.endConnection()
		break

	else:
		print("Oops that's not an option!")


