diccionario = {'Álvaro' : 'Chirou', 'Estudiantes' : 'Genios'}

print(type(diccionario))

print(diccionario['Álvaro'])

diccionario['Álvaro'] = 'Profesor'
print(diccionario['Álvaro'])

print(diccionario)

del(diccionario['Álvaro'])

print(diccionario)

edades_de_mis_estudiantes = {'estudiante': 20, 'otros' : 30}
print(edades_de_mis_estudiantes)

edades_de_mis_estudiantes['estudiante'] += 1
print(edades_de_mis_estudiantes)

print(edades_de_mis_estudiantes['estudiante'] + edades_de_mis_estudiantes['otros'])

for edades in edades_de_mis_estudiantes:
  print(edades)

for edades in edades_de_mis_estudiantes:
  print(edades, edades_de_mis_estudiantes[edades])

lista = []
lista.append(edades_de_mis_estudiantes)

print(lista)

edades_de_mis_estudiantes = {'masestudiantes': 40, 'masgenios' : 50}
lista.append(edades_de_mis_estudiantes)

print(lista)