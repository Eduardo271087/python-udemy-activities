# First In - First Out (FIFO)
# Así se importan las librerías en Python
from collections import deque

colas = deque()
print(colas)

print(type(colas))

colas = deque(['Álvaro', 'Estudiantes', 'Familia', 'Genios'])
print(colas)

# Las colas permiten sacar el primero y el último elemento
# Las pilas solamente permiten sacar el último
print(colas.pop())

# popleft() no funciona en las pilas
print(colas.popleft()) 