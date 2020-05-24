variable = float(input("Introduce algo: "))
# Si se introduce una letra
#    File "/home/eduardo-fernandez/source/python-udemy-activities/section-9/multiple-exceptions.py", line 1, in <module>
#      variable = float(input("Introduce algo: "))
# ValueError: could not convert string to float: 'l'

a = 2
print("Resultado: ", a * variable)

try:
  variable = float(input("Introduce un número: "))
  a = 2
  print("Resultado: ", a * variable)
except:
  print("Ingresaste cualquier otra cosa menos la que se te pidió")

while True:
  try:
    variable = float(input("Introduce un número: "))
    a = 2
    print("Resultado: ", a * variable)    
  except:
    print("Ingresaste cualquier otra cosa menos la que se te pidió, te voy a dar otra oportunidad")
  else:
    print("Iniciaste sesión perfectamente, amigo")
    break

while True:
  try:
    variable = float(input("Introduce un número: "))
    a = 2
    print("Resultado: ", a * variable)    
  except:
    print("Ingresaste cualquier otra cosa menos la que se te pidió, te voy a dar otra oportunidad")
  # El else se ejecuta cuando no se arrojan excepciones
  else:
    print("Iniciaste sesión perfectamente, amigo")
    break
  # El finally se ejecuta siempre
  finally:
    print("Perfecto mi amigo, terminó todo esto")