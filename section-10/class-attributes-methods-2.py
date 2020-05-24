class Auto:
  Rojo = False

# self es this, hace referencia al objeto actual
  def __init__(self, puertas = None, color = None):
    self.puertas = puertas
    self.color = color
    if puertas is not None and color is not None:
      print("Se creó un Auto con puertas {} y color {}".format(puertas, color))
  
  def fabricar(self):
    self.Rojo = True

  def confirmar_fabricacion(self):
    if self.Rojo:
      print("Auto coloreado rojo")
    else:
      print("Aun no está coloreado")

auto = Auto("2", "Rojo")

#   File "/home/eduardo-fernandez/source/python-udemy-activities/section-10/class-attributes-methods-2.py", line 21, in <module>
#     auto = Auto()
# TypeError: __init__() missing 2 required positional arguments: 'puertas' and 'color'
# Error si los atributos del constructor no tienen valores por defecto
# auto = Auto()

auto = Auto("2", "Rojo")