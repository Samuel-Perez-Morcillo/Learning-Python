# Crea una función llamada abrir_leer() que abra (open) un archivo indicado
# como parámetro, y devuelva su contenido (read).
def abrir_leer(ruta_archivo):
    with open(ruta_archivo, "r") as archivo:
        contenido = archivo.read()
        return contenido


# Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro,
# y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"
def sobrescribir(ruta_archivo):
    with open(ruta_archivo, "w") as archivo:
        archivo.write("contenido eliminado")


# Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro,
# y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución".
# Finalmente, debe cerrar el archivo abierto.
def registro_error(texto_archivo):
    with open(texto_archivo, "a") as archivo:
        archivo.write("se ha registrado un error de ejecución")
