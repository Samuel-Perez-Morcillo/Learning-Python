archivo = open("prueba.txt", "a")

archivo.write("Actualizado 19:56")


archivo.close()

"""
Hay que tener en cuenta que el metodo de escritura al poner W, sobreescribirá toda la información
que contenia el documento.
Al usar "a" no se sobreescribirá la información, simplemente se escribirá lo que queramos al final del documento
Al usar "r" solo se abrirá el documento y no se podrá escribir.
"""


""" Ejercicios de Prueba"""
# 1
archivo = open("mi_archivo.txt", "w")
archivo.write("Nuevo texto")
archivo.close()

archivo_lectura = open("mi_archivo.txt", "r")
print(archivo_lectura.read())

archivo_lectura.close()

# 2

archivo = open("mi_archivo.txt","a")
archivo.write("Nuevo inicio de sesión")
archivo.close()

archivo_lectura = open("mi_archivo.txt", "r")
print(archivo_lectura.read())
archivo_lectura.close()

# 3

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

archivo = open("registro.txt", "a")
archivo.writelines(["\t".join(registro_ultima_sesion) + "\n"])
archivo.close()

archivo_read = open("registro.txt", "r")
print(archivo_read.read())
archivo_read.close()