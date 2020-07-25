from employeeSale import *
from placeOrder import *
from orderManagement import *
from databaseManagement import *
from reportManagement import *
from deliveryManagement import *
import sys

class Employee:
	
	def __init__(self,server, uname, pword):
		self.id=''
		self.name =''
		self.phone=''
		self.preference=''
		self.accessLevel=0
		self.sales=0.0
		self.username=uname
		self.password=pword
		self.EmployeeLogin(server)


	def EmployeeLogin(self, server):
		emp = server.sqlSelect("SELECT * FROM employees WHERE employee_username= '%s'"% self.username)
		emp = emp.fetchone()
		if emp is None:
			print("Invalid Username")
		elif emp[3] != self.password:
			print("Password and Username Does Not Match")
		else:
			print("Welcome " + emp[1] + "!")
			self.id = str(emp[0])	
			self.name =str(emp[1])
			self.preference=str(emp[4])
			self.accessLevel=emp[5]
			self.sales=emp[6]
			self.phone=emp[7]
			self.signedIn(server)

	def signedIn(self, server):
		while 1:
			print("---Employee Menu---")
			print("1. Sale")
			print("2. Order Management")
			print("3. Database Management")
			print("4. Report Management")
			print("5. Delivery Management")
			print("6. Sign Out")
			try:
				userInput = input()
				try:
					userInput=int(userInput)
				except:
					print("Please enter a valid option")
					continue
				if userInput == 1:
					PlaceOrder("NULL",self.id,server,self.preference)		
				elif userInput == 2:
					if self.accessLevel == 2:
						OrderManagement(server, self.preference)
					else:
						print("You dont have the right credentials for this section!")
				elif userInput == 3:
					DatabaseManagement(server,self.accessLevel)
				elif userInput == 4:
					ReportManagement(server)
				elif userInput == 5:
					DeliveryManagement(server)
				elif userInput == 6:
					break
				else:
					print("Not an option!")
			except:
				 print("Unexpected error:", sys.exc_info()[0])
				 raise