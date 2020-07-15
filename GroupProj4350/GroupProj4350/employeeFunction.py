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
		emp = server.loginCheck("SELECT * FROM employees WHERE employee_username= '%s'"% self.username)
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