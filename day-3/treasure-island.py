print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Bem Vindo a Ilha do Tesoudo.")
print("Sua missão é encontrar o tesouro.")
crossroad = input("Você está em uma encruzilhada. Aonde você quer ir?\nDigite 'direita' ou 'esquerda\n")

if crossroad == 'direita':
 print("Você caiu em um buraco!")
 print("Game Over!!!")

elif crossroad == 'esquerda':
 print("Você chegou em um lago. Há uma ilha no meio do lago")
 swim_wait = input("Digite 'esperar' para esperar por um barco.\nDigite 'nadar' para atrevessar a nado.\n")
 if swim_wait == 'nadar':
  print("Atacado por piranhas\n GAME OVER!!")
 elif swim_wait == 'esperar':
  print("Você chegou a ilha ileso")
  print("Há uma casa com 3 portas. Uma vermelha, uma amarela e uma azul.")
  color_door = input("Qual a cor você quer? ")
  if color_door =='vermelha':
   print("Você morreu queimado!\nGAME OVER!!")
  elif color_door == 'azul':
   print("Você foi comigo por feras selvagens\nGAME OVER!!")
  elif color_door == 'amarelo':
   print("Você encontou o tesouro!!\n YOU WIN!")
  else:
   print("Você escolheu uma porta que não existe!\nGAME OVER!!")

