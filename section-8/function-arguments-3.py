def argu(*tu):
  for tus in tu:
    print(tus)

argu('alvaro', 'chirou', 'estudiantes', 10, [1, 2, 3])

def nombre_diccionario(**lo):
  print(lo)

nombre_diccionario(alvaro = 'chirou', Estudiantes = 'Genios', calificaciones = [7, 8, 9])

def nombre_diccionario1(**lo):
  for x in lo:
    print(x)

nombre_diccionario1(alvaro = 'chirou', Estudiantes = 'Genios', calificaciones = [7, 8, 9])

def nombre_diccionario2(**lo):
  for x in lo:
    print(x, " ", lo[x])

nombre_diccionario2(alvaro = 'chirou', Estudiantes = 'Genios', calificaciones = [7, 8, 9])

# Envío de argumentos por posición y por nombre al mismo tiempo
def nombre_diccionario3(*tu, **lo):
  b = 0
  for tus in tu:
    b += tus
  print(b)

  for x in lo:
    print(x, " ", lo[x])

nombre_diccionario3(1, 2, 3, 4, alvaro = 'chirou', Estudiantes = 'Genios', calificaciones = [7, 8, 9])