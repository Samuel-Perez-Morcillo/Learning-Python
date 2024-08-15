# Asociaciones de tipo clave-valor
# A diferencia de las listas el orden es irrelevante

diccionario = {"c1": "valor1", "c2": "valor2"}
print(type(diccionario))
print(diccionario)

# Si necesito hacer una llamada a una clave en particular se realizará asi:

resultado = diccionario["c1"]
print(resultado)

# Ejemplo más real

cliente = {
    "nombre": "Juan",
    "apellido": "Perez",
    "peso": 88,
    "talla_Zapatos": 43.5,
}

consulta = cliente["apellido"]
print(consulta)

# Ejercicio: Imprime en una sola linea de código la letra "e" pero En Mayúscula.
dic = {"c1": ["a", "b", "c"], "c2": ["d", "e", "f"]}
print(dic["c2"][1].upper())
