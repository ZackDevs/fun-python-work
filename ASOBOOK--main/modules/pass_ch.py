from modules.clear import clear as clr
def changePass(db, currentuser):
	def askForPass(usr):
			passed = False
			while not passed:
				print(" ---- Gestor de utilizadores ----\n\nEscrever back, se quiser sair deste menu.")
				user = db[usr]
				psw = user["password"][::-1]
				pswed = input(f"Password antiga: ")
				if pswed.lower() == "back":
					return
				if psw != pswed:
					clr()
					print("Incorrect Password.")
					continue
				
				passed = True
			return True
	def askForNewPass():
			passed = False
			while not passed:
				print(" ---- Gestor de utilizadores ----\n\nEscrever back, se quiser sair deste menu.")
				pswed = input(f"Password nova: ")
				if pswed.lower() == "back":
					return
				if not pswed:
					clr()
					print("Por favor, escreva uma palavra-passe.")
					continue
				if not 8 <= len(pswed) <= 20:
					clr()
					print("Por favor, escreva uma palavra-passe entre 8 e 20 caracteres.")
					continue
				if pswed.lower() == pswed:
					clr()
					print("Por favor, escreva uma palavra-passe com pelo menos uma letra maiuscula.")
					continue
				if not any([True if pswed.count(i) != 0 else False for i in ["#","@","?","!"]]):
					clr()
					print("Por favor, escreva uma palavra-passe que contenha (#@?!).")
					continue
				passed = True
				return pswed[::-1]
	clr()
	yes = askForPass(currentuser)
	if not yes:
		return None
	clr()
	newpass = askForNewPass()
	if not newpass:
		return None
	return newpass
	