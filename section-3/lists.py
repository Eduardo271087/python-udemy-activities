listas = [5, 9, "Alvaro", -8, "estudiantes"]

print("listas[0]: '" + str(listas[0]) + "'")

print("listas[-1]: '" + str(listas[-1]) + "'")

print("listas[2]: '" + str(listas[2]) + "'")

print("listas[2:]: '" + str(listas[2:]) + "'")

primera_parte = [1, 2, 3, 4]
segunda_parte = [5, 6, 7]
print("primera_parte + segunda_parte: '" + str(primera_parte) + str(segunda_parte) + "'")

numeros = [1, 2, 3, 4, 5, 9, 6, 7, 8]
print("numeros: '" + str(numeros) + "'")

numeros[4] = 5
print("numeros: '" + str(numeros) + "'")

numeros.append(10)
print("numeros: '" + str(numeros) + "'")

numeros.append(10 + 1)
print("numeros: '" + str(numeros) + "'")

abecedario = ['A', 'B', 'C', 'D']
print("abecedario: '" + str(abecedario) + "'")

print("abecedario[:2]: '" + str(abecedario[:2]) + "'")

abecedario[:2] = ['a', 'b']
print("abecedario: '" + str(abecedario) + "'")

primero = [1, 2, 3]
segundo = [4, 5, 6]
tercero = [7, 8, 9]
cuarto = [10, 11, 12]
anidadas = [primero, segundo, tercero, cuarto]
print("anidadas: '" + str(anidadas) + "'")

print("anidadas[0]: '" + str(anidadas[0]) + "'")

print("anidadas[1][0]: " + str(anidadas[1][0]) + "'")