# Las tuplas son inmutables, a diferencia de las listas
t = ('Álvaro', 'Chirou', 'Estudiantes', 10, [1, 2, 8], 10, -80)
l = ['Álvaro', 'Chirou', 'Estudiantes', 10, [1, 2, 8], 10, -80]

print(t)

print(t[0])

print(t[3])

print(t[2])

print(t[2:])

# Error en ejecución porque las tuplas son inmutables
# t[0] = 'Los estudiantes'

l[0] = 'Los estudiantes'

print(l[0])

print(len(t))

print(len(t[2]))

print(t.index('Estudiantes'))

# Error en ejecución porque la tupla no contiene 'otro'
# print(t.index('otro'))

print(t.count(10))

# Error en ejecución porque las tuplas son inmutables
# t.append('a')