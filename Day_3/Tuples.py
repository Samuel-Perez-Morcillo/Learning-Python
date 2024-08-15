mi_tuple = (1, 2, 3, 4, 5)
print(type(mi_tuple))

# Los Tuples son inmutables al igual que los strings

# Podemos almacenar los valores de las tuplas
mi_tuple = (1,2,3,4,5,"h")
a,b,c,d,e,f = mi_tuple
print(f)

# Podemos contar cuantas veces aparece repetido un valor dentro de una tupla
ejemplo = (1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 1,)
recuento = ejemplo.count(1)
print(f"El valor 1 aparece repetido en la tupla {recuento} veces")
