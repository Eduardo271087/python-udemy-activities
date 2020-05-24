def funciones(a, b):
  return a - b

print(funciones(2, 2))

# Envío de argumentos por nombre
print(funciones(b = 2, a = 1))

print(funciones(a = 2, b = 1))

def nulos(x = None, i = None):
  if x == None or i == None:
    print('Amigo, debes ingresar los dos números')
    return
  return x / i

print(nulos())

print(nulos(2, 2))