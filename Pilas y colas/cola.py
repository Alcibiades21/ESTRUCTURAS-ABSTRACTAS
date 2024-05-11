from nodo import Nodo
class Cola:
  cab = None
  fin = None
  def __init__(self) -> None:
    pass
  def atender(self):
    if self.cab == None:
      return None
    elif self.cab == self.fin:
      aux = self.cab
      self.cab = self.fin = None
      return aux.dato
    else:
      aux = self.cab
      self.cab = aux.enlace
      aux.enlace = None
      return aux.dato
  def formar(self, dato):
    nuevo = Nodo(dato)
    if self.cab == None:
      self.cab = self.fin = nuevo
    else:
      self.fin.enlace = nuevo
      self.fin = nuevo
  def __str__(self) -> str:
    aux = self.cab
    lista = ""
    while aux != None:
      lista += str(aux.dato) + " "
      aux = aux.enlace
    return lista