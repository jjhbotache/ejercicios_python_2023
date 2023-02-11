from random import randint
respuesta = -1
def preguntar():
  global respuesta
  respuesta = int(input("Escribe un numero del 1 al 100: "))

print("Juguemos a adivinar el numero")
intentos = -1
numero_random = 0

# guarda la cantidad de intentos a la que se quiere jugar
while intentos <= 0:
  try:
    intentos = int(input("Inserte la cantidad de intentos: "))
  except:
    print('Introduce un numero y nada mas')
print(f"Usted esta jugando a {intentos} numero de intentos, comencemos")

numero_random = randint(1,100)

print("~"*50) 
  
while intentos > 0:
  preguntar()

  # si esta mal
  if numero_random != respuesta:
    print("Incorrecto")
    if respuesta > numero_random: print("El numero que pense es menor")
    if respuesta < numero_random: print("El numero que pense es mayor")
  #has adivinado
  else:
    print("has adivinado!!")
    break
  
  intentos-=1


if numero_random != respuesta: print(f"Perdiste, el numero era: {numero_random}")