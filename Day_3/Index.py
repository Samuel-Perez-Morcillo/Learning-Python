mi_texto = "Esta es una Prueba"
resultado = mi_texto[8]
print(resultado)

mi_texto = "Esta es una Prueba"
resultado = mi_texto.index("u")
print(resultado)

# Tambien podremos fijar de forma concreta la búsqueda

mi_texto = "Esta es una Prueba"
resultado = mi_texto.index("u", 9)
print(resultado)

# Tambien existe el método rIndex que es igual pero busca
# de derechas a izquierdas

mi_texto = "Esta es una Prueba"
resultado = mi_texto.rindex("u")
print(resultado)

# Ejercicio

# Extrae en que posición empieza la ultima palabra "práctica"

frase = "En la teoria, la práctica y la teoria son lo mismo, en la práctica no lo son"
resultado = frase.rindex("práctica")
print(resultado)