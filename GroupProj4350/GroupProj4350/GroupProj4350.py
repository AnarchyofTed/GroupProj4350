from customerFunction import *  
from employeeFunction import *
from newUser import *
from server import *

#serverName= input('Enter the server name: ')
#databaseName=input('Enter the database name: ')
MainServer=server('Rxlbcoxlt\mssqlserver01','master')
while 1:
	print("Please Sign In")
	print("1. Customer (Online Mode)")
	print("2. Employee (Store Mode)")
	print("3. Create New Customer (New Employees must be created by management)")
	n = int(input())
	if n is 1:
		print("Welcome to Lego Store Online")
		print("Please Sign In")
		Uname = input("UserName : ")		
		Pword = input("Password : ")
		customer = Customer(MainServer, Uname, Pword)


	elif n is 2:
		Employee()

	elif n is 3:		
		NewUser()

	else:
		print("Oops that's not an option!")


