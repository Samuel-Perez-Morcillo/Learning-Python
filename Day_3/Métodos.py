# Mayúsculas

mi_texto = "Este es el texto de prueba"
resultado = mi_texto.upper()
print(resultado)

# Método Split

resultado = mi_texto.split()
print(resultado)

resultado = mi_texto.split("t")  # Tomará como separador cada vez que encuentre una t
print(resultado)

# Método Join
a = "hola"
b = "que tal"
c = "estas"
d = " ".join([a, b, c])
print(d)

# Método Find
# La diferencia que tiene respecto a Index es que si la letra
# buscada no esta en el texto arroja un -1 y no un Error

texto = "Buscame a ver que encuentras"
resultado = texto.find("w")
print(resultado)

# Reemplazar, Método replace