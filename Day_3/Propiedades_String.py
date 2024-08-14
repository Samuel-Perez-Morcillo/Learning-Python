# Una de las propiedades mas importantes de los strings es su inmutabilidad

# Un String puede ocupara varias lineas de código sin usar \n

nombre = """Al usar las tres comillas
cada vez que le de a enter
generare un salto de linea
Fácil."""
print(nombre)

# Puedo preguntar si existe una determinada palabra dentro de mi texto

nombre = """Al usar las tres comillas
cada vez que le de a enter
generare un salto de linea
Fácil."""
print("salto" in nombre)


# Podremos conocer el largo de nuestro texto incluyendo espacios

nombre = """Al usar las tres comillas
cada vez que le de a enter
generare un salto de linea
Fácil."""
print("El largo de nuestro texto es " + str(len(nombre)))

