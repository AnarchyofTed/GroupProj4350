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
		s = server.loginCheck("SELECT * FROM customers WHERE customer_username= '%s'"% self.username)
		cust = s.fetchone()
		if s.description.__len__ is 0:
			print("Invalid Username")
		elif cust[5] != self.password:
			print("password aint " + str(cust[5]))
		else:
			print("Welcome " + cust[1] + "!")
			self.id = str(cust[0])
			
		
		