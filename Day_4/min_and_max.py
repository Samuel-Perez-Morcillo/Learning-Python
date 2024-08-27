menor = min(56,54,32,34)
print(menor)

mayor = max(56,54,32,34)
print(mayor)

# Comportamiento con los strings
# Con los stings es importante tener en cuenta que se deben de buscar en minusculas
# ya que se hace un orden distinto entre Mayus y Minusculas

nombre = "Samuel"
menor = min(nombre.lower())
print(menor)

# Comportamiento con los diccionarios
dic = {"C1":45, "C2":11}
print(min(dic))
print(min(dic.values()))

# Ejemplo 1
lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

maximo = max(lista_numeros)
minimo = min(lista_numeros)

rango = maximo - minimo

# Ejemplo 2

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)
