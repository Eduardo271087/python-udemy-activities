# Last In - First Out (LIFO)
apilar = [1, 2, 3, 4]
apilar.append(3)
apilar.append(6)
apilar.append(8)
print(apilar)

# pop() para desapilar
print(apilar.pop())

print(apilar)

no_perderlo = apilar.pop()

print(no_perderlo)

print(apilar.pop())
print(apilar.pop())
print(apilar.pop())
print(apilar.pop())
print(apilar.pop())

# Error en ejecución porque no hay más elementos para desapilar
# print(apilar.pop())