import os
from time import sleep
import csv
os.system("cls")

verbo_completo=""
# verifica que termine en ar er ir
while not(verbo_completo[-2:].lower() in ["ar","er","ir"]): 
  # pregunto por el verbo
  verbo_completo = (input("Introduzca un verbo: ").strip())

# traigo los verbos irregulares
verbos_irregulares = []
with open('verbos_irregulares.csv', 'r') as file:
    file = csv.reader(file)
    for row in file:
      verbos_irregulares += row
# guardo las conjugaciones
conjugaciones = {
  # pronombre       aditivo
  "Yo"          :    "o",
  "Tú"          :    "s",
  "Él"          :    "",
  "Nosotros"    :    "mos",
  "Vosotros"    :    "ís",
  "Ellos"       :    "n"
}

# guardo la terminacion ar er ir (solo la letra anterio a la r) 
terminacion = verbo_completo[-2]

print("~"*50)
print("Procesando")
print("~"*50)
sleep(2)

if verbo_completo in verbos_irregulares:
  print(f'Lo sentimos "{verbo_completo}" es un verbo irregular')
  import csv

else:
  # termino de recortar el verbo
  verbo = verbo_completo[:-2]

  # por cada pronombre, uso su debido aditivo
  for pronombre in conjugaciones.keys():
    # en caso de que sea el primer pronombre, no agreto la terminacion
    if pronombre == "Yo": print(f"{pronombre} {verbo}{conjugaciones[pronombre]}")
    else:
      print(f"{pronombre} {verbo}{terminacion}{conjugaciones[pronombre]}")
    sleep(0.6)
  
  print("~"*50)
  
  if input("Es la respuesta correcta? (s/n) ").lower() == "n" :
    # Abrir el archivo CSV en modo de escritura
    with open('verbos_irregulares.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=[""])
        # Escribir una nueva fila con los valores
        writer.writerow({"":verbo_completo})
    print("Se ha agregado el verbo a la lista de verbos irregulares")
  else:
    print("Me alegra!")
    print("Adios")
    