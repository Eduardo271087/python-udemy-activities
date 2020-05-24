import copy

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

class Auto(Fabrica):
  pass

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

class Accesorios(Fabrica):
  autor = ""
  fabricante = ""

  def __str__(self):
    return """\
MARCA\t\t{}
NOMBRE\t\t{}
PRECIO\t\t{}
DESCRIPCION\t{}
AUTOR\t\t{}
FABRICANTE\t{}""".format(self.marca, self.nombre, self.precio, self.descripcion, self.autor, self.fabricante)

fabrica = Fabrica('Ford', 'Ranger', 10, 'Camioneta 4x4')

auto = Auto('Ford', 'Ranger', 100000, 'Camioneta')

deportivo = Deportivo('Volkswagen', 'Vento', 54000, 'El mejor')
deportivo.ruedas = 3
deportivo.distribuidor = 'Tu autito'

accesorios = Accesorios('Fiat', 'Luces de neón', 10000, 'Iluminan mejor')
accesorios.autor = 'Vos'
accesorios.fabricante = 'Yo'

fabrica = [accesorios, deportivo]
fabrica.append(auto)

print(fabrica)

for x in fabrica:
  print(x, "\n")

for x in fabrica:
  print(x.marca, x.precio)

#   File "/home/eduardo-fernandez/source/python-udemy-activities/section-10/inherited-classes-polymorphism.py", line 70, in <module>
#     print(x.autor)
# AttributeError: 'Deportivo' object has no attribute 'autor'
# for x in fabrica:
#   print(x.autor)

for x in fabrica:
  if isinstance(x, Auto):
    print(x.marca, x.nombre)
  elif isinstance(x, Deportivo):
    print(x.marca, x.nombre, x.ruedas)
  elif isinstance(x, Accesorios):
    print(x.marca, x.nombre, x.fabricante)

def descuento_accesorio(t, descuento):
  t.precio = t.precio - (t.precio / 100 * descuento)

descuento_accesorio(accesorios, 10)

print(accesorios.precio)

copia_deportivo = copy.copy(accesorios)

print(copia_deportivo)