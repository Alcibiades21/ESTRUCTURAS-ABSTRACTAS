from pila import Pila
"""Elabore un programa que lea dat por dato hasta llenar una pila, con 
esta deberá ir sacando cada valor mostrando cada evolución."""
x = 1
p = Pila()
while x != 0:
  try:
    x = int(input("Ingrese un valor, 0 para terminar: "))
  except:
    x = 0
    print("Error al digitar")
  if x != 0:
    p.agregar(x)

while p.tope != None:
  print(p.mostrar(), end=" ")
  print("Sacar:", p.sacar())