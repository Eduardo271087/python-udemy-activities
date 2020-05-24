def estudiantes():
  print("Genios mis estudiantes parte de mi familia digital")

estudiantes()
estudiantes()

def tabla_del_7():
  for x in range(10):
    print("7 * {} = {}".format(x, x * 7))

tabla_del_7()

def advierto():
  variable = 'alvaro'

advierto()

# Error en ejecución porque el ámbito es la función advierto()
# print(variable)

def advierto():
  # La variable 'variable' es global
  global variable
  variable = 'alvaro'
  print(variable)

advierto()

variable = 'Chirou'
advierto()
print(variable)
