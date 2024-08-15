# Podemos extraer una posición cualquiera de las listas
lista = ["a", "b", "c", 55, 2.5]
resultado = lista[3]
print(f"""Hay que seguir teniendo en cuenta que se empieza
por 0 entonces si pongo índice 3 extraere {resultado} """)

# Podemos concaterar listas y formar una única que contenga todo
lista = ["a", "b", "c"]
lista2 = [20, "hola", 12.5]
lista_3 = lista + lista2
print(lista_3)


# En las listas podemos sobre escribir cualquiera de sus elementos
lista = ["a", "b", "c"]
lista2 = [20, "hola", 12.5]
lista_3 = lista + lista2
lista_3[0] = "DeadPool"
print(lista_3)


# Tambien Con el método Append() podremos agregar otro elemento a la lista (Al final)
# Podremos eliminar elementos de la lista con el método pop()
lista = ["a", "b", "c"]
lista2 = [20, "hola", 12.5]
lista_3 = lista + lista2
lista_3.append("soy el nuevo")
lista_3.pop()   # Si no pongo ningun índice interpreta que es el último
print(lista_3)

# Existen Métodos Para ordernar las listas
lista = ["g", "a", "h", "z", "y", "b"]
lista.sort()    # El Método Sort no puede almacenar datos "NON_TYPE"
print(lista)

# Se pueden ordenar las listas al revés
lista = ["g", "a", "h", "z", "y", "b"]
lista.sort()
lista.reverse()
print(lista)
