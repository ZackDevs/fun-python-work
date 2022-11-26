from modules.clear import clear as clr
def stats(db, current_user):
	clr()
	print(" ---- Gestor de utilizadores ----")
	dead = db["dead_users"]
	s = "s" if len(db) - 1 > 1 else ""
	se = "es" if len(db) - 1 > 1 else ""
	v = "em" if len(db) - 1 > 1 else "e"
	print(f"Neste momento exist{v}: {len(db) - 1} utilizador{se}.")
	list = []
	for i in db.keys():
		if i == "dead_users":
			continue
		list += [db[i]["user"]]
	print(f"Sendo o{s} nome{s}:\n")
	list.sort()
	print("\n".join(list))
	print()
	s = "s" if dead > 1 or dead == 0 else ""
	se = "es" if dead > 1 or dead == 0 else ""
	print(f"Neste momento existem: {dead} utilizador{se} apagado{s}.")
	input("Para ir para traz pressionar enter.\n")