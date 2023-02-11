from random import randint
from functools import reduce
import os
# =============================================== variables ===============================================
puntos_para_ganar = 50
puntos_jugador1 = 0
puntos_jugador2 = 0
# =============================================== clases ===============================================
class Jugador ():
  def __init__(self,nombre = "",puntos = 0):
    self.nombre = nombre
    self.puntos = puntos
  
  def rodar_dado(self):
    puntaje = 0
    input(f"Turno de {self.nombre}\n presiona para rodar el dado")
    puntaje = randint(1,6)
    print(f"Has obtenido {puntaje}")
    return puntaje
  
  def sumar_puntos(self,puntos):
    print(f"\n Felicidades {self.nombre}, has sumado {puntos} puntos.")
    self.puntos += puntos
  
# =============================================== funciones ===============================================
def bienvenida():
  os.system("cls")
  print("~"*50)
  print("Bienvenido")
  print("~"*50)
  jugador1=Jugador(nombre=input("Como te llamas, jugador 1?\n").title())
  print(f"Bienvenido {jugador1.nombre}")
  jugador2=Jugador(nombre=input("Como te llamas, jugador 2?\n").title())
  print(f"Bienvenido {jugador2.nombre}")
  print("~"*50)
  return jugador1,jugador2

def pedir_puntos_para_ganar():
  puntos_para_ganar = 0
  while puntos_para_ganar < 50:
    try:
      puntos_para_ganar=int(input("Introduce la cantidad de puntos para ganar (50 o más)\n"))
    except:
      print("Asegurate de que sea un numero")
  return puntos_para_ganar

def turno(jugador1,jugador2):
  """pide a cada jugador rodar los dados
  Returns:
      tupla : devuelve una lista donde el primer elemento es el puntaje del jugador 1
  y el segundo elemento es del segundo jugador
  """
  puntaje1 = jugador1.rodar_dado()
  puntaje2 = jugador2.rodar_dado()
  total = puntaje1 + puntaje2
  
  if puntaje1 > puntaje2 : jugador1.sumar_puntos(total)
  elif puntaje1 < puntaje2 : jugador2.sumar_puntos(total)
  else : 
    jugador1.sumar_puntos(total)
    jugador2.sumar_puntos(total)  

# =============================================== codigo ===============================================

jugadores = bienvenida()
puntos_para_ganar = pedir_puntos_para_ganar()
while jugadores[0].puntos < puntos_para_ganar and jugadores[1].puntos < puntos_para_ganar:
  print("~"*50)
  turno(jugadores[0],jugadores[1])
  print("~"*50)
  input("Presiona para continuar")
  os.system("cls")
  for jugador in jugadores:
    print(f"{jugador.nombre} tiene {jugador.puntos}")
  print("~"*50)

if jugadores[0].puntos > jugadores[1].puntos:
  print(f"Ha ganado {jugadores[0].nombre}")
elif jugadores[0].puntos < jugadores[1].puntos:
  print(f"Ha ganado {jugadores[1].nombre}")
else:
  print("Es un empate, felicidades jugadores")