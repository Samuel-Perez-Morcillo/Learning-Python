# Para Fragmentar un texto podemos coger desde el principio hasta un fin determinado:
mi_texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
fragmento = mi_texto[:4]  # La posición 4 no esta incluida
print(fragmento)

# Para Fragmentar desde un inicio determinado hasta el final
mi_texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
fragmento = mi_texto[4:]
print(fragmento)

# Desde un principio determinado hasta un final determinado
mi_texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
fragmento = mi_texto[2:5]  # La posición 5 no está incluida
print(fragmento)

# Extraer Caracteres con saltos determinados
mi_texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
fragmento = mi_texto[2:5:2]
print(fragmento)

mi_texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
fragmento = mi_texto[2:9:2]
print(fragmento)

# Como curiosidad También podremos poner nuestra cadena al revés
mi_texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
fragmento = mi_texto[::-1]
print(fragmento)