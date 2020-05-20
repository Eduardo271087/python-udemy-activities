lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
indice = 0
while indice < len(lista):
  print(lista[indice])
  indice += 1

for item in lista:
  print(item)

for item in lista:
  item *= 15
  print(item)

indice = 0
for item in lista:
  lista[indice] *= 10
  print(lista[indice])
  indice += 1

for item in lista:
  print(item * 10)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
indice = 0
for indice, item in enumerate(lista):
  lista[indice] *= 10
print(lista)

string = 'Alvaro'
for caracter in string:
  print(caracter)

for i in range(10):
  print(i)

print(range(10))

for i in [1, 2, 3, 4, 5]:
  print(i)

print(list(range(10)))