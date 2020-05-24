# Las variables no se modifican dentro de las funciones
def estudiantes(valor):
  valor *= 3

variable = 15

estudiantes(variable)
print(variable)

# Las listas sí se modifican dentro de las funciones
def listas(numero):
  for x, i in enumerate(numero):
    numero[x] *= 3

lista = [50, 100, 150]
listas(lista)
print(lista)

lista1 = [50, 100, 150]
# Para evitar la modificación de la lista dentro de la función se agrega
# : dentro de los corchetes
listas(lista1[:])
print(lista1)

def estudiantes1(valor):
  return valor * 3

variable = 15
variable = estudiantes1(variable)
print(variable)