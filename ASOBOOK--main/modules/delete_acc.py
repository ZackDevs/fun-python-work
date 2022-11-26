from modules.clear import clear as clr
def del_acc(db, current_user):
	def askForPass(usr):
			passed = False
			while not passed:
				print(" ---- Gestor de utilizadores ----\n\nEscrever back, se quiser sair deste menu.")
				user = db[usr]
				psw = user["password"][::-1]
				pswed = input(f"Password: ")
				if pswed.lower() == "back":
					return
				if psw != pswed:
					clr()
					print("Incorrect Password.")
					continue
				
				passed = True
			return True
	def delAccount(usr):
		passed = False
		while not passed:
			username = db[usr]["user"]
			print(" ---- Gestor de utilizadores ----\n\nEscrever back, se quiser sair deste menu.")
			print(f"Para apagares a tua conta por favor escreva: {username}")
			inputted = input()
			if inputted == "back":
				return
			if inputted != username:
				clr()
				print("Username errado.")
				continue
			return True
	clr()
	yes = askForPass(current_user)
	if not yes:
		return
	clr()
	yes = delAccount(current_user)
	if not yes:
		return
	return [current_user]