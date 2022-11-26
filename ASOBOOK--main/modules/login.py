from modules.clear import clear as clr
def login(db):
	passed = False
	while not passed:
		
		def askForIndent():
			passed = False
			while not passed:
				print(" ---- Gestor de utilizadores ----\n\nIf you want to go back write back.")
				way = input("Email / Username? ")
				user = ""
				if way.lower() == "back":
					return
				for i in db.keys():
					if i == "dead_users":
						continue
					if db[i]["email"] == way:
						user = i
				if "user-"+ way.lower() in db.keys():
					user = "user-"+ way.lower()
				if not user:
					clr()
					print("There is no user with that username / email.")
					continue
				passed = True
			return user
					
		def askForPass(usr):
			passed = False
			while not passed:
				print(" ---- Gestor de utilizadores ----\n\nEscrever back, se quiser sair deste menu.")
				user = db[usr]
				name = user["user"]
				psw = user["password"][::-1]
				pswed = input(f"Password for {name}: ")
				if pswed.lower() == "back":
					return
				if psw != pswed:
					clr()
					print("Incorrect Password.")
					continue
				passed = True
			return True
		clr()
		usr = askForIndent()
		if not usr:
			return
		clr()
		passed = askForPass(usr)
		if not passed:
			return
		return usr