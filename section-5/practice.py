print('Elige tu propio camino')
inicio = input("Escribe empezar para iniciar el programa: ")
while inicio == "empezar":
  print("""¿Qué camino quieres elegir?
  Escribe la opción con número:
  1.- Quiero que me saludes.
  2.- Deseo multiplicar ya que no sé cómo hacerlo.
  3.- Quiero salir de este programa, ya que aprendí a multiplicar con el curso de Álvaro.""")
  opcion = input()
  if opcion == '1':
    print("Te saludo")
  elif opcion == '2':
    numero1 = float(input('Introduce el primer valor a multiplicar: '))
    numero2 = float(input('Introduce el segundo valor a multiplicar: '))
    print('El resultado es: ', str(numero1 * numero2))
  elif opcion == '3':
    print('Excelente decisión que hayas tomado el curso de Álvaro.')
    break
  else:
    print('No sé qué elegiste, tuviste que haber puesto algún número de las opciones, se nota que no tomaste el curso de Álvaro.')