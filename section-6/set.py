# Los conjuntos son colecciones no ordenadas de objetos únicos
con = {5, 4, 3}

print(con)

con.add(2)

print(con)

con.add(6)

print(con)

con.add('H')

print(con)

con.add('B')
con.add('Y')

print(con)

con.add('A')
con.add('Z')

print(con)

coleccion = {'Mis estudiantes', 'Yo', "Vos"}
print('Vos' in coleccion)

print('Cualquier' in coleccion)

repetido = {'Repetido', 'Repetido', 'Repetido', 'Repetido', 'Repetido', 'Repetido'}
print(repetido)

lista = [5, 5, 6, 6, 7, 7]
print(lista)

# set convierte la lista en conjunto (set)
conjunto = set(lista)
print(conjunto)

cadena = "Álvaro esta clase se está haciendo muy larga, esto ya es lo último"
print(set(cadena))