from words import test as words
import random
import re
from os import system
def createAscii(num):
	switch = {
		0: """	  _______
     |/      |
     |      
     |      
     |       
     |      
     |
 ____|___""",
		1: """	  _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
 ____|___""",
		2: """	  _______
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
 ____|___""",
		3: """	  _______
     |/      |
     |      (_)
     |      \|
     |       
     |
     |
 ____|___""",
		4: """	  _______
     |/      |
     |      (_)
     |      \|/
     |       
     |     
     |
 ____|___""",
		5: """	  _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
 ____|___""",
		6: """	  _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      /
     |
 ____|___""",
		7: """	  _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
 ____|___"""
	}
	return switch.get(num)
	
def clr():
	system("clear")
def start():
	start = False
	word = ""
	looses = 0
	encodedWord = ""
	tentativas = []
	while True:
		if not start:
			word = random.choices(words)[0]
			encodedWord = "_ "*len(word)
			start = True
		print(createAscii(looses))
		print("\n\n")
		print("Palavra: " + encodedWord)
		print("Letras usadas: " + ", ".join(tentativas))
		if word == encodedWord.replace(" ",""):
			s = "" if looses == 1 else "s"
			print()
			print("Ganhaste! Nice.")
			print(f"Tiveste {looses} erro{s}!")
			s = "" if len(tentativas) == 1 else "s" 
			print(f"Usas-te {len(tentativas)} tentativa{s}")
			break
		if looses == 7:
			print("\nA pessoa morreu")
			print(f"A palavra era {word}.")
			break
		letra = input("\nLetra? ").lower()
		if letra == word:
			s = "" if looses == 1 else "s"
			print()
			print("Ganhaste! Nice.")
			print(f"Tiveste {looses} erro{s}!")
			s = "" if len(tentativas) == 1 else "s" 
			print(f"Usas-te {len(tentativas)+1} tentativa{s}.")
			break
		if letra in tentativas:
			clr()
			print("Já usaste essa letra...")
			continue
		if len(re.findall("[0-9]",letra)) > 0 or len(re.findall("[a-z]|[A-Z]", letra)) != len(letra) or len(letra) > 1:
			clr()
			print("Tenta usar só uma letra ou descobre a palavra inteira.")
			continue
		if word != re.sub(letra, "_",word):
			cache = word
			word = re.sub(letra, "_",word)
			encodedWord = encodedWord.split()
			for i in range(len(word)):
				if word[i] != "_":
					continue
				encodedWord[i] = letra
			encodedWord = " ".join(encodedWord)
			word = cache
			tentativas += letra
			clr()
		else:
			looses += 1
			tentativas += letra
			clr()

start()
			
