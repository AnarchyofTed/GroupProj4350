from customerFunction import *  
from employeeFunction import *
from newUser import *
while 1:
	print("Please Sign In")
	print("1. Customer (Online Mode)")
	print("2. Employee (Store Mode)")
	print("3. Create New Customer (New Employees must be created by management)")
	n = int(input())
	if n is 1:
		Customer()


	elif n is 2:
		Employee()

	elif n is 3:		
		NewUser()

	else:
		print("Oops that's not an option!")

