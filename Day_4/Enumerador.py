lista = ["a", "b", "c"]
indice = 0

for item in lista:
    print(indice, item)
    indice += 1


# Con el Enumerador lo podremos hacer de una forma mas optima:

lista = ["a", "b", "c"]

for item in enumerate(lista):
    print(indice, item)

# Ejemplo 1

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice , nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

# Ejemplo 2

string = "Python"

lista_indices = [(indice, caracter) for indice, caracter in enumerate(string)]

print(lista_indices)

# Ejemplo 3
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano","Melisa"]

for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(indice)