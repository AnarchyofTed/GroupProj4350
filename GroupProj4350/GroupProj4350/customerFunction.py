class Customer:
	
	def __init__(self,server, uname, pword):
		self.id=''
		self.name =''
		self.phone=''
		self.preference=''
		self.username=uname
		self.password=pword
		self.CustomerLogin(server)


	
	def CustomerLogin(self, server):
		cust = server.loginCheck("SELECT * FROM customers WHERE customer_username= '%s'"% self.username)
		cust = cust.fetchone()
		if cust is None:
			print("Invalid Username")
		elif cust[5] != self.password:
			print("Password and UserName Does Not Match!")
		else:
			print("Welcome " + cust[1] + "!")
			self.id = str(cust[0])
			self.name =str(cust[1])
			self.preference=str(cust[3])
			self.phone=emp[2]
		