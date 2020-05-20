# El else se usa cuando termina el ciclo, excepto cuando se hac break
iteracion = 1
while iteracion <= 0:
  iteracion += 1
  print('Estoy iterando, van = ', iteracion)
else:
  print('Imprimo esto porque se terminó y es el else')

iteracion = 1
while iteracion <= 3:
  iteracion += 1
  print('Estoy iterando, van = ', iteracion)
  break
else:
  print('Imprimo esto porque se terminó y es el else')

iteracion = 0
while iteracion <= 10:
  iteracion += 1
  if iteracion == 4:
    print('Estoy iterando, van = ', iteracion)
    break
else:
  print('Imprimo esto porque se terminó y es el else')