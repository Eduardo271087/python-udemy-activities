def estudiante():
  return "Mis estudiantes son unos genios"

print(estudiante())

def estudiantes():
  return [5, 6, 4, 7]

print(estudiantes())

print(estudiantes()[0:2])

def estudiante1():
  return "Álvaro Chirou", "Mis estudiantes", 10, [5, 6, 4, 7]

print(estudiante1())

a, b, c, d = estudiante1()
print(a)
print(b)
print(c)
print(d)

def multiplicacion(i, x):
  return i * x

print(multiplicacion(5, 5))

variable = multiplicacion(5, 5)
print(variable)