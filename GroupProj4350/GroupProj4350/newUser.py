class NewUser:

	def __init__(self):
		print("Welcome! Please fill out the information for your new customer account")
		Uname = input("UserName : ")
		Pword = input("Password : ")
		name = input("Name : ")
		address = input("Address : ")
		phoneNum = input("Phone # : ")
		loopcheck=0
		while loopcheck is 0:
			sp = input("Store Preference 1) LegoTron 2) Mrs.LegoTron  Enter 1 or 2: ")
			if sp is '1':
				storePref="LegoTron"
				loopcheck=2
			elif sp is '2':
				storePref="Mrs.LegoTron"
				loopcheck=2
			else:
				print("Not a valid store selection!")
