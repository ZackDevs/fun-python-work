import json
import os
import requests
import re as regex

def clear():
  os.system("clear")
def duas_moedas(cont,len):  
  def get_first():
    res = input("Por favor escolha a moeda de base.\nExample: Dollars - USD\n------> ")
    if res.lower() == "back":
      clear()
      cambio()
      return None
    else:
      moeda_base = cont.get(res.upper(), None)
      if not moeda_base:
        clear()
        print("Por favor escolha uma moeda válida")
        print("Escreva back para voltar ao menu anterior.\n")
        return get_first()
      clear()
      return res.upper()

  def get_second(code):
    res = input(f"Por favor escolha uma moeda para ser convertida para {code}.\nExample: Dollars - USD\n------> ")
    if res.lower() == "back":
      clear()
      cambio()
      return None
    else:
      if res.upper() == code:
        clear()
        print("Não escolhas a mesma moeda..")
        return get_second(code)
      moeda_base = cont.get(res.upper(), None)
      if not moeda_base:
        clear()
        print("Por favor escolha uma moeda válida")
        print("Escreva back para voltar ao menu anterior.\n")
        return get_second(code)
      return res.upper()
  def get_value():
    res = input("Qual era a quantia que gostaria de converter?\n------> ")
    try:
      res = float(res)
      return res
    except:
      clear()
      print("Por favor usar um número.")
      return get_value()
  first_code = get_first()
  if not first_code:
    return
  second_code = get_second(first_code)
  if not second_code:
    return
  clear()
  value = get_value()
  my_secret = "" # GET IT FROM https://apilayer.com/marketplace/exchangerates_data-api#authentication
  url = f"https://api.apilayer.com/exchangerates_data/convert?to={first_code}&from={second_code}&amount={value}"
  headers= {
    "apikey": my_secret
  }
  response = requests.get(url, headers=headers)
  rate = response.json()["info"]["rate"]
  print(f"\n{value} {first_code} - {round(value/rate,2)} {second_code}")
  if rate*value < value:
    print(f"{first_code} é {round(1/rate,2)} vezes maior que {second_code}")
  else:
    print(f"{second_code} é {round(rate,2)} vezes maior que {first_code}")
  rep = input("\n\n\nGostaria de voltar ao menu do cambio?\n------> ")
  if rep.lower() == "sim":
    clear()
    return cambio()
  else:
    print("Saindo do programa.")
    exit()
  
def ver_moedas(cont, len):
  string = ""
  p = 0
  pages = len["pages"]
  
  for i in cont.keys():
    name = cont[i]
    if p <= 10 or pages == 1:
      string += f"{i} - {name}\n"
      p += 1
    else:
      print("Por favor ver quais as moedas estão disponiveis.")
      print("Se quiser sair use back.")
      print("Se quiser ver mais use next.\n")
      print(string)
      rep = input("\n------> ")
      if rep.lower() == "back":
        clear()
        return cambio()
      elif rep.lower() == "next":
        p = 0
        string = ""
        clear()
        pages -= 1
  print("Vistes todas as moedas.")
  print("Voltando ao menu do cambio.\n")
  return cambio()
def buscar_moedas():
  file = open("currencies.json", "r")
  content = json.load(file)
  length = len(content)
  pages = (length // 10) + 1 if length / 10 > length // 10 else length // 10
  n = { "len": length, "pages": pages}
  return {"len": n, "cont": content}
def ganhar_dinheiro(cont,len):
  clear()
  print("De quanto em quanto tempo gostaria de receber dinheiro?\n")
  s = {
    "dia": 365,
    "semana": 52,
    "mês": 30,
    "ano": 1,
  }
  p = 0
  for i in s.keys():
    print(f"{p+1} - {i}")
    p += 1
  tempo = input("------> ")
  try:
    tempo = int(tempo)
  except:
    return ganhar_dinheiro(cont,len)
  tempo = list(s.keys())[tempo-1]
  ano = s.get(tempo)
  clear()
  money = input(f"Quanto dinheiro ganharias por cada {tempo}?\n------> ")
  try:
    money = int(money)
  except:
    return ganhar_dinheiro(cont,len)
  string = ""
  for i in range(10):
    string += f"Passado {(i+1)*10} anos ganharias {ano*money*(i+1)}.\n"
  clear()
  print(string)
  reply = input("Gostaria de proceder?\n------> ")
  if reply.lower() == "sim":
    clear()
    return cambio()
  else:
    print("Saindo do programa.")
    exit()
  
def fun_facts(cont,len):
  clear()
  massa = round(7.5*10**9)
  altura = round(2.33*10**9)
  print("Vamos falar de quão grande é um bilião.")
  print(f"Em moedas de 1 euro.\n1 Bilião pesaria {massa} kilogramas ou {int(massa*10**-3)} toneladas.")
  print(f"Em altura seria {altura} metros ou {int(altura*10**-3)} kilometros.")
  print(f"Conseguiamos dar {altura * 10// (6.3781*10**6)} voltas á Terra.")
  reply = input("Gostaria de proceder? (sim / não)\n------> ")
  if reply.lower() == "sim":
    clear()
    return cambio()
  else:
    print("Saindo do programa.")
    exit(0)
def cambio():
  escolhas = {
  "1": duas_moedas,
  "2": ver_moedas,
  "3": ganhar_dinheiro,
  "4": fun_facts,
}
  currencies = buscar_moedas()
  length = currencies["len"]
  size = length["len"]
  cont = currencies["cont"]
  print("Bem vindo ao menu do seu amigo o Economista!")
  print(f"Pode escolher entre {size} moedas.")
  print("O que gostaria de ver?\n")
  print("1 - Escolher duas moedas para converter!")
  print("2 - Ver as moedas que pode converter!")
  print("3 - Ver quanto dinheiro ganharia a longo do tempo!")
  print("4 - Fun facts.")
  choice = input("------> ")
  menu = escolhas.get(choice, None)
  if not menu:
    clear()
    return cambio()
  clear()
  menu(cont, length)
