from modules.clear import clear as clr
def register(db):
	def askusername():
		passed = False
		while not passed:
			print(" ---- Gestor de utilizadores ----")
			usrn = input("Username: ")
			usr = db.get(f"user-{usrn.lower()}", None)
			if not usrn or usr:
				clr()
				print("Por favor, digite um username." if not usrn else "Essa conta já existe.")
				continue
			passed = True
		return usrn
	def askEmail():
		passed = False
		while not passed:
			print(" ---- Gestor de utilizadores ----")
			email = input("Email: ")
			if not email:
				clr()
				print("Por favor, digite um email.")
				continue
			if email.count("@") != 1 or not email.split("@")[0] or email.split("@")[1] != "treetree2.school" or len(email.split(" ")) != 1:
				clr()
				print("Por favor, digite um email com o domínio de treetree2.school")
				continue
			t = all([False if i == "dead_users" or db[i]["email"].lower() != email.lower() else True for i in db.keys()])
			if t:
				clr()
				print("Esse email já foi usado, por favor usar outro email.")
				continue
			passed = True
		return email
	def askPassword():
		passed = False
		while not passed:
			print(" ---- Gestor de utilizadores ----")
			psw = input("Password: ")
			if not psw:
				clr()
				print("Por favor, escreva uma palavra-passe.")
				continue
			if not 8 <= len(psw) <= 20:
				clr()
				print("Por favor, escreva uma palavra-passe entre 8 e 20 caracteres.")
				continue
			if psw.lower() == psw:
				clr()
				print("Por favor, escreva uma palavra-passe com pelo menos uma letra maiuscula.")
				continue
			if not any([True if psw.count(i) != 0 else False for i in ["#","@","?","!"]]):
				clr()
				print("Por favor, escreva uma palavra-passe que contenha (#@?!).")
				continue
			passed = True
		return psw
	
	def askAge():
		passed = False
		while not passed:
			print(" ---- Gestor de utilizadores ----\n")
			print("Devido aos nossos termos de serviço nós necessitamos de saber a sua idade.")
			age = input("Idade: ")
			try: 
				age = int(age)
			except:
				clr()
				print("Por favor usar números.")
				continue
			if not 18 <= age < 120:
				clr()
				print("É necessário ter, no minimo, 18 anos de idade." if 18 > age else "Duvido que tenha mais de 120 anos de idade.\nSe estiver enganado por favor contactar um admin.")
				continue
			passed = True
		return True
	clr()
	username = askusername()
	clr()
	email = askEmail()
	clr()
	password = askPassword()
	clr()
	askAge()
	return {
		"usr": "user-"+ username.lower(),
		"object": {
			"user": username,
			"email": email,
			"password": password[::-1]
		}
	}
	