try:
  a = float(input("Número: "))
  10 / a
except TypeError:
  print("Esto es una cadena querido")
except ValueError:
  print("La cadena debe ser un número")
except ZeroDivisionError:
  print("No se puede dividir entre cero")
except Exception as x:
  print(type(x).__name__)

def profesor(estudiantes = None):
  if estudiantes is None:
    print("Debes escribir algo, sino no llames a la función")

profesor('algo')

profesor()

def profesor1(estudiantes = None):
  try:
    if estudiantes is None:
      raise ValueError("Debes escribir algo, sino no llames a la función")
  except ValueError:
    print("No amigo, el valor nulo no se permite")

profesor1()