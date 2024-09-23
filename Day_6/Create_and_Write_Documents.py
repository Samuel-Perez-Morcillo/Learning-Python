archivo = open("prueba.txt", "a")

archivo.write("Actualizado 19:56")


archivo.close()

"""
Hay que tener en cuenta que el metodo de escritura al poner W, sobreescribirá toda la información
que contenia el documento.
Al usar "a" no se sobreescribirá la información, simplemente se escribirá lo que queramos al final del documento
Al usar "r" solo se abrirá el documento y no se podrá escribir.
"""