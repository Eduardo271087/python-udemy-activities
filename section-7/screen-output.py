print("Hola mi querida familia digital")

variable = 'Álvaro Chirou'
otra = 'Genios estudiantes'

# Así se usan los placeholders en Python
forma = "El profesor '{}' y sus '{}'".format(variable, otra)
print(forma)

forma = "El profesor '{1}' y sus '{0}'".format(variable, otra)
print(forma)

print('{:>50}'.format('Álvaro Chirou'))