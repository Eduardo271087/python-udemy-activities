class Fabrica:
  def __init__(self, marca, nombre, precio, descripcion, ruedas = None, distribuidor = None):
    self.marca = marca
    self.nombre = nombre
    self.precio = precio
    self.descripcion = descripcion
    self.ruedas = ruedas
    self.distribuidor = distribuidor

  def __str__(self):
    return """\
MARCA\t\t{}
NOMBRE\t\t{}
PRECIO\t\t{}
DESCRIPCION\t{}""".format(self.marca, self.nombre, self.precio, self.descripcion)

auto = Fabrica('Ford', 'Ranger', 10, 'Camioneta 4x4')

print(auto.nombre)

class Auto(Fabrica):
  pass

z = Auto('Ford', 'Ranger', 100.000, 'Camioneta')
print(z)

class Deportivo(Fabrica):
  ruedas = ""
  distribuidor = ""

  def __str__(self):
    return """\
MARCA\t\t{}
NOMBRE\t\t{}
PRECIO\t\t{}
DESCRIPCION\t{}
RUEDAS\t\t{}
DISTRIBUIDOR\t{}""".format(self.marca, self.nombre, self.precio, self.descripcion, self.ruedas, self.distribuidor)

deportivo = Deportivo('Volkswagen', 'Vento', 54000, 'El mejor')
deportivo.ruedas = 3
deportivo.distribuidor = 'Tu autito'

print(deportivo)