class Fabrica:
  # __init__ es el constructor de la clase
  def __init__(self, tiempo, nombre, ruedas):
    self.tiempo = tiempo
    self.nombre = nombre
    self.ruedas = ruedas
    print("Se creó el auto", self.nombre)

  # __del__ es el destructor de la clase
  def __del__(self):
    print("Se eliminó el auto", self.nombre)

  # __str__ sobreescribe el método str() y se invoca al intentar imprimir el objeto completo de esta clase
  def __str__(self):
    return "{} se fabricó con éxito en el tiempo {} y tiene {} ruedas".format(self.nombre, self.tiempo, self.ruedas)
  
  # __len__ sobreescribe el método len()
  def __len__(self):
    return self.tiempo


a = Fabrica(10, "Alvaro", 4)
print(str(a))
print(len(a))