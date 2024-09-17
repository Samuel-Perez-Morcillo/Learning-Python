# Es importante tener el archivo a abrir en una codificacion legible para el programa
# Cada Linea esta compuesta por un salto de linea en caso de querer omitirlo podemos usar el metodo rstrip()
# Siempre añadiremos el metodo close cuando hagamos un programa que abra un archivo de nuestro PC


mi_archivo = open("Prueba.txt", encoding="latin-1")

"""print(mi_archivo.read())"""

"""
print(mi_archivo.readline().rstrip())
print(mi_archivo.readline())
print(mi_archivo.readline())
"""

# Podemos iterar sobre las lineas

"""
for l in mi_archivo:
    print("Aqui dice : " + l)
"""

# Si usamos el metodo readlines() se generará una lista con las frases

todas = mi_archivo.readlines()
todas = todas.pop()
print(todas)

mi_archivo.close()
