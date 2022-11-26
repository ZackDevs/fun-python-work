from modules.clear import clear as clr
from modules.register import register
from modules.login import login
from modules.pass_ch import changePass
from modules.delete_acc import del_acc
from modules.stats import stats
# Este é o código que sobrou depois do problema com o espião...

# O código tem 3 listas fundamentais. O propósito de cada uma é auto-explicativo. A lista_pass tem uma password já encriptada.

# Começa a implementação do programa dentro da função "programa" e depois do if que já estava escrito. O programa já recolhe a resposta do utilizador. O código que trata da opção 6 não foi eliminado pelo espião, por isso não te preocupes com essa opção.

# Podes definir todas as variáveis e funções auxiliares que quiseres abaixo da linha compreendida para esse efeito.

# Dá uma vista de olhos no código já escrito antes de começar. Boa sorte!

# IMPORTANTE:
# Usa tabs em vez de espaços na indentação, caso contrário terás um "IndentationError
# - Vai a Settings -> Indent type e muda para tabs
# - Usa a tecla "tab" quando queres indentar

# Don't worry the test user still exists, just in the repl.it db

db:dict = {
	"user-john the spy": {
		"user": "John the Spy",
		"email": "Johnspy@treetree2.school",
		"password": "password"[::-1]
	},
	"dead_users": 0
}

def programa():
	login_account = False
	while not login_account:
		clr()
		print(""" ---- Gestor de utilizadores ----
		1 - Registar utilizador 
		2 - Login no ASOBOOK 
		3 - Sair 
		""")
	
		escolha = input()
	
	  
		options = {
			"1": register,
			"2": login,
	    "3": 1
	  }
		escolha = options.get(escolha, None)
		if escolha == 1:
			return -1
	  
	
		if not escolha:
			continue
		returned = escolha(db)
		if type(returned) == dict:
			db[returned["usr"]] = returned["object"]
			continue
		if type(returned) == str:
			login_account = returned
		
	while login_account:
		clr()
		print(f""" ---- Gestor de utilizadores ----
		Logged in as {db[login_account]["user"]}
	
		1 - Redefinir Password
		2 - Eliminar Conta
		3 - Estatisticas
		4 - Log out
		""")

		escolha = input()
		options = {
			"1": changePass,
			"2": del_acc,
			"3": stats,
	    "4": 1
	  }
		escolha = options.get(escolha, None)
		if not escolha:
			continue
		if escolha == 1:
			return programa()
		returned = escolha(db,login_account)
		if type(returned) == str:
			db[login_account]["password"] = returned
		if type(returned) == list:
			del db[login_account]
			db["dead_users"] += 1
			return programa()
programa()
	# A tua implementação começa abaixo desta linha 
	# --------------------------------------------- 
 

# Podes implementar as funções auxiliares que pretenderes abaixo desta linha 
# --------------------------------------------- #
	