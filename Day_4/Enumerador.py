lista = ["a", "b", "c"]
indice = 0

for item in lista:
    print(indice, item)
    indice += 1


# Con el Enumerador lo podremos hacer de una forma mas optima:

lista = ["a", "b", "c"]

for item in enumerate(lista):
    print(indice, item)
