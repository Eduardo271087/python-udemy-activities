class Fabrica:
  # __init__ es el constructor de la clase
  def __init__(self, tiempo, nombre, ruedas):
    self.tiempo = tiempo
    self.nombre = nombre
    self.ruedas = ruedas
    print("Se creó el auto", self.nombre)

  # __str__ sobreescribe el método str()
  def __str__(self):
    return "{} ({})".format(self.nombre, self.tiempo)

class Listado:
  autos = []

  def __init__(self, autos = []):
    self.autos = autos

  def fabricar(self, x):
    self.autos.append(x)
  
  def visualizar(self):
    for x in self.autos:
      print(x)

a = Fabrica(10, "Alvaro", 4)

l = Listado([a])
l.visualizar()

l.fabricar(Fabrica(15, "Estudiantes", 10))
l.visualizar()