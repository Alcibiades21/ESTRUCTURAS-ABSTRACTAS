from nodo import Nodo
class Pila:
  base = None # ultimo nodo de la lista enlazada
  tope = None # primer nodo de la lista enlazada
  def __init__(self) -> None:
    pass
  def agregar(self, dato):
    nuevo = Nodo(dato)
    if self.tope == None:
      self.tope = self.base = nuevo
    else:
      nuevo.enlace = self.tope
      self.tope = nuevo
  def sacar(self):
    if self.tope == None:
      return None
    elif self.tope == self.base:
      aux = self.tope
      self.tope = self.base = None
      return aux.dato
    else:
      aux = self.tope
      self.tope = aux.enlace
      aux.enlace = None
      return aux.dato
  def mostrar(self):
    aux = self.tope
    lista = ""
    while aux != None:
      lista += str(aux.dato) + " "
      aux = aux.enlace
    return lista