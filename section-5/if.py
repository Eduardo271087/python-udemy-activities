# Importante recordar los dos puntos (:)
if True:
  print('Imprimo esto porque la evaluación fue veradera')

if False:
  print('Imprimo esto porque la evaluación fue veradera')

alvaro = 10
if alvaro == 67:
  print('Alvaro vale 67')

if alvaro == 10:
  print('Alvaro vale 10')

if alvaro == 11:
  print('Alvaro vale 67')
  if alvaro == 10:
    print('Alvaro vale 10')

if alvaro == 11 and alvaro == 10:
  print('Entró')

if alvaro == 11 or alvaro == 10:
  print('Entró')
