def atras(segundos):
  segundos -= 1
  if segundos >= 0:
    print(segundos)
    atras(segundos)
  else:
    print('Terminó la cuenta atrás')

atras(10)

e = int("15")
print(e)

print(bin(15))

print(hex(15))

print(abs(-15))

print(round(5.5))

print(round(5.4))

print(len("alvaro"))

print(help())