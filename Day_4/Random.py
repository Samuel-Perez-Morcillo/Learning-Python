# Random necesita ser importado

from random import *

# Randint
aleatorio = randint(1,50)
print(aleatorio)

# Uniform
aleatorio = round(uniform(1,5), 2)
print(aleatorio)

# Random
aleatorio = random()
print(aleatorio)

# Choice
colores = ["azul", "rojo", "verde", "amarillo", "gris"]
aleatorio = choice(colores)
print(aleatorio)

# Shuffle
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)