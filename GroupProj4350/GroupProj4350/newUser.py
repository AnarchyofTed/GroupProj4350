class NewUser:
	def __init__(self, server):
		self.Uname = ''
		self.Pword = ''
		self.name = ''
		self.phoneNum = ''
		self.storePref = ''
		self.addUser(server)

	def addUser(self, server):
		print("Welcome! Please fill out the information for your new customer account")
		self.Uname = input("UserName : ")
		self.Pword = input("Password : ")
		self.name = input("Name : ")
		self.phoneNum = input("Phone # : ")
		loopcheck=0
		while loopcheck is 0:
			sp = input("Store Preference 1) LegoTron 2) Mrs.LegoTron  Enter 1 or 2: ")
			if sp is '1':
				self.storePref="LegoTron"
				loopcheck=1
			elif sp is '2':
				self.storePref="Mrs.LegoTron"
				loopcheck=1
			else:
				print("Not a valid store selection!")
		print("New user created for " + self.name + "!")
		server.sqlInsert("INSERT INTO customers (customer_name, customer_phone, customer_storePreference, customer_username, customer_password) VALUES('%s', '%s', '%s', '%s', '%s')" %(self.name, self.phoneNum, self.storePref, self.Uname, self.Pword))
