# Made by ZackDevs (github.com/ZackDevs)

list = ["Adição","Subtração","Muliplicação","Divisão","Resto da Divisão","Elevado"]
def arit(num):
    switch={
      "1":'+',
      "2":'-',
      "3":'*',
      "4":'/',
      "5":'%',
      "6":'**'
      }
    return switch.get(num, 0)
string = ""
for i in range(len(list)):
  string+=str(i+1) + " - " + list[i]+ "\n"
print("Qual calculo gostaria de fazer?\n")
calc = arit(input(string + "\n-> "))
if calc == 0: 
  print("Por favor escolher um numero de 1 a " + str(len(list)))
else:
  num1 = input("\nPrimeiro Número: ")
  num2 = input("\nSegundo Número: ")
  try:
    num1 = float(num1)
    num2 = float(num2)
    res = str(eval(str(num1) + calc + str(num2)))
    if res.split(".")[1] == "0":
      res = res.split(".")[0]
    print("\n" + "Resultado: " + res)
  except:
    print("Eu pedi um número...")
