"""Elabore un programa que recoja la cantidad de tiempo que demoraron 
cada uno de los n clientes que esperaban fuera del banco en el momento 
de abrirse para ser atendidos en la caja. Mostrar cuanto demoró el 
último cliente en la entidad antes de ser atendido.

Ejemplo: n = 7 clientes

Tiempos:

7 3 9 2 5 8 3
El último cliente demoró: 34 minutos"""

def leernumero(mensaje):
  y = 1
  while y != 0:
    try:
      x = int(input(mensaje))
      y = 0
    except:
      y = 1
      print("Error al digitar")
  return x
from cola import Cola
c = Cola()
n = leernumero("Cantidad de clientes: ")
for i in range(n):
  c.formar(leernumero("Demora del cliente en la caja: "))
print(c)
suma = 0
while c.cab != c.fin:
  suma += c.atender()
print("El tiempo para atender al último fue:", suma)
