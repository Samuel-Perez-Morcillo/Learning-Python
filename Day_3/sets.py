# Dentro de los sets solo puedes poner un único argumento
mi_set = set([1, 2, 3, 4, 5 ])

# No imprimirá si un valor se halla repetido
mi_set1 = set((1, 2, 3, 4, 5, 1, 1, 3))
print(type(mi_set1))
print(mi_set1)

# Los sets no admiten diccionarios ni listas, pero si tuplas
# Esto se debe a que los tuples son inmutables y los sets requieren que sus elementos sean inmutables

mi_set1 = set((1, 2, 3, 4, 5, (1, 2)))
print(mi_set1)

# Se pueden unir dos sets distintos
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)   # Elimina un 3 porque se encuentra repetido

# Se pueden agregar mas elementos y eliminarlos
set = {1,2,3}
set.add(4)
set.remove(1)

print(set)
