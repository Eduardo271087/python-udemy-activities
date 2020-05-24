class Auto:
  pass

auto = Auto()

auto.color = "Rojo"
auto.puertas = "Muchas"
print("Mi auto es de color: ", auto.color)

class OtroAuto:
  Rojo = False

otroAuto = OtroAuto()
print(otroAuto.Rojo)

otroAuto.Rojo = True
print(otroAuto.Rojo)

class NuevoAuto:
  Rojo = False

# self es this, hace referencia al objeto actual
  def __init__(self):
    print("Se creó un Nuevo Auto")
  
  def fabricar(self):
    self.Rojo = True

  def confirmar_fabricacion(self):
    if self.Rojo:
      print("Auto coloreado rojo")
    else:
      print("Aun no está coloreado")

nuevoAuto = NuevoAuto()
print(nuevoAuto.Rojo)

nuevoAuto.confirmar_fabricacion()

nuevoAuto.fabricar()
print(nuevoAuto.Rojo)

nuevoAuto.confirmar_fabricacion()
