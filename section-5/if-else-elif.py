alvaro = 10
if alvaro % 2 == 0:
  print('El resto es 0')
else:
  print('El resto no es 0')

frase = "Alvaro"
if frase == "Entrar":
  print('Bienvenid@s')
elif frase == 'hola':
  print('Nos están saludando')
else:
  print('Esto es algo cuando no da ningún resultado')

  final = float(input('Coloca la nota: '))
  if final >= 9:
    print('Sos un genio')
  elif final >= 7:
    print('Aprobaste!')
  elif final == 6:
    print('Te faltó poco')
  elif final <= 5:
    print('Tuviste que haber estudiando en el curso de Python de Álvaro')
  else:
    print('No sé dónde estudias porque la nota que pusiste no la puedo evaluar!')