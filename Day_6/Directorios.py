"""import os

# Para averigurar la ruta en la que estamos trabajando actualmente:
ruta  = os.getcwd()
print(ruta)

# Para abrir un archivo que se encuentre en una ruta diferente a la actual:

ruta = os.chdir("/Users/samuelperez/Desktop/Carpeta_Ruta_Alternativa_Python")

archivo = open("Prueba_copia.txt")

print(archivo.read())"""


# Otro metodo para poder abrir archivos alojados en otros directorios y además mas compatible
# Es el uso del objeto Path

from pathlib import Path

carpeta = Path("/Users/samuelperez/Desktop/Carpeta_Ruta_Alternativa_Python")
archivo = carpeta / "Prueba_copia.txt"

mi_archivo = open(archivo)
print(mi_archivo.read())